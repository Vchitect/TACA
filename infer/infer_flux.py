import torch
from pipeline_taca_flux import FluxPipeline

pipe = FluxPipeline.from_pretrained("path/to/ckpts", torch_dtype=torch.bfloat16)
pipe = pipe.to("cuda")

prompt = "A beautiful landscape with mountains and a river."

# Uncomment the following line if you just want training-free inference
pipe.load_lora_weights('path/to/lora_weights')

image = pipe(
    prompt,
    num_inference_steps=30,
).images[0]

image.save(f"out.png")