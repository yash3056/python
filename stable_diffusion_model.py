from diffusers import StableDiffusionPipeline

import torch

model_id = "runwayml/stable-diffusion-v1-5"

# Disable GPU usage (I don't have a GPU)
torch.cuda.is_available = lambda: False

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

prompt = "a photo of a man on the moon"
image = pipe(prompt).images[0]

image.save("man_on_moon.png")