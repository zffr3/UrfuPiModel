from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image

import io
import streamlit as st

def open_image():
    uploadFile = st.file_uploader(label="Load file")

    if uploadFile is not None:
        imageData = uploadFile.getvalue()
        st.image(imageData)
        return Image.open(io.BytesIO(imageData))
    else:
        return None

img = open_image()
if img is not None:
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
    inputs = processor(images=img, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits

    predicted_class_idx = logits.argmax(-1).item()
    out = model.config.id2label[predicted_class_idx]
    st.text(out)