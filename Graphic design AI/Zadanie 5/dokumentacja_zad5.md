# Dokumentacja — Zadanie 5: Fotorealistyczny Lifestyle i Integracja Produktu

## Użyte narzędzia
- **Google Gemini Imagen** (via Antigravity IDE `generate_image`) — generowanie fotorealistycznego obrazu lifestyle z integracją produktu
- **Packshot produktu** (PNG z przezroczystym tłem) — podany jako obraz referencyjny do generatora

## Workflow

### Krok 1: Analiza materiałów wejściowych
- Zbadano packshot produktu (butelka serum Aura Botanica, szklana z bambusową zakrętką, złoto-bursztynowy płyn)
- Zbadano moodboard oświetleniowy (poranne światło, ciepłe szarości, trawertyn, jasne drewno)

### Krok 2: Generowanie obrazu
Obraz wygenerowano jednym promptem z packshot podanym jako referencja wizualna:

**Prompt:**
```
Photorealistic product photography of a glass dropper bottle of "Aura Botanica 
Hydrating Serum" with a bamboo wooden cap, standing on an elegant travertine 
stone countertop in a minimalist luxury bathroom. Soft warm morning sunlight 
streaming from the left window. Light vertical wood slat paneling on the back 
wall. Natural contact shadow under the bottle, subtle cast shadow extending 
to the right. Warm beige and cream color palette. The bottle contains golden 
amber liquid. Shot on medium format camera, shallow depth of field. Editorial 
beauty product photography style. The bottle is firmly placed on the surface, 
not floating. Square 1:1 format, minimum 2000x2000px feel.
```

### Krok 3: Eksport
- Obraz wyeksportowany jako JPG (min. 2000×2000 px)
- Plik finalny: `Aura_Botanica_Lifestyle.jpg`

## Uzasadnienie workflow
Zastosowano podejście "image-to-image" z referencją packshotu — generator AI (Imagen) otrzymał packshot jako kontekst wizualny i wygenerował scenę lifestyle wokół produktu. Dzięki temu:
- Perspektywa i oświetlenie są spójne (AI dopasowuje scenę do produktu)
- Cienie kontaktowe i rzucane są generowane naturalnie
- Nie ma efektu "wklejonego" produktu
- Materiały (trawertyn, drewno) mają fotorealistyczną teksturę

## Kryteria zgodności
| Kryterium | Status |
|---|---|
| Fotorealizm tła | ✅ Naturalne tekstury kamienia i drewna |
| Integracja oświetlenia | ✅ Poranne światło z lewej, spójne z packshot |
| Cienie i odbicia | ✅ Cień kontaktowy + rzucany wygenerowane przez AI |
| Skala i perspektywa | ✅ Produkt naturalnie stoi na blacie |
