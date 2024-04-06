import google.generativeai as genai
import os
from markdownify import markdownify as to_markdown

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
model = genai.GenerativeModel('gemini-1.0-pro-latest')

response = model.generate_content("hello")
print(to_markdown(response.text))