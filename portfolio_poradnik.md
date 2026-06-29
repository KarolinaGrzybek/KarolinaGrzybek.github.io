# Poradnik: Jak spersonalizować i opublikować Twoje portfolio

Twój dysk zawiera gotowy, w pełni responsywny prototyp portfolio w folderze `portfolio`:
- [index.html](file:///c:/Users/karol/.gemini/antigravity/portfolio/index.html) - struktura strony i treści.
- [style.css](file:///c:/Users/karol/.gemini/antigravity/portfolio/style.css) - nowoczesny design (ciemny motyw neonowy).
- [script.js](file:///c:/Users/karol/.gemini/antigravity/portfolio/script.js) - obsługa interakcji (filtry, modalne okna, suwak porównania).

---

## 1. Jak podejrzeć stronę lokalnie?
Wystarczy wejść do folderu `portfolio` i dwukrotnie kliknąć w plik **[index.html](file:///c:/Users/karol/.gemini/antigravity/portfolio/index.html)**. Strona otworzy się w Twojej domyślnej przeglądarce. Będziesz mogła przetestować działanie przycisków, filtrów, formularza kontaktowego oraz interaktywnego suwaka w sekcji grafiki AI.

---

## 2. Jak spersonalizować treści?

Wszystkie treści są w pełni edytowalne w pliku `index.html`. Możesz go otworzyć w zwykłym notatniku lub edytorze kodu.

### A. Zdjęcie profilowe i CV
1. Kiedy przygotujesz swoje biznesowe zdjęcie profilowe, zapisz je w folderze `assets` pod nazwą `avatar.png` (zastępując obecny plik) lub zmień ścieżkę w `index.html` (linia `76`).
2. Zapisz swoje CV w formacie PDF (np. jako `CV_Karolina_Grzybek.pdf`) w głównym folderze, a następnie w `index.html` podepnij link do niego (np. w sekcji Kontakt).

### B. Dodawanie prawdziwych raportów Power BI
Obecne karty są przygotowane z makietami obrazkowymi. Kiedy będziesz mieć swoje raporty:
1. **Wersja statyczna (Zrzuty ekranu):** Zapisz zrzuty ekranu swoich raportów w folderze `assets` i zmień ścieżki w `index.html`.
2. **Wersja interaktywna (Live Embedded):** 
   - W Power BI Service przejdź do swojego raportu -> *Plik* -> *Osadź raport* -> *Opublikuj w sieci (publicznie)*.
   - Skopiuj wygenerowany kod `<iframe>` (link URL).
   - W pliku `index.html` wewnątrz modalu dla danego raportu (np. sekcja `<div class="modal-visual-area">`) zamiast znacznika `<img>` wklej ramkę:
     ```html
     <iframe width="100%" height="400px" src="TWÓJ_LINK_Z_POWER_BI" frameborder="0" allowFullScreen="true"></iframe>
     ```

### C. Sekcja AI Graphic Design (Z suwakiem Przed/Po)
W projekcie umieściłem interaktywny suwak, który pozwala przesuwać granicę między dwoma nałożonymi obrazkami (szkic koncepcyjny vs końcowy render AI).
1. Zapisz swój szkic/koncepcję w folderze `assets` pod nazwą `concept_sketch.png`.
2. Zapisz gotową grafikę AI pod nazwą `final_ai_graphic.png`.
3. Jeśli chcesz dodać kolejne suwaki, możesz powielić strukturę `.comparison-slider` w kodzie HTML — skrypt automatycznie obsłuży każdy nowy suwak na stronie.

---

## 3. Jak opublikować stronę w sieci za darmo?

Ponieważ strona opiera się na czystym HTML/CSS/JS (tzw. strona statyczna), jej utrzymanie w sieci może być w 100% darmowe. Oto dwie najprostsze metody:

### Metoda A: Netlify (Najprostsza — Drag & Drop)
1. Wejdź na stronę [Netlify.com](https://www.netlify.com/) i załóż darmowe konto.
2. Zaloguj się i przejdź do zakładki **Sites**.
3. Zobaczysz tam obszar z napisem *"Want to deploy a new site without connecting to Git? Drag and drop your site folder here"*.
4. Przeciągnij cały swój folder `portfolio` (ten z plikiem `index.html`) i upuść go w tym oknie.
5. Po kilku sekundach Twoja strona będzie dostępna online pod losowym adresem (np. `https://random-name.netlify.app`).
6. W ustawieniach możesz bezpłatnie zmienić ten adres na własny (np. `karolinagrzybek.netlify.app`) lub podpiąć własną domenę.

### Metoda B: GitHub Pages (Zalecana dla programistów)
1. Załóż darmowe konto na [GitHub.com](https://github.com/).
2. Stwórz nowe repozytorium o nazwie np. `portfolio`.
3. Wgraj do niego pliki: `index.html`, `style.css`, `script.js` oraz folder `assets` z grafikami.
4. Przejdź do ustawień repozytorium (**Settings**), znajdź zakładkę **Pages** (w menu po lewej).
5. W sekcji **Build and deployment** ustaw źródło (*Source*) na **Deploy from a branch**, wybierz gałąź **main** (lub `master`) i folder `/root`, a następnie kliknij **Save**.
6. Po około 1-2 minutach Twoja strona będzie dostępna pod adresem `https://twoj-username.github.io/portfolio/`.

---

## 4. A co z WordPress-em?

Jeżeli w przyszłości zdecydujesz się przenieść tę stronę na system WordPress (np. ze względu na łatwiejsze dodawanie wpisów na blogu w przyszłości):
1. **Motyw i Builder:** Użyj darmowego motywu (np. *Astra* lub *Hello Elementor*) i wtyczki *Elementor*.
2. **Przeniesienie sekcji:** W Elementorze możesz łatwo odtworzyć zaprojektowany układ za pomocą kontenerów (Hero, O mnie, Projekty, Kontakt).
3. **Sekcje niestandardowe:** 
   - **Suwak Przed/Po:** Do WordPressa istnieje wiele darmowych wtyczek realizujących dokładnie tę funkcję (wyszukaj w kokpicie wtyczkę pod hasłem *"Before After Image Slider"*).
   - **Power BI:** Wklejanie raportów live realizuje się poprzez blok kodu HTML w Elementorze, wklejając tam wspomnianą ramkę `<iframe>` wygenerowaną z konta Power BI.
