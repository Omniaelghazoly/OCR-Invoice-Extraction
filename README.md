 ## 🧾 OCR Invoice Extraction with LangChain & Streamlit

This project allows you to extract structured data from invoice images using LangChain, Google Generative AI, and a Streamlit web interface. It processes uploaded invoice images and returns key details like buyer name, invoice number, invoice date, and itemized purchases.

## 🧰 Tech Stack
LangChain for LLM-based processing

Google Generative AI via langchain_google_genai

Streamlit for UI

Pydantic for schema validation

Python 3.9+


## 🧠 How It Works
User uploads an invoice image.

The image is converted to base64.

LangChain sends a prompt with the image and an output schema to Google Generative AI.

The LLM extracts structured invoice data based on few-shot examples.

The output is returned as JSON and displayed in the UI.


