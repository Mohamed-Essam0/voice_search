from fastapi import FastAPI, UploadFile, File
import whisper
import tempfile

app = FastAPI()

# Load the Whisper base model (use 'tiny' if you want faster response)
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Transcribe
    result = model.transcribe(tmp_path)

    return {"text": result["text"]}