import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Fetch website content
def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch website content.")
        return None

# Preprocess text
def preprocess_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])
    return text

# Main function to answer question
def answer_question(url, question):
    # Fetch website content
    html_content = fetch_website_content(url)
    if html_content:
        # Preprocess text
        text = preprocess_text(html_content)
        # Use question answering pipeline from Hugging Face Transformers
        qa_pipeline = pipeline("question-answering")
        # Answer the question using the extracted text
        answer = qa_pipeline(question=question, context=text)
        return answer['answer']

# Example usage
if __name__ == "__main__":
    url = "https://huggingface.co/docs/hub/sentence-transformers"  # Replace with the URL of the website you want to query
    question = "what is sentence-transformers "  # Replace with the query you want to perform
    answer = answer_question(url, question)
    print("Answer:", answer)
