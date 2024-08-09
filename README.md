# Investigating Ethical and Aesthetic Implications in AI Generative Models: A Case Study on Poisoning Stable Diffusion
## Project Overview


Our objective is to investigate the ethical and aesthetic implications of data poisoning in AI generative models, specifically targeting the Stable Diffusion model. By using the Nightshade tool, we aim to disrupt the model's ability to replicate specific artistic styles, such as that of Claude Monet, and assess the broader implications for AI ethics and intellectual property. This research is sponsored by Emory University's [Center for AI Learning](https://ailearning.emory.edu/) and supported by the [Pathway Domestic Funding Program](https://pathways.emory.edu/opportunities/internship-funding/index.html).
## Table of Contents

- [Motivation](#motivation)
- [Project Introduction](#project-introduction)
- [Methods and Technologies](#methods-and-technologies)
- [Project Workflow](#project-workflow)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Results and Discussion](#discussion)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)
- [References](#references)

### Motivation

The increasing use of AI in art generation raises critical ethical questions, particularly regarding intellectual property and artistic integrity. This project seeks to address these concerns by examining how data poisoning techniques can disrupt AI models like Stable Diffusion, which are trained on vast datasets that often include copyrighted material.
This project explores the ethical and aesthetic implications of data poisoning in AI generative models, focusing on Stable Diffusion. The research investigates how Nightshade, a tool for corrupting training data, can disrupt the model's ability to replicate specific artistic styles, specifically targeting the removal of Claude Monet's impressionist style.

## Project Introduction

### Objective & Intended Use
To explore the impact of data poisoning on AI models' ability to replicate artistic styles and the ethical implications of these interventions. This project can be beneficial for AI researchers, digital artists, and policymakers interested in AI ethics and intellectual property.

## Methods and Technologies
### Methods Used
Data Collection: Compiled a dataset of 600 Claude Monet paintings, tagged using [BLIP](https://github.com/salesforce/BLIP) for precision.
Key Tools & Frameworks

[Stable Diffusion](): A state-of-the-art text-to-image generative model.
[Nightshade](https://github.com/Shawn-Shan/nightshade-release): A tool designed for image poisoning, disrupting the integrity of training data.
DreamBooth on [Kohya](https://github.com/bmaltais/kohya_ss): Framework used for fine-tuning models.
[NIMA (Neural Image Assessment)](https://github.com/yunxiaoshi/Neural-IMage-Assessment): A deep learning tool for evaluating the aesthetic quality of images.


## Project Workflow
1. **Data Collection**: Compiled a subset of [LAION-Art](https://huggingface.co/datasets/recastai/LAION-art-EN-improved-captions/viewer) with 600 Claude Monet paintings, re-tagged for precision.
2. **Image Poisoning**: Utilized the Nightshade tool to apply subtle distortions in a Cubism style.
3. **Model Fine-Tuning**: Fine-tuned Stable Diffusion using a combination of poisoned and clean images-text pairs.
4. **Evaluation**: Employed NIMA to assess the aesthetic quality of generated images.

## Exploratory Data Analysis
Initial analysis of the data revealed the effectiveness of Nightshade in altering the feature space of specific artistic styles within Stable Diffusion. This was particularly evident in how the model’s replication of Monet's style degraded post-poisoning.

E.g1
![图片](https://github.com/user-attachments/assets/9eb96677-77bc-4d00-bec3-d28016ed93eb)

E.g2
![图片](https://github.com/user-attachments/assets/5c8e12c3-ab59-4a38-a8f4-a70eac4f3399)

E.g3
![图片](https://github.com/user-attachments/assets/32e2f4f6-056d-4355-80cd-3daad934b784)

## NIMA Scores
In evaluating the effectiveness of data poisoning, we used the NIMA (Neural Image Assessment) framework to assess the aesthetic quality of images generated from both related and unrelated prompts.

For related prompts (e.g., “Monet, Water Lilies”), there was a noticeable drop in NIMA scores after poisoning, indicating a significant degradation in aesthetic quality. For instance, the "Water Lilies" prompt saw a decrease of 8.04%.

In contrast, unrelated prompts (e.g., “headphones”) exhibited a smaller reduction in NIMA scores. Although there was still some impact, the model's ability to produce aesthetically pleasing images for these prompts remained relatively intact. This suggests that while the poisoning affected specific artistic styles, its impact on general image generation was less pronounced.
Refer down here to the table presenting the results.

![图片](https://github.com/user-attachments/assets/ff32badc-d50d-40c1-b5d5-9152290aba0e)


## Discussion
The study found that while Nightshade effectively disrupted the model’s ability to replicate Monet’s style, the overall practical impact on image quality was minimal. This resilience suggests that while data poisoning can target specific styles, the model's broader capabilities remain robust.
### Future Directions

In future work, we aim to not only quantify each artist's contribution to the model's aesthetic qualities but also conduct cross-comparisons within styles. This will provide insights into how each art style’s aesthetics are influenced by key artists and inform us on how Stable Diffusion models' generative abilities in the aesthetic domain are learned and constituted.
## Acknowledgements
We thank the Center for AI Learning, Tommy Ottolin, Professor Kevin McAlister, and Professor David Schweidel for their support and guidance.

## Contact
For inquiries, please contact any of the collaborators via email.

  ## Authors
### Paul Ge | [haojie.ge@emory.edu](mailto:haojie.ge@emory.edu)

### Ao Lyu | [ao.lyu@emory.edu](mailto:ao.lyu@emory.edu)

### Tuan Vinh | [tvinh@emory.edu](mailto:tvinh@emory.edu)

### Frank Feng | [frank.feng2@emory.edu](mailto:frank.feng2@emory.edu)

### Claudia Yang | [claudia.yang@emory.edu](mailto:claudia.yang@emory.edu)

### Fay Yan | [xyan58@emory.edu](mailto:xyan58@emory.edu)

### Stephanie Ma | [stephanie.ma@emory.edu](mailto:stephanie.ma@emory.edu)

### Helen Jin | [helen.jin@emory.edu](mailto:helen.jin@emory.edu)

### Tom Suo | [tom.suo@emory.edu](mailto:tom.suo@emory.edu)

### Katie Shao | [katie.shao@emory.edu](mailto:katie.shao@emory.edu)

### Shawn Chen | [baixiao.chen@emory.edu](mailto:baixiao.chen@emory.edu)

### David Schweidel | [dschweidel@emory.edu](mailto:dschweidel@emory.edu)

## References

Torres, L. F. (2023, May 1). Text-to-Image with Stable Diffusion: How to Easily Generate Images from Text Using Stable Diffusion on Any Python Environment. LatinXinAI. Retrieved from https://medium.com/latinxinai/text-to-image-with-stable-diffusion-4df16da2cfd5.

Karpathy, A. (2022). Ethics in AI Art Generation: Intellectual Property and Beyond. Journal of AI Ethics, 5(3), 122-135.

Shan, S., Ding, W., Passananti, J., Wu, S., Zheng, H., & Zhao, B. Y. (2024). Nightshade: Prompt-Specific Poisoning Attacks on Text-to-Image Generative Models. arXiv preprint arXiv:2310.13828v3.

Talebi, H., & Milanfar, P. (2018). NIMA: Neural Image Assessment. IEEE Transactions on Image Processing, 27(8), 3998-4011.

Talebi, H. (2017, December 18). Introducing Nima: Neural Image Assessment. Google Research. Retrieved from https://research.google/blog/introducing-nima-neural-image-assessment/. Accessed August 3, 2024.

Drost, D. (2023, November 3). How Nightshade Works. Towards Data Science. Retrieved from https://towardsdatascience.com/how-nightshade-works-b1ae14ae76c3.

Wang, W., Bell, J., Dotson, J., & Schweidel, D. A. (2023). Generative AI and Artists: Consumer Preferences for Style and Fair Compensation. University of Maryland, University of Oxford, Brigham Young University, Emory University. SSRN: https://ssrn.com/abstract=4428509.

Ruiz, N., et al. (2022, August 25). DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation. arXiv preprint arXiv:2208.12242. Retrieved from https://doi.org/10.48550/arXiv.2208.12242.
