from TTS.api import TTS
import os

tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")

def synthesize_voice(text, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "reply.wav")
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path