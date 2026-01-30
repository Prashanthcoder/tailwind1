#  AI Nutritionist

![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
![Tech](https://img.shields.io/badge/stack-FastAPI%20%7C%20HTML%20%7C%20TailwindCSS-blue)

AI Nutritionist is a simple full‑stack web application that allows users to upload a food image and get an AI‑based prediction of what the food is, along with confidence information. It is designed as a clean, beginner‑friendly project that demonstrates frontend–backend integration with machine learning inference.

---

##  What the project does

* Provides a modern web UI to upload food images
* Sends images to a backend API for prediction
* Displays predicted food label and confidence score
* Shows image preview before upload
* Handles loading and error states gracefully

The frontend is built using **HTML + Tailwind CSS**, while the backend exposes a `/predict` API endpoint (implemented separately, typically using **FastAPI**).

---

##  Why this project is useful

* Great learning reference for **full‑stack ML projects**
* Demonstrates **image upload handling** using `FormData`
* Shows clean **frontend–backend communication** via `fetch`
* Minimal and readable codebase, easy to extend
* Ideal starting point for projects like:

  * AI Nutrition Tracker
  * MyFitnessPal‑style apps
  * Food calorie estimation systems

---

## Tech Stack

### Frontend

* HTML5
* Tailwind CSS
* Vanilla JavaScript

### Backend

* FastAPI
* Uvicorn
* python-multipart
* python-dotenv
* Clarifai Python SDK

### ML / AI

* Clarifai Hosted Food Item Recognition Model

---

## How to get started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-nutritionist.git
cd ai-nutritionist
```

### 2. Backend setup

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install fastapi uvicorn python-multipart clarifai python-dotenv
```

Create a `.env` file in the backend root:

```env
CLARIFAI_PAT=your_clarifai_personal_access_token
```

Run the backend server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

### 3. Frontend setup

Open `index.html` directly in a browser or serve it locally:

```bash
python -m http.server 8000
```

Then open:

```
http://localhost:8000
```

### 4. Configure API endpoint

Ensure the frontend points to the correct backend URL:

```js
fetch("http://127.0.0.1:8000/predict", {
  method: "POST",
  body: formData
});
```

---

## Example API Response

```json
{
  "message": "Prediction successful",
  "prediction": "Pizza",
  "confidence": 0.92,
  "filename": "food.jpg",
  "size_kb": 245
}
```

---

## Where to get help

* Open an issue in the GitHub repository
* Check backend API implementation (FastAPI docs)
* Refer to Tailwind CSS documentation for UI customization

Useful links:

* [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
* [https://tailwindcss.com/docs](https://tailwindcss.com/docs)

---

## Contributing

Contributions are welcome! 🎉

Please read the contribution guidelines before submitting a PR:

* [`CONTRIBUTING.md`](docs/CONTRIBUTING.md)

You can help by:

* Improving UI/UX
* Adding calorie or nutrition estimation
* Enhancing ML model accuracy
* Writing tests or documentation

---

## Maintainer

**Prashanth T**
Computer Science Engineering student
Passionate about AI, ML, and full‑stack development

---

## Roadmap

* Food calorie estimation
* Portion size estimation
* Nutrition breakdown (macros)
* User authentication
* Daily nutrition tracking dashboard
* Progressive Web App support

---

If you find this project useful, consider starring the repository.
