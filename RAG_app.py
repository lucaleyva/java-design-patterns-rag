import logging
from transformers import logging as hf_logging
import warnings
from dotenv import load_dotenv
import os
import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Suppress noisy logs
logging.getLogger("langchain.text_splitter").setLevel(logging.ERROR)
hf_logging.set_verbosity_error()
warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found. Make sure your .env file has OPENAI_API_KEY set.")

openai.api_key = api_key

# -----------------------------
# Parameters
# -----------------------------
chunk_size = 500
chunk_overlap = 50
model_name = "sentence-transformers/all-distilroberta-v1"
top_k = 20

# Re-ranking parameters
cross_encoder_name = "cross-encoder/ms-marco-MiniLM-L-6-v2"
top_m = 8

# Read contents of Selected_Document.txt into text variable
with open("Selected_Document.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split text into chunks using RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
)
chunks = text_splitter.split_text(text)
