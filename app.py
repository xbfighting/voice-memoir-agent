from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from whisper_utils import transcribe_audio
from gpt_utils import generate_reply
from tts_utils import synthesize_voice
from memory_faiss import add_to_memory, query_memory
import os
import uuid

app = FastAPI()

UPLOAD_DIR = "uploads"
AUDIO_REPLY_DIR = "audio_reply"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(AUDIO_REPLY_DIR, exist_ok=True)

@app.post("/memoir")
async def handle_audio(file: UploadFile = File(...)):
    audio_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.mp3")
    with open(audio_path, "wb") as f:
        f.write(await file.read())

    text = transcribe_audio(audio_path)
    add_to_memory(text)
    context = query_memory(text)
    reply = generate_reply(text, context)
    audio_output_path = synthesize_voice(reply, AUDIO_REPLY_DIR)
    return FileResponse(audio_output_path, media_type="audio/wav")