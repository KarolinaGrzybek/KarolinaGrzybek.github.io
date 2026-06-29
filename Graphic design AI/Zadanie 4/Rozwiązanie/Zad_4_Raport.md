# Raport: Zadanie 4 – Wideo Generatywne i Dźwięk

To zadanie skupia się na stworzeniu pionowego, fotorealistycznego wideo reklamowego (9:16) promującego letnią kolekcję oraz spójnego, energetycznego podkładu muzycznego z minimalistyczną nakładką tekstową.

---

## 1. Wygenerowane Zdjęcia Referencyjne (Klatki Bazowe)

W celu ułatwienia procesu generacji wideo AI (metodą **Image-to-Video** z użyciem klatki początkowej i końcowej, co daje najwyższą kontrolę nad spójnością postaci i tłem), wygenerowaliśmy pary wysokiej jakości klatek referencyjnych (9:16).

Możesz ich użyć jako obrazów wejściowych **First Frame** (klatka startowa) oraz **End Frame / Last Frame** (klatka końcowa) w takich narzędziach jak **Kling AI**, **Luma Dream Machine** czy **Runway Gen-3 Alpha**:

* **Scenariusz A (Szeroki kadr z płynnym najazdem do zbliżenia):**
  * **Klatka Startowa:** [Zad_4_Ref_1.png](Zad_4_Ref_1.png) – Szerszy kadr kinowy z piękną, brukowaną włoską uliczką i słoneczną atmosferą.
  * **Klatka Końcowa:** [Zad_4_Ref_1_End.png](Zad_4_Ref_1_End.png) – Bliskie ujęcie (close-up) tej samej uśmiechniętej dziewczyny z głębią ostrości (bokeh) w tle tej samej uliczki.
* **Scenariusz B (Średnie ujęcie z odwróceniem się i odejściem):**
  * **Klatka Startowa:** [Zad_4_Ref_2.png](Zad_4_Ref_2.png) – Portret dziewczyny idącej pod słońce (backlight) z wiatrem we włosach.
  * **Klatka Końcowa:** [Zad_4_Ref_2_End.png](Zad_4_Ref_2_End.png) – Dziewczyna odwraca się lekko przez ramię, odchodząc w głąb uliczki (ujęcie od tyłu/z boku).

*(Wszystkie pliki graficzne zostały zapisane bezpośrednio w tym katalogu).*

---

## 2. Zestaw Promptów do Realizacji (Zoptymalizowany pod kątem Detali Kolekcji i Akcesoriów)

Poniższe prompty zostały zoptymalizowane pod kątem fotorealizmu, kinowej jakości oraz stabilności fizyki w ruchu, ze szczególnym naciskiem na **elementy letniej kolekcji: dodatki, akcesoria oraz fakturę materiałów**.

### A. Prompty do generowania obrazów bazowych (Midjourney v6 / Flux)
Jeśli chcesz wygenerować własne klatki początkowe lub końcowe w Midjourney:

* **SCENARIUSZ A (Szeroki kadr z najazdem – Skupienie na sylwetce i torebce):**
  * **Klatka Startowa A:**
    > `A highly photorealistic, cinematic vertical 9:16 fashion shot of a beautiful young woman walking confidently down a sunny, narrow cobblestone street in a picturesque Italian coastal town. She is wearing a light, flowing white linen summer dress that catches the breeze, and carrying a stylish woven straw beach bag. Large designer sunglasses, warm golden hour sunlight, soft lens flare, deep depth of field, shot on 35mm lens, 8k resolution, realistic linen fabric texture, fashion editorial style --ar 9:16 --style raw --v 6.0`
  * **Klatka Końcowa A:**
    > `A highly photorealistic, cinematic vertical 9:16 fashion close-up shot of the same beautiful young woman with detailed facial features, smiling gently. Soft golden hour lens flare, picturesque Italian coastal town street blurred in the background (bokeh), warm sunset light, close-up focusing on her face, designer sunglasses, and fine gold earrings, shot on 85mm lens, natural skin texture, fashion editorial style --ar 9:16 --style raw --v 6.0`

* **SCENARIUSZ B (Średnie ujęcie z odwróceniem – Skupienie na biżuterii i ruchu sukienki):**
  * **Klatka Startowa B:**
    > `A highly photorealistic, cinematic vertical 9:16 portrait of a smiling young woman in a white linen dress walking down a sunny cobblestone street. She is wearing delicate gold necklaces and bracelets that shimmer in the sun. Sunny backlighting, golden hour glow, breeze moving her hair and dress, 50mm lens look, elegant and stylish, photorealistic skin pores and details --ar 9:16 --style raw --v 6.0`
  * **Klatka Końcowa B:**
    > `A highly photorealistic, cinematic vertical 9:16 shot of the same young woman in a white linen dress walking away, looking back over her shoulder with a subtle smile. Showing the detailed back design of the linen dress, fine gold jewelry on her back and neck, flowing dress and wind-blown hair, shot on 35mm lens, deep depth of field, natural lighting --ar 9:16 --style raw --v 6.0`

