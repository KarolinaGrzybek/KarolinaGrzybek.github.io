# Raport z Zadania 2: Spójność Stylu (Skandynawska Jesień)

## 1. Metodologia Spójności (Consistency Workflow)
Do zachowania spójności serii 3 grafik promocyjnych zastosowano technikę precyzyjnego opisania elementów wspólnych (Shared Tokens) w promptach dla modelu Gemini. Elementy te to:
* **Paleta kolorów**: Ciepły beż (`#E6DACA`), szałwiowa zieleń (`#9CAE96`), zgaszona musztarda (`#D4AF37`) oraz ciemne orzechowe drewno (`#4A3B32`).
* **Styl oświetlenia**: Złota godzina (golden hour), jesienne popołudniowe słońce wpadające pod niskim kątem przez duże okna, tworzące długie i miękkie cienie.
* **Kompozycja**: Minimalistyczne, nowoczesne wnętrza skandynawskie, ujęcia o charakterze profesjonalnej fotografii wnętrzarskiej.

## 2. Użyte Prompty

### Salon (16:9)
> `Scandinavian modern living room interior banner, 16:9 aspect ratio landscape. Beautifully styled cozy room with dark walnut wood table and furniture, sage green (#9CAE96) cushions and accent wall, zgaszona musztarda (#D4AF37) knit throw blanket, warm oat beige (#E6DACA) sofa and walls. Warm golden hour autumn sunbeams pouring through large clean windows, creating long soft shadows on the floor. Minimalist design, photorealistic, 8k, professional interior photography, cozy scandinavian autumn theme, no text, clean space.`

### Sypialnia (1:1)
> `Scandinavian modern bedroom interior, square 1:1 aspect ratio. Cozy bed with warm oat beige (#E6DACA) linen sheets, dark walnut wood headboard and nightstand, sage green (#9CAE96) accent blanket, zgaszona musztarda (#D4AF37) accent pillow. Warm golden hour autumn sunbeams pouring through large clean windows, creating long soft shadows on the floor. Minimalist design, photorealistic, 8k, professional interior photography, cozy scandinavian autumn theme, no text, clean space.`

### Jadalnia (9:16)
> `Scandinavian modern dining room interior, vertical 9:16 aspect ratio. Walnut wood dining table and chairs, warm oat beige (#E6DACA) wall, sage green (#9CAE96) ceramic vase and table runner, zgaszona musztarda (#D4AF37) chair cushions and napkins. Warm golden hour autumn sunbeams pouring through large windows, creating long soft shadows on the dining table and floor. Minimalist design, photorealistic, 8k, professional interior photography, cozy scandinavian autumn theme, no text, clean space.`

## 3. Kadrowanie i Postprodukcja
Wygenerowane obrazy zostały przetworzone za pomocą skryptu Python (Pillow). Skrypt przeprowadził centrowanie i precyzyjne przycięcie obrazów do wymaganych pikseli:
* Salon: `1920x1080 px` (16:9)
* Sypialnia: `1080x1080 px` (1:1)
* Jadalnia: `1080x1920 px` (9:16)
Zapewnia to komercyjną przydatność banerów bez zniekształceń proporcji.
