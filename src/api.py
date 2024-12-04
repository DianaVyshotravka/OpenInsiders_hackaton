import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import load_model
import openpyxl
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from pydantic import BaseModel
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel

model = load_model("model.h5")

# Load the pre-trained tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
bert_model = AutoModel.from_pretrained("DeepPavlov/rubert-base-cased")

# Define unique labels
unique_labels = ['Заперечення', 'Виправдовування', 'Заклик', 
                 'Розпалювання ворожнечі та ненависті', 
                 'Приниження національної честі та гідності', 
                 'Просто текст']

label_to_id = {label: idx for idx, label in enumerate(unique_labels)}
id_to_label = {idx: label for label, idx in label_to_id.items()}

# Initialize FastAPI app
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
# Request schema
class SentenceInput(BaseModel):
    text: str

def preprocess_text(text):
    import spacy  # Ensure spaCy is installed and the language model is loaded
    nlp = spacy.load("en_core_web_sm")  # Adjust to your language model
    doc = nlp(str(text).lower()) 
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def get_avg_w2v(text, tokenizer, bert_model):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    vector = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return vector

@app.post("/classify/")
def classify_sentence(sentence: SentenceInput):
    # Preprocess the input sentence
    processed_text = preprocess_text(sentence.text)
    
    # Convert the processed text to a vector (наприклад, Word2Vec або будь-який інший)
    vector = get_avg_w2v(processed_text, tokenizer, bert_model)
    
    vector = vector[:767]

    # Передбачення ймовірностей
    probabilities = model.predict(np.array([vector]))

    # Нормалізовані ймовірності (якщо необхідно)
    probabilities_dict = {
        id_to_label[i]: float(probabilities[0][i]) for i in range(len(probabilities[0]))
    }

    # Найвірогідніший клас
    predicted_label = id_to_label[np.argmax(probabilities)]

    return {
        "text": sentence.text,
        "processed_text": processed_text,
        "label": predicted_label,
        "probabilities": probabilities_dict,
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the NLP classification API. Use /docs for API documentation."}
