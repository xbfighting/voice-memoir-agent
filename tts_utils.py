import pyttsx3
import os
import tempfile
import wave


def synthesize_voice(text, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "reply.wav")
    engine = pyttsx3.init()
    # 保存到临时 wav 文件
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tf:
        temp_wav = tf.name
    engine.save_to_file(text, temp_wav)
    engine.runAndWait()
    # pyttsx3 生成的 wav 可能有兼容性问题，重新写一遍标准 wav
    with wave.open(temp_wav, 'rb') as src:
        params = src.getparams()
        audio_data = src.readframes(params.nframes)
    with wave.open(output_path, 'wb') as dst:
        dst.setparams(params)
        dst.writeframes(audio_data)
    os.remove(temp_wav)
    return output_path
