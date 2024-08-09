#1dataextreaction
import os
import sys
from PIL import Image
import glob
import pickle
import argparse
import numpy as np
import random
import torch
from torchvision import transforms
from sklearn.metrics.pairwise import cosine_similarity
import clip

# Add the path to the directory containing custom modules
sys.path.append("/home/shansixioing/dos/")

def crop_to_square(img):
    size = 512
    image_transforms = transforms.Compose(
        [
            transforms.Resize(size, interpolation=transforms.InterpolationMode.BILINEAR),
            transforms.CenterCrop(size),
        ]
    )
    return image_transforms(img)

class CLIPModel:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        model, preprocess = clip.load("ViT-B/32", device=self.device)
        self.model = model.to(self.device)
        self.preprocess = preprocess
        self.tokenizer = clip.tokenize

    def text_emb(self, text_list):
        if isinstance(text_list, str):
            text_list = [text_list]
        text_tokens = self.tokenizer(text_list, truncate=True).to(self.device)
        with torch.no_grad():
            text_features = self.model.encode_text(text_tokens)
        return text_features

    def img_emb(self, img):
        image = self.preprocess(img).unsqueeze(0).to(self.device)
        with torch.no_grad():
            image_features = self.model.encode_image(image)
        return image_features

    def __call__(self, image, text, softmax=False):
        if isinstance(text, str):
            text = [text]

        if isinstance(image, list):
            image = [self.preprocess(img).unsqueeze(0).to(self.device) for img in image]
            image = torch.cat(image)
        else:
            image = self.preprocess(image).unsqueeze(0).to(self.device)

        text_tokens = self.tokenizer(text).to(self.device)

        if softmax:
            with torch.no_grad():
                logits_per_image, logits_per_text = self.model(image, text_tokens)
                probs = logits_per_image.softmax(dim=-1).cpu().numpy()
            return probs
        else:
            with torch.no_grad():
                image_features = self.model.encode_image(image)
                text_features = self.model.encode_text(text_tokens)

                image_features /= image_features.norm(dim=-1, keepdim=True)
                text_features /= text_features.norm(dim=-1, keepdim=True)
                similarity = text_features.cpu().numpy() @ image_features.cpu().numpy().T
                score = similarity[0][0]

            return score

def main(args):
    clip_model = CLIPModel()
    data_dir = args.directory
    source_concept = args.concept
    os.makedirs(args.outdir, exist_ok=True)
    all_data_files = glob.glob(os.path.join(data_dir, "*.p"))

    res_list = []
    for idx, data_file in enumerate(all_data_files):
        with open(data_file, "rb") as f:
            cur_data = pickle.load(f)
        cur_img = Image.fromarray(cur_data["img"])
        cur_text = cur_data["text"]
        cur_key = cur_data.get("key", f"unknown_key_{idx}")

        cur_img = crop_to_square(cur_img)
        score = clip_model(cur_img, f"a photo of a {source_concept}")
        if score > 0.24:
            res_list.append((cur_img, cur_text, cur_key))

    if len(res_list) < args.num:
        raise Exception("Not enough data from the source concept to select from. Please add more in the folder.")

    all_prompts = [d[1] for d in res_list]
    if not all_prompts:
        raise ValueError("No prompts found in the selected data.")

    print("Generating text embeddings for all prompts...")
    text_emb = clip_model.text_emb(all_prompts)
    text_emb_target = clip_model.text_emb(f"a photo of a {source_concept}")

    if text_emb is None or text_emb_target is None:
        raise ValueError("Failed to generate text embeddings.")

    text_emb_np = text_emb.cpu().float().numpy()
    text_emb_target_np = text_emb_target.cpu().float().numpy()

    if text_emb_np.shape[0] == 0 or text_emb_target_np.shape[0] == 0:
        raise ValueError("Generated embeddings are empty.")

    res = cosine_similarity(text_emb_np, text_emb_target_np).reshape(-1)
    candidates = np.argsort(res)[::-1][:300]
    random_selected_candidates = random.sample(list(candidates), args.num)
    final_list = [res_list[i] for i in random_selected_candidates]

    for i, data in enumerate(final_list):
        img, text, key = data
        cur_data = {
            "img": np.array(img),
            "text": text,
            "key": key,
        }
        with open(os.path.join(args.outdir, f"{i}.p"), "wb") as f:
            pickle.dump(cur_data, f)

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', type=str, required=True, help="Directory containing the input data files")
    parser.add_argument('-od', '--outdir', type=str, required=True, help="Directory to save the output data files")
    parser.add_argument('-n', '--num', type=int, default=100, help="Number of samples to extract")
    parser.add_argument('-c', '--concept', type=str, required=True, help="Concept to filter and compare")
    return parser.parse_args(argv)

if __name__ == '__main__':
    args = parse_arguments(sys.argv[1:])
    main(args)
