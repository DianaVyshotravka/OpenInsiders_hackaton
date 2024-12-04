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

## Usage Example
- **http://127.0.0.1:8000/docs:**
    -  After using the link, you will be addressed to such page:
![зображення](https://github.com/user-attachments/assets/3838d343-9dbd-4aca-b743-9fad6b2b491b)
    -  Click "Try it out" and enter your string that is to be classified:
![зображення](https://github.com/user-attachments/assets/19ed8bb4-98fc-4768-8c90-8a5155dbd132)
    -  Click "Execute" and check results:
![зображення](https://github.com/user-attachments/assets/03f828a2-18f3-4e97-a15d-ba607f73b3f1)

- **http://127.0.0.1:8000/static/index.html:**
    -  After using the link, you will be addressed to such page:
![зображення](https://github.com/user-attachments/assets/3c1bc084-eb8e-4775-931e-f2ecf4586dbe)
    -  Enter your string that is to be classified:
![зображення](https://github.com/user-attachments/assets/e7da0602-abdc-4c08-9587-e39510b9f5fa)
    -  Click "Classify" and check results:
![зображення](https://github.com/user-attachments/assets/b5fdc3fe-9221-4ef7-b951-bf79d328aab2)

