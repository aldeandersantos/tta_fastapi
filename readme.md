# 🗣️ Text to Audio FastAPI

Este projeto é uma API simples para converter textos em áudio (TTS) usando FastAPI e vozes brasileiras da Microsoft Edge TTS.  
Ideal para gerar áudios em português brasileiro de forma rápida e fácil! 🇧🇷🔊

## 🚀 Como usar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute o servidor:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Faça uma requisição POST para `/tts/`**  
   Envie um JSON como este:
   ```json
   {
     "text": "Olá, mundo!",
     "voice": "feminina_2"
   }
   ```

## 🎤 Vozes disponíveis

- feminina_1
- feminina_2 (padrão)
- masculina_1

## 📂 Saída

Os arquivos MP3 gerados ficam na pasta `audios/`.

## 📝 Exemplo de resposta

```json
{
  "message": "Áudio gerado com sucesso.",
  "mp3_file": "audios/Olá,_mundo.mp3",
  "voz_utilizada": "pt-BR-FranciscaNeural",
  "vozes_disponiveis": ["feminina_1", "feminina_2", "masculina_1"]
}
```

---

Feito com FastAPI, gtts e edge-tts.  
Contribuições são bem-vindas! ✨