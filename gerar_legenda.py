import whisper
import moviepy.editor as mp
import os

def extrair_audio(video_path, audio_path="audio_temp.wav"):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return audio_path

def traduzir_legenda(video_path, modelo="small"):
    print("Extraindo áudio do vídeo...")
    audio_path = extrair_audio(video_path)

    print("Carregando modelo Whisper...")
    model = whisper.load_model(modelo)

    print("Traduzindo áudio...")
    resultado = model.transcribe(audio_path, task="translate", fp16=False)

    srt_path = video_path.rsplit(".", 1)[0] + "_traduzido.srt"
    print(f"Salvando legenda traduzida em {srt_path}...")
    
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, segmento in enumerate(resultado["segments"]):
            start = formatar_tempo(segmento["start"])
            end = formatar_tempo(segmento["end"])
            texto = segmento["text"].strip()

            f.write(f"{i+1}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{texto}\n\n")
    
    print("Legenda traduzida criada com sucesso!")
    os.remove(audio_path)

def formatar_tempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos_restantes = int(segundos % 60)
    milissegundos = int((segundos - int(segundos)) * 1000)
    return f"{horas:02}:{minutos:02}:{segundos_restantes:02},{milissegundos:03}"

if __name__ == "__main__":
    caminho_video = input("Digite o caminho do vídeo: ")
    traduzir_legenda(caminho_video)
