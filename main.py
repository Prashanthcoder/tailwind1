from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from clarifai.client.model import Model
from dotenv import load_dotenv
import os

# --- Load .env ---
load_dotenv()
CLARIFAI_PAT = os.getenv("CLARIFAI_PAT")
if not CLARIFAI_PAT:
    raise RuntimeError("⚠️ CLARIFAI_API_KEY not found in .env")

# --- FastAPI Setup ---
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# --- Clarifai Hosted Food Model (no deployment needed) ---
model = Model(
    "https://clarifai.com/clarifai/main/models/food-item-recognition",
    pat=CLARIFAI_PAT
)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = model.predict_by_bytes(contents, input_type="image")
        concepts = result.outputs[0].data.concepts

        if not concepts:
            return {
                "filename": file.filename,
                "size_kb": len(contents) // 1024,
                "prediction": None,
                "confidence": 0,
                "message": "No food detected in the image."
            }

        top = concepts[0]
        top_food = top.name
        top_conf = round(top.value, 3)

        if top_conf < 0.3:
            return {
                "filename": file.filename,
                "size_kb": len(contents) // 1024,
                "prediction": None,
                "confidence": top_conf,
                "message": "This image does not seem to contain food."
            }

        return {
            "filename": file.filename,
            "size_kb": len(contents) // 1024,
            "prediction": top_food,
            "confidence": top_conf,
            "message": f"Detected food: {top_food}"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Prediction failed: {str(e)}")
