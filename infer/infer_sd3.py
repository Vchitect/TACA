import torch
from pipeline_taca_sd3 import StableDiffusion3Pipeline

pipe = StableDiffusion3Pipeline.from_pretrained("path/to/ckpts", torch_dtype=torch.bfloat16)
pipe = pipe.to("cuda")

prompt = "A beautiful landscape with mountains and a river."

# Comment the following line if you just want training-free inference
pipe.load_lora_weights('path/to/lora_weights')

image = pipe(
    prompt,
    num_inference_steps=30,
    guidance_scale=4.5,
).images[0]

image.save("out.png")