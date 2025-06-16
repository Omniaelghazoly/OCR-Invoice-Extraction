import streamlit as st
from PIL import Image
import os
import base64
from ocr import get_invoice_data  # Make sure this path is correct

st.set_page_config(page_title="Invoice App", layout="centered")
st.title("📄 Basic Invoice Upload App")

st.write("👋 Hello! Upload an invoice image to extract data from it.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Save the image to a local folder
    save_path = os.path.join("uploaded_image", uploaded_file.name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    image.save(save_path)
    st.success(f"✅ Image uploaded and saved to: `{save_path}`")

    # Run invoice extraction
    with st.spinner("🔍 Extracting data from the invoice..."):
        try:
            result = get_invoice_data(save_path)
            st.success("✅ Invoice data extracted successfully!")

            st.subheader("📋 Extracted Invoice Data:")
            st.json(result)

        except Exception as e:
            st.error(f"❌ Failed to extract data: {e}")

else:
    st.info("Please upload an image to continue.")
