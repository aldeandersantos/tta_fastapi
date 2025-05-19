from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid
import os
import asyncio
import edge_tts

app = FastAPI()

OUTPUT_DIR = "audios"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Liste algumas vozes brasileiras para o usuário escolher
PRESET_VOICES = {
    "feminina_1": "pt-BR-ThalitaMultilingualNeural",
    "feminina_2": "pt-BR-FranciscaNeural",
    "masculina_1": "pt-BR-AntonioNeural",
}

class TTSRequest(BaseModel):
    text: str
    voice: str = "feminina_2"  # valor padrão

@app.post("/tts/")
async def text_to_speech(payload: TTSRequest):
    audio_id = str(uuid.uuid4())
    name = payload.text[0:10].replace(" ", "_").replace(".", "_")
    mp3_path = os.path.join(OUTPUT_DIR, f"{name}.mp3")

    # Seleciona a voz
    voice = PRESET_VOICES.get(payload.voice, PRESET_VOICES["feminina_2"])

    # Gera o áudio async
    communicate = edge_tts.Communicate(payload.text, voice)
    await communicate.save(mp3_path)

    return JSONResponse({
        "message": "Áudio gerado com sucesso.",
        "mp3_file": mp3_path,
        "voz_utilizada": voice,
        "vozes_disponiveis": list(PRESET_VOICES.keys())
    })