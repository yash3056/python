from diffusers import StableDiffusionPipeline

import torch

model_id = "runwayml/stable-diffusion-v1-5"

# Disable GPU usage (I don't have a GPU)
torch.cuda.is_available = lambda: False

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]

image.save("astronaut_rides_horse.png")