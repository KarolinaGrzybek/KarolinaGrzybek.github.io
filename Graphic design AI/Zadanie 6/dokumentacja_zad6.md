# Dokumentacja — Zadanie 6: Spójność Wizualna Kampanii Wyprzedażowej

## Użyte narzędzia
- **Google Gemini Imagen** (via Antigravity IDE `generate_image`) — generowanie 3 fotorealistycznych grafik kampanijnych

## Workflow

### Krok 1: Analiza Brand Booka
- Dominujący kolor: pastelowy błękit `#D0E1FD`
- Kolor akcentowy: neonowy pomarańcz `#FF5F1F`
- Format: 16:9 (1920×1080 px)
- Styl: editorial fashion, komercyjny, premium

### Krok 2: Technika zachowania spójności
Spójność wizualną zapewniono poprzez:
1. **Identyczne elementy promptu** — każdy z 3 promptów zawiera te same frazy kluczowe:
   - `Soft pastel blue (#D0E1FD) studio background`
   - `Neon orange (#FF5F1F) accent lighting`
   - `Consistent soft diffused studio lighting`
   - `Horizontal 16:9 landscape format 1920x1080`
   - `Premium high-end [...] photography`
   - `Same lighting and color grading as a unified fashion campaign`
2. **Jedna sesja generowania** — wszystkie 3 obrazy wygenerowane w jednej serii, co minimalizuje zmienność stylu modelu AI

### Krok 3: Generowanie — 3 prompty

**Banner 1 — Modelka w okularach przeciwsłonecznych:**
```
Fashion editorial photograph, young confident woman wearing large trendy 
oversized sunglasses, positioned on the right side of frame. Large empty 
pastel blue (#D0E1FD) negative space on the left for text overlay. Soft 
pastel blue studio background. Subtle neon orange (#FF5F1F) rim lighting 
on model's face and hair. Professional beauty campaign photography, clean 
commercial look, summer vibes. Horizontal 16:9 landscape format 1920x1080. 
Consistent soft diffused studio lighting. Premium high-end fashion aesthetic. 
Model wearing a light summer outfit.
```

**Banner 2 — Torba plażowa:**
```
Professional product photography of a stylish woven straw summer beach 
tote bag with leather handles, positioned on the left side of frame. 
Large empty pastel blue (#D0E1FD) negative space on the right for text 
overlay. Soft pastel blue studio background. Subtle neon orange (#FF5F1F) 
accent lighting. Fashion accessories e-commerce campaign style, clean 
modern composition. Horizontal 16:9 landscape format 1920x1080. Consistent 
soft diffused studio lighting matching a cohesive summer fashion campaign. 
Premium high-end aesthetic. Same lighting and color grading as a unified 
photo series.
```

**Banner 3 — Letnie buty:**
```
Fashion editorial photograph of stylish summer canvas espadrille shoes 
on a male model's feet and lower legs, positioned at the bottom of the 
frame. Large empty pastel blue (#D0E1FD) negative space at the top for 
text overlay. Soft pastel blue studio background. Neon orange (#FF5F1F) 
accent lighting and subtle orange color highlights on shoes. Summer fashion 
campaign aesthetic. Horizontal 16:9 landscape format 1920x1080. Consistent 
soft diffused studio lighting. Premium high-end commercial photography. 
Same lighting and color grading as a unified fashion campaign photo series.
```

### Krok 4: Eksport
- 3 pliki JPG w rozdzielczości 1920×1080 (16:9)
- `banner_sunglasses.jpg`, `banner_bag.jpg`, `banner_shoes.jpg`

## Technika spójności — podsumowanie
| Element | Jak zapewniono spójność |
|---|---|
| Kolory | Identyczne kody HEX w każdym prompcie (#D0E1FD, #FF5F1F) |
| Oświetlenie | Fraza "consistent soft diffused studio lighting" w każdym |
| Styl | "Premium high-end [...] photography" + "unified campaign" |
| Format | "Horizontal 16:9 landscape format 1920x1080" |
| Negative space | Różne położenie (lewo/prawo/góra) ale ten sam koncept |
| Grading | "Same lighting and color grading as a unified photo series" |
