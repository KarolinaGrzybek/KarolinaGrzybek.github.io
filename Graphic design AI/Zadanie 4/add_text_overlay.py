import os
import subprocess
import sys

def install_dependencies():
    print("Sprawdzanie i instalowanie wymaganych bibliotek Pythona...")
    try:
        import cv2
        from PIL import Image, ImageDraw, ImageFont
        import numpy
    except ImportError:
        print("Brak wymaganych bibliotek. Instalowanie opencv-python oraz Pillow...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python", "Pillow", "numpy"])
        print("Instalacja zakończona pomyślnie!\n")

# Uruchom instalację zależności
install_dependencies()

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def process_video(input_video_path, output_video_path, text):
    if not os.path.exists(input_video_path):
        print(f"Błąd: Plik wejściowy {input_video_path} nie istnieje!")
        print("Upewnij się, że wygenerowane wideo zostało zapisane w tym folderze pod nazwą Zad_4_Surowe.mp4")
        return False

    print(f"Rozpoczynanie przetwarzania wideo: {input_video_path}...")
    
    cap = cv2.VideoCapture(input_video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if fps == 0 or total_frames == 0:
        fps = 30
        
    print(f"Format wideo: {width}x{height} px, FPS: {fps:.2f}, Klatek: {total_frames}")

    # Użycie kodeka mp4v dla stabilności na Windows
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    temp_output = "temp_text_video.mp4"
    out = cv2.VideoWriter(temp_output, fourcc, fps, (width, height))

    # Wybór czcionki systemowej (Montserrat, Arial lub inna bezszeryfowa)
    font_names = [
        "Montserrat-Bold.ttf", "Montserrat-Regular.ttf",
        "HelveticaNeue-Bold.ttf", "Helvetica.ttf", 
        "arialbd.ttf", "arial.ttf"
    ]
    
    font_path = None
    # Próba znalezienia czcionki lokalnie lub w Windows Fonts
    windows_fonts_dir = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
    
    # Szukamy czcionki w katalogu Windows/Fonts oraz lokalnie
    for font_name in font_names:
        full_path = os.path.join(windows_fonts_dir, font_name)
        if os.path.exists(full_path):
            font_path = full_path
            break
        elif os.path.exists(font_name):
            font_path = font_name
            break

    # Dostosowanie rozmiaru czcionki do rozdzielczości pionowej
    # Dla 1080x1920 optymalny rozmiar to około 60-70px
    font_size = int(width * 0.06) 
    print(f"Użyta czcionka: {os.path.basename(font_path) if font_path else 'Domyślna Pillow'}")
    print(f"Rozmiar czcionki: {font_size}px")

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Konwersja klatki do formatu PIL (RGB)
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(image)

        # Wczytanie czcionki
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default()

        # Obliczenie rozmiaru tekstu w celu wyśrodkowania go w poziomie
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]
        except AttributeError:
            text_w, text_h = draw.textsize(text, font=font)

        # Ustawienie napisu w dolnej 1/4 ekranu (np. na 83% wysokości)
        x = (width - text_w) // 2
        y = int(height * 0.83) - text_h // 2

        # 1. Rysowanie cienia (drop shadow) dla czytelności na jasnym tle
        shadow_offset = max(2, int(width * 0.003))
        # Rysujemy delikatne przesunięcie w dół i w prawo w kolorze czarnym z lekką przezroczystością
        draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=(0, 0, 0, 180))

        # 2. Rysowanie tekstu głównego (biały)
        draw.text((x, y), text, font=font, fill=(255, 255, 255))

        # Konwersja z powrotem na BGR i zapis klatki
        processed_frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        out.write(processed_frame)
        
        frame_count += 1
        if frame_count % 30 == 0 or frame_count == total_frames:
            print(f"Przetworzono klatki: {frame_count}/{total_frames} ({(frame_count/total_frames)*100:.1f}%)")

    cap.release()
    out.release()
    print("Nakładanie tekstu zakończone!")
    return temp_output

