import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Load the sentence similarity pipeline
pipe = pipeline("sentence-similarity", model="sentence-transformers/all-MiniLM-L6-v2")

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
        # Compute similarity between question and text
        similarity = pipe(question, text)
        # Sort similarity scores and return the most relevant answer
        most_similar = sorted(similarity, key=lambda x: x['score'], reverse=True)[0]
        return most_similar['text']
    
# Example usage
if __name__ == "__main__":
    url = "https://huggingface.co/docs/hub/sentence-transformers"  # Replace with the URL of the website you want to query
    question = "what is sentence-transformers "  # Replace with the query you want to perform
    answer = answer_question(url, question)
    print("Answer:", answer)
