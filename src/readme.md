# Documentation for NLP Classification API

This API provides NLP classification capabilities for text, enabling users to classify sentences into predefined categories.

---

## Endpoints

### `/` (GET)
- **Description:** Base endpoint to verify if the API is running.
- **Response:**
  ```json
  {
      "message": "Welcome to the NLP classification API. Use /docs for API documentation."
  }
  ```

  
### `/classify/` (POST)
- **Description:** Classifies a given sentence into one of the predefined categories.
- **Request:**
  ```json
  {
      "text": "Your input sentence here"
  }
  ```
- **Response:**
  ```json
  {
      "text": "Your input sentence here",
      "processed_text": "Processed sentence after lemmatization",
      "label": "Predicted label",
      "probabilities": {
          "Заперечення": 0.25,
          "Виправдовування": 0.15,
          "Заклик": 0.10,
          ...
      }
  }
  ```

## User Interfaces
- **Interactive API Documentation**
Visit the /docs path (e.g., http://127.0.0.1:8000/docs) to test the endpoints manually via Swagger UI.

- **Website Usage**
Access the HTML-based interface at http://127.0.0.1:8000/static/index.html to classify text using a web form.

## Installation Commands
1. **Clone or download the repository**
   ```code
  git clone https://github.com/DianaVyshotravka/OpenInsiders_hackaton.git
   cd OpenInsiders_hackaton
   ```
2. **Install Python dependencies**
  ```code
  pip install fastapi uvicorn pandas scikit-learn tensorflow torch transformers numpy openpyxl spacy
  python -m spacy download ru_core_news_sm
  ```
3. **Run the API: Start the API server using**
  ```code
  uvicorn api:app --reload
  ```
4. **Access the API**
- Visit the Swagger docs: http://127.0.0.1:8000/docs
- Use the web interface: http://127.0.0.1:8000/static/index.html