def combine_audio(video_with_text, audio_path, final_output):
    if not os.path.exists(audio_path):
        print(f"\nUwaga: Nie znaleziono pliku audio: {audio_path}")
        print("Zapisano wideo z samym tekstem pod nazwą: Zad_4_Gotowe_BezDźwięku.mp4")
        if os.path.exists(video_with_text):
            os.rename(video_with_text, "Zad_4_Gotowe_BezDźwięku.mp4")
        return False

    print("\nŁączenie wideo z podkładem muzycznym za pomocą ffmpeg...")
    
    # Wywołanie ffmpeg w celu połączenia audio i wideo
    # -y (nadpisz), -i (wideo), -i (audio), -shortest (przytnij do krótszego z plików)
    cmd = [
        'ffmpeg', '-y',
        '-i', video_with_text,
        '-i', audio_path,
        '-c:v', 'libx264',    # Konwersja na standardowy H.264
        '-pix_fmt', 'yuv420p', # Zgodność z odtwarzaczami mobilnymi
        '-c:a', 'aac',
        '-map', '0:v:0',
        '-map', '1:a:0',
        '-shortest',          # Skrócenie do długości wideo
        final_output
    ]
    
    try:
        # Sprawdzamy czy ffmpeg jest dostępny
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Sukces! Gotowy plik wyeksportowany do: {final_output}")
        # Sprzątanie tymczasowego pliku
        if os.path.exists(video_with_text):
            os.remove(video_with_text)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nBrak globalnego ffmpeg w systemie. Próba użycia biblioteki moviepy jako fallback...")
        try:
            # Automatyczna próba instalacji moviepy, jeśli nie jest dostępny
            try:
                try:
                    # Spróbujmy najpierw dla moviepy v2.0+
                    from moviepy.video.io.VideoFileClip import VideoFileClip
                    from moviepy.audio.io.AudioFileClip import AudioFileClip
                except ImportError:
                    # Jeśli nie zadziała, to dla starszych wersji v1.x
                    from moviepy.editor import VideoFileClip, AudioFileClip
            except ImportError:
                print("Instalowanie moviepy w celu automatycznego połączenia dźwięku...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", "moviepy"])
                try:
                    from moviepy.video.io.VideoFileClip import VideoFileClip
                    from moviepy.audio.io.AudioFileClip import AudioFileClip
                except ImportError:
                    from moviepy.editor import VideoFileClip, AudioFileClip

            print("Łączenie audio i wideo przy użyciu moviepy...")
            video_clip = VideoFileClip(video_with_text)
            audio_clip = AudioFileClip(audio_path)
            
            # Przycinanie długości audio do długości wideo (obsługa moviepy v1 i v2)
            if hasattr(audio_clip, "with_duration"):
                audio_clip = audio_clip.with_duration(video_clip.duration)
            else:
                audio_clip = audio_clip.set_duration(video_clip.duration)
            
            # Łączenie wideo z przyciętym dźwiękiem (obsługa moviepy v1 i v2)
            if hasattr(video_clip, "with_audio"):
                final_clip = video_clip.with_audio(audio_clip)
            else:
                final_clip = video_clip.set_audio(audio_clip)
            
            # Zapis pliku wynikowego
            final_clip.write_videofile(
                final_output, 
                codec='libx264', 
                audio_codec='aac'
            )
            
            # Zamknięcie plików w celu zwolnienia pamięci i odblokowania plików na dysku
            video_clip.close()
            audio_clip.close()
            final_clip.close()
            
            print(f"Sukces! Gotowy plik wyeksportowany przez moviepy do: {final_output}")
            if os.path.exists(video_with_text):
                os.remove(video_with_text)
            return True
            
        except Exception as e:
            print(f"\nBłąd podczas próby łączenia przez moviepy: {e}")
            # Zamykamy otwarte klipy, aby odblokować plik temp_text_video.mp4 na dysku
            try:
                video_clip.close()
            except:
                pass
            try:
                audio_clip.close()
            except:
                pass
                
            backup_name = "Zad_4_Gotowe_WideoBezAudio.mp4"
            print(f"Wideo z nałożonym tekstem zostało zapisane jako: {backup_name}")
            if os.path.exists(video_with_text):
                if os.path.exists(backup_name):
                    try:
                        os.remove(backup_name)
                    except Exception as remove_err:
                        print(f"Nie udało się usunąć istniejącego pliku backupu: {remove_err}")
                try:
                    os.rename(video_with_text, backup_name)
                except Exception as rename_err:
                    print(f"Nie udało się zmienić nazwy pliku tymczasowego: {rename_err}")
            return False

if __name__ == "__main__":
    video_in = "Zad_4_Surowe.mp4"
    audio_in = "Zad_4_Audio.mp3"
    video_out = "Zad_4_Gotowe.mp4"
    text_to_overlay = "SUMMER COLLECTION '26"
    
    temp_vid = process_video(video_in, video_out, text_to_overlay)
    if temp_vid:
        combine_audio(temp_vid, audio_in, video_out)
        print("\nZadanie zakończone!")