* **SCENARIUSZ C (Mocne zbliżenie na detale – Skupienie na akcesoriach: kapelusz, okulary, biżuteria):**
  * **Klatka Startowa C:**
    > `A highly photorealistic, cinematic vertical 9:16 close-up fashion portrait of a stylish young woman wearing a chic wide-brimmed straw hat, elegant designer gold sunglasses, and fine gold jewelry. Warm golden hour sunlight reflecting off the lenses of her sunglasses. Detailed textures of linen shirt and straw hat, Italian coastal village in the blurred background, cinematic bokeh, 85mm lens --ar 9:16 --style raw --v 6.0`
  * **Klatka Końcowa C:**
    > `A highly photorealistic, cinematic vertical 9:16 medium close-up of the same young woman, smiling gently, adjusting the brim of her straw hat. Detailed shot of her hand (5 fingers, realistic nails), beautiful gold bracelets on her wrist, warm sunset backlight, lens flare, detailed linen dress texture, fashion editorial style --ar 9:16 --style raw --v 6.0`

### B. Prompty do ożywiania obrazu (Image-to-Video / Frame Interpolation)
Po wgraniu klatki startowej i końcowej w generatorze wideo (np. Kling, Luma, Runway), użyj następujących instrukcji ruchu:

* **Prompt ruchu (dla płynnego przejścia i stabilności):**
  > `Slow motion cinematic camera transition from the starting frame to the ending frame. Soft summer breeze gently blowing her hair, the fabric of her white dress, and the brim of her straw hat. Subtle waves in the background, light dust motes in the sunbeams, highly realistic movement, no morphing, consistent face and limbs, photorealistic skin, professional color grading.`

### C. Prompty do generowania podkładu muzycznego (Suno v4 / Udio)
Wgraj jeden z poniższych promptów do generatora audio, aby stworzyć spójną, powolną, śródziemnomorską ścieżkę dźwiękową idealnie pasującą do klimatu slow-motion we włoskim miasteczku:

* **Opcja 1: Tradycyjna, nostalgiczna i nastrojowa (Acoustic Folk / Gitara i Mandolina):**
  > `Slow acoustic mediterranean folk instrumental, solo nylon-string classical guitar, gentle mandolina tremolo, warm accordion pads, nostalgic cinematic italian romance vibe, slow tempo, relaxing, dolce vita, high quality recording`
* **Opcja 2: Nowoczesna, relaksująca i marzycielska (Mediterranean Chillout Lounge):**
  > `Slow tempo mediterranean lounge track, acoustic guitar, soft warm ambient synth pad, very slow gentle percussion, dreamy and relaxing holiday vibe, ambient chillout instrumental, no vocals, high quality`

---

## 3. Sugerowany Workflow Realizacji

1. **Wideo (Image-to-Video z klatką końcową):**
   * Wejdź na platformę **Kling AI**, **Luma Dream Machine** lub **Runway (Gen-3 Alpha)**.
   * Wgraj plik startowy (np. `Zad_4_Ref_1.png`) jako **First Frame** (klatkę startową).
   * Wgraj odpowiadający mu plik końcowy (np. `Zad_4_Ref_1_End.png`) jako **End Frame / Last Frame** (klatkę końcową).
   * Wpisz powyższy prompt ruchu (sekcja 2.B) i wygeneruj klip o długości 5-8 sekund. Narzędzie automatycznie dokona interpolacji ruchu i wygeneruje przejście z pierwszej klatki do drugiej.
   * Pobierz gotowe wideo i zapisz je w tym folderze pod nazwą **`Zad_4_Surowe.mp4`**.
 
2. **Dźwięk (Audio AI):**
   * Przejdź do **Suno.com** lub **Udio.com**.
   * Wygeneruj krótki (np. 10-15 sekundowy) podkład instrumentalny za pomocą promptu z sekcji 2.C.
   * Pobierz plik audio w formacie MP3 i zapisz go w tym folderze jako **`Zad_4_Audio.mp3`**.
 
3. **Montaż Końcowy (Wideo + Audio + Napis):**
   * Możesz zmontować wideo ręcznie w programie CapCut / Premiere Pro, nakładając napis `"SUMMER COLLECTION '26"` u dołu ekranu z czcionką Montserrat lub Helvetica.
   * **Alternatywnie:** Skorzystaj z przygotowanego automatycznego skryptu Python.

---

## 4. Automatyczny Montaż Skryptem Python

W folderze znajduje się gotowy skrypt [add_text_overlay.py](add_text_overlay.py). Automatycznie nałoży on napis ze stabilnym cieniem i połączy ścieżkę audio z wideo.

### Jak go uruchomić?
1. Zapisz swoje pliki w tym folderze jako:
   * `Zad_4_Surowe.mp4` (wideo)
   * `Zad_4_Audio.mp3` (dźwięk)
2. Uruchom terminal w tym folderze i wpisz:
   ```bash
   python add_text_overlay.py
   ```
3. Skrypt sam pobierze potrzebne zależności (`opencv-python`, `Pillow`) i wygeneruje finalny plik **`Zad_4_Gotowe.mp4`**.

*Uwaga: Do pełnego połączenia audio i wideo skrypt wymaga zainstalowanego w systemie narzędzia `ffmpeg`. Jeśli go nie masz, skrypt wygeneruje wideo z samym napisem, które możesz łatwo połączyć z dźwiękiem w dowolnej aplikacji.*
