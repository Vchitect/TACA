<div align="center">
<h1>TACA: Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers</h1>
</div>

<div align="center">
    <span class="author-block">
      <a href="https://scholar.google.com/citations?user=FkkaUgwAAAAJ&hl=en" target="_blank">Zhengyao Lv*</a><sup>1</sup>,</span>
    </span>
    <span class="author-block">
      <a href="https://tianlinn.com/" target="_blank">Tianlin Pan*</a><sup>2,3</sup>,</span>
    </span>
    <span class="author-block">
      <a href="https://chenyangsi.github.io/" target="_blank">Chenyang Si*</a><sup>2</sup>,</span>
    </span>
    <span class="author-block">
      <a href="https://frozenburning.github.io/" target="_blank">Zhaoxi Chen</a><sup>4</sup>,</span>
    </span>
    <span class="author-block">
      <a href="https://homepage.hit.edu.cn/wangmengzuo" target="_blank">Wangmeng Zuo</a><sup>5</sup>,</span>
    </span>
    <span class="author-block">
      <a href="https://liuziwei7.github.io/" target="_blank">Ziwei Liu</a><sup>4†</sup>,</span>
    </span>
    <span class="author-block">
      <a href="https://i.cs.hku.hk/~kykwong/" target="_blank">Kwan-Yee K. Wong</a><sup>1†</sup>
    </span>
</div>

<div align="center">
    <sup>1</sup>The University of Hong Kong &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
    <sup>2</sup>Nanjing University <br> 
    <sup>3</sup>University of Chinese Academy of Sciences &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
    <sup>4</sup>Nanyang Technological University<br> 
    <sup>5</sup>Harbin Institute of Technology
</div>
<div align="center">(*Equal Contribution.&nbsp;&nbsp;&nbsp;&nbsp;<sup>†</sup>Corresponding Author.)</div>

<p align="center">
    <a href="https://arxiv.org/abs/2506.07986/">Paper</a> | 
    <a href="https://vchitect.github.io/TACA/">Project Page</a> |
    <a href="https://huggingface.co/ldiex/TACA/tree/main">LoRA Weights</a>
</p>

# About
We propose **TACA**, a parameter-efficient method that dynamically rebalances cross-modal attention in multimodal diffusion transformers to improve text-image alignment.

https://github.com/user-attachments/assets/ae15a853-ee99-4eee-b0fd-8f5f53c308f9

# Usage
For Stable Diffusion 3.5, simply run:
``` sh
python infer/infer_sd3.py
```

For FLUX.1, run:
``` sh
python infer/infer_flux.py
```

# Benchmark
Comparison of alignment evaluation on T2I-CompBench for FLUX.1-Dev-based and SD3.5-Medium-based models.

| Model | Attribute Binding | | | Object Relationship | | Complex $\uparrow$ |
|---|---|---|---|---|---|---|
| | Color $\uparrow$ | Shape $\uparrow$ | Texture $\uparrow$ | Spatial $\uparrow$ | Non-Spatial $\uparrow$ | |
| FLUX.1-Dev | 0.7678 | 0.5064 | 0.6756 | 0.2066 | 0.3035 | 0.4359 |
| FLUX.1-Dev + TACA ($r = 64$) | **0.7843** | **0.5362** | **0.6872** | **0.2405** | 0.3041 | **0.4494** |
| FLUX.1-Dev + TACA ($r = 16$) | 0.7842 | 0.5347 | 0.6814 | 0.2321 | **0.3046** | 0.4479 |
| SD3.5-Medium | 0.7890 | 0.5770 | 0.7328 | 0.2087 | 0.3104 | 0.4441 |
| SD3.5-Medium + TACA ($r = 64$) | **0.8074** | **0.5938** | **0.7522** | **0.2678** | 0.3106 | 0.4470 |
| SD3.5-Medium + TACA ($r = 16$) | 0.7984 | 0.5834 | 0.7467 | 0.2374 | **0.3111** | **0.4505** |

# Showcases
![](static/images/short_1.png)
![](static/images/short_2.png)
![](static/images/long_1.png)
![](static/images/long_2.png)
