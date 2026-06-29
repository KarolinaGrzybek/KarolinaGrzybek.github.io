# Raport z Zadania 1: Fotorealizm i Integracja Produktu (Packshot)

## 1. Wybrane Narzędzia
* **Gemini (Imagen 3)** – wbudowany silnik generowania obrazów platformy. Wybrany ze względu na doskonałe rozumienie kompozycji, realistyczne oddanie odbić świetlnych w szkle i naturalną fizykę cieniowania na marmurze.
* **Python (Pillow)** – skrypt użyty do wyodrębnienia oryginalnego produktu i przygotowania fizycznych warstw (background, product, shadow) w celach edycji.

## 2. Użyte Prompty (Tło i Integracja)
Do wygenerowania zintegrowanego packshotu z produktem użyto następującego promptu:
> `Luxury cosmetic product photography. Place the glass cream jar from the input image onto a white and grey marble countertop. In the background is clean water reflecting soft warm sunlight. Tropical palm leaves cast sharp shadows onto the marble. Warm golden hour summer glow lighting. Maintain the product jar's shape, color, label, and texture exactly. Realistic shadows and reflections of the jar on the marble surface. High-end, commercial style.`

Do wygenerowania czystego tła (dla struktury warstw):
> `Luxury cosmetics product photography background. A premium white and grey marble countertop, clean water surface with gentle ripples on the side reflecting soft warm sunlight, sharp and defined tropical palm leaf shadows cast across the marble surface, bright and warm sunbeams (summer glow), warm beige and gold color palette, extremely photorealistic, 8k resolution, detailed texture of marble, shallow depth of field, high-end commercial shot. No product in the scene, empty space in the middle for product placement.`

## 3. Uzasadnienie
Wybór Gemini do generowania tła i kompozycji wynika z jego unikalnej zdolności do zachowania detali obiektu referencyjnego (etykieta, kształt zakrętki) przy jednoczesnym generowaniu fizycznie poprawnych interakcji świetlnych. Imagen 3 precyzyjnie zaadaptował płaskie oświetlenie oryginalnego zdjęcia do ciepłego, kierunkowego światła "Summer Glow", generując spójne odbicie szklanego słoiczka na wypolerowanym marmurze oraz miękki cień, który idealnie stapia produkt z podłożem.
