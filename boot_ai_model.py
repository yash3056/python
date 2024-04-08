from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from PyPDF2 import PdfReader

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/pythia-160m")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/pythia-160m")

# Specify the device to use (Intel Integrated GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Disable the warning messages
torch.autograd.set_grad_enabled(False)

while True:
    # Take user input for the prompt
    prompt = input("Enter the prompt for text generation (or type 'quit' to exit): ")

    # Check if the user wants to exit
    if prompt.lower() == "quit":
        print("Exiting...")
        break
    elif prompt.lower() == "file":  # If user wants to input text from a file
        file_path = input("Enter the path to the PDF file: ")
        try:
            # Open the PDF file
            with open(file_path.strip("'& "), "rb") as file:
                # Initialize PDF reader
                pdf_reader = PdfReader(file)
                # Extract text from each page of the PDF
                text = ""
                for page_num in range(len(pdf_reader.pages)):
                    text += pdf_reader.pages[page_num].extract_text()
                prompt = text.strip()  # Remove leading/trailing whitespace
        except FileNotFoundError:
            print("File not found. Please try again.")
            continue

    # Encode the prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate text
    output_sequences = model.generate(
        input_ids=input_ids,
        max_length=400000,  # Adjust the maximum output length as needed
        num_return_sequences=3,  # Number of different outputs to generate
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,  # Adjust temperature for more or less creative text
        pad_token_id=tokenizer.eos_token_id,  # Set pad_token_id to eos_token_id for open-end generation
    )

    # Decode and print the generated text
    for i, generated_sequence in enumerate(output_sequences):
        print(f"Generated Sequence {i+1}: {tokenizer.decode(generated_sequence, skip_special_tokens=True)}")
