 ## 🧾 OCR Invoice Extraction with LangChain & Streamlit

This project allows you to extract structured data from invoice images using LangChain, Google Generative AI, and a Streamlit web interface. It processes uploaded invoice images and returns key details like buyer name, invoice number, invoice date, and itemized purchases.

## 🧰 Tech Stack
LangChain for LLM-based processing

Google Generative AI via langchain_google_genai

Streamlit for UI

Pydantic for schema validation

Python 3.9+

## ⚙️ Setup Instructions
1. Clone the Repository

git clone https://github.com/your-username/OCR-Invoice-Extraction.git
cd OCR-Invoice-Extraction
2. Create & Activate a Virtual Environment (Optional)

conda create -n OCR_Project python=3.9
conda activate OCR_Project
3. Install Dependencies

pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the root directory and add your Google Generative AI API key:

GOOGLE_API_KEY=your_google_gemini_api_key_here
▶️ Running the App
Launch the Streamlit web app:

streamlit run app.py
Then open http://localhost:8501 in your browser.

## 🧠 How It Works
User uploads an invoice image.

The image is converted to base64.

LangChain sends a prompt with the image and an output schema to Google Generative AI.

The LLM extracts structured invoice data based on few-shot examples.

The output is returned as JSON and displayed in the UI.


