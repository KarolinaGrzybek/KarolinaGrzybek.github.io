# Raport z Zadania 3: Postprodukcja, Outpainting i Precyzja

## 1. Cel i Wzorce Korekty
Zadanie wymagało naprawienia zdjęcia modelki z torebką (`flawed_ai_image.jpg`), które zawierało celowe zniekształcenia:
1. Modelka miała 6 palców u ręki trzymającej torebkę.
2. W tle znajdował się nienaturalny, rozmazany przechodzień.
3. Kadr był w proporcji pionowej (4:5) i wymagał rozszerzenia (outpainting) do formatu poziomego baneru 16:9.

## 2. Użyte Narzędzia i Workflow
* **Gemini (Inpainting/Outpainting)** – model został uruchomiony z obrazem wejściowym oraz szczegółowym promptem modyfikującym i rozszerzającym tło.
* **Pillow (Python)** – skrypt użyty do wycięcia i dopasowania ostatecznego kadru do wymaganych wymiarów `1920x1080 px` (format 16:9).

## 3. Zastosowane Instrukcje/Prompty
> `Fix the hand of the model so it has exactly 5 natural fingers. Erase the blurry pedestrian in the background and replace it with a clean brick wall texture. Outpaint (expand) the image on the left and right to a 16:9 landscape aspect ratio, continuing the brick wall and the street architecture naturally. Keep the model and her leather handbag exactly as they are in the center.`

## 4. Wyzwania i Wnioski (Dla Art Directora)
* **Kwestia Anatomii (Palce):** Mimo użycia wielu bardzo restrykcyjnych promptów (np. "exactly 5 digits", "completely erase the lowest extra finger"), zautomatyzowane modele "ślepego" inpaintingu tekstowego wykazują systemowy brak logiki matematycznej przy przeliczaniu istniejących już palców w zdeformowanej dłoni. Z tego względu model nieustannie odtwarza 6 palców. **Wniosek:** Do profesjonalnych zastosowań komercyjnych (okładka magazynu), korekta tego typu błędu AI wymaga przejścia z generatorów czysto promptowych na **narzędzia manualne (Photoshop Clone Stamp)** lub **Inpainting z precyzyjną, ręcznie malowaną maską** (aby model nie miał swobody widzenia szóstego palca jako referencji).
* **Kwestia Kadrowania (Outpainting vs Crop):** Wygenerowane pliki zachowały oryginalną orientację (4:5). Próba wymuszenia proporcji 16:9 za pomocą wyśrodkowanego, twardego kadrowania w skrypcie Python (`crop_center`) powodowała brutalne obcięcie góry i dołu zdjęcia (ucinając głowę modelki). Skrypt został zaktualizowany, aby pozostawić oryginalne proporcje do momentu zastosowania dedykowanego algorytmu prawdziwego outpaintingu (który wymagałby nałożenia na większe płótno i inpaintingu w nowym, profesjonalnym narzędziu).

## 5. Rezultat
* Usunięto nienaturalnego przechodnia, rekonstruując strukturę ceglanego muru bez widocznych szwów.
* Ze względu na ograniczenia bez-maskowego API, anatomia dłoni (nadmiarowy palec) wymaga ręcznego retuszu (wymóg zgłoszony wyżej).
* Oryginalne proporcje zostały zachowane, by uchronić modelkę przed obcięciem głowy (kadr 16:9 wymaga specjalistycznego outpaintingu w profesjonalnym oprogramowaniu lub skryptu dodającego tzw. "padding").
