import re
import os

html_path = r"c:\Users\karol\.gemini\antigravity\portfolio\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Cards replacements
# We want to keep the two powerbi cards, and replace the two aidesign cards with our 4 new cards.
# First, let's locate the projects-grid content.
match = re.search(r'(<div class="projects-grid">)(.*?)(</section>)', html, re.DOTALL)
if match:
    projects_grid_content = match.group(2)
    # Extract only powerbi cards
    powerbi_cards = re.findall(r'<div class="project-card glass-card" data-category="powerbi">.*?</div>\s*</div>', projects_grid_content, re.DOTALL)
    
    new_cards = """
            <!-- Projekt 1: Power BI -->
            <div class="project-card glass-card" data-category="powerbi">
                <div class="project-img-wrapper">
                    <img src="assets/powerbi_dashboard.png" alt="Dashboard Power BI" class="project-img">
                    <span class="category-badge badge-cyan">Power BI</span>
                </div>
                <div class="project-info">
                    <h3>Dashboard Ośrodka Badań Biegłości ISO</h3>
                    <p>Zaawansowany panel analityczny dedykowany monitorowaniu zgodności statystycznej wyników badań laboratoryjnych z wymaganiami norm ISO 17043/17025.</p>
                    <div class="project-tags">
                        <span>DAX</span>
                        <span>Power Query</span>
                        <span>Analiza Statystyczna</span>
                    </div>
                    <button class="btn btn-outline btn-sm open-modal-btn" data-modal="modal-pbi-1">Szczegóły projektu</button>
                </div>
            </div>

            <!-- Projekt 2: Power BI -->
            <div class="project-card glass-card" data-category="powerbi">
                <div class="project-img-wrapper">
                    <img src="assets/powerbi_dashboard.png" alt="Analiza Efektywności Biznesowej" class="project-img" style="filter: hue-rotate(120deg);">
                    <span class="category-badge badge-cyan">Power BI</span>
                </div>
                <div class="project-info">
                    <h3>Panel Analizy Efektywności i Kosztów</h3>
                    <p>Dashboard optymalizacyjny integrujący dane o kosztach operacyjnych z wydajnością maszyn i terminowością laboratoriów w ujęciu kwartalnym.</p>
                    <div class="project-tags">
                        <span>KPI</span>
                        <span>SQL</span>
                        <span>Excel Integration</span>
                    </div>
                    <button class="btn btn-outline btn-sm open-modal-btn" data-modal="modal-pbi-2">Szczegóły projektu</button>
                </div>
            </div>

            <!-- Projekt 3: AI Design - Packshot -->
            <div class="project-card glass-card" data-category="aidesign">
                <div class="project-img-wrapper">
                    <img src="assets/packshot_final.jpg" alt="Packshot Fotorealizm" class="project-img">
                    <span class="category-badge badge-purple">AI Graphic Design</span>
                </div>
                <div class="project-info">
                    <h3>Fotorealizm i Integracja (Packshot)</h3>
                    <p>Zaawansowana generacja fotorealistycznego tła z zachowaniem detali obiektu referencyjnego (szklany słoiczek) i precyzyjną fizyką odbić.</p>
                    <div class="project-tags">
                        <span>Gemini (Imagen 3)</span>
                        <span>Python (Pillow)</span>
                    </div>
                    <button class="btn btn-outline btn-sm open-modal-btn" data-modal="modal-ai-1">Szczegóły projektu</button>
                </div>
            </div>

            <!-- Projekt 4: AI Design - Skandynawska Jesień -->
            <div class="project-card glass-card" data-category="aidesign">
                <div class="project-img-wrapper">
                    <img src="assets/1_salon_16_9.jpg" alt="Skandynawska Jesień" class="project-img">
                    <span class="category-badge badge-purple">AI Graphic Design</span>
                </div>
                <div class="project-info">
                    <h3>Spójność Stylu (Skandynawska Jesień)</h3>
                    <p>Seria 3 grafik promocyjnych (salon, sypialnia, jadalnia) wygenerowanych przy pomocy Shared Tokens dla ścisłej spójności oświetlenia i kolorystyki.</p>
                    <div class="project-tags">
                        <span>Prompt Engineering</span>
                        <span>Stylizacja Wnętrz</span>
                    </div>
                    <button class="btn btn-outline btn-sm open-modal-btn" data-modal="modal-ai-2">Szczegóły projektu</button>
                </div>
            </div>

            <!-- Projekt 5: AI Design - Outpainting -->
            <div class="project-card glass-card" data-category="aidesign">
                <div class="project-img-wrapper">
                    <img src="assets/fixed_image.png" alt="Outpainting" class="project-img">
                    <span class="category-badge badge-purple">AI Graphic Design</span>
                </div>
                <div class="project-info">
                    <h3>Postprodukcja i Outpainting</h3>
                    <p>Naprawa obrazu, inpainting defektów i rozszerzenie do formatu 16:9, dbając o precyzję rekonstrukcji tła architektonicznego.</p>
                    <div class="project-tags">
                        <span>Inpainting</span>
                        <span>Outpainting</span>
                    </div>
                    <button class="btn btn-outline btn-sm open-modal-btn" data-modal="modal-ai-3">Szczegóły projektu</button>
                </div>
            </div>

            <!-- Projekt 6: AI Design - Video -->
            <div class="project-card glass-card" data-category="aidesign">
                <div class="project-img-wrapper">
                    <video autoplay loop muted playsinline class="project-img" style="object-fit: cover;">
                        <source src="assets/Zad_4_Gotowe.mp4" type="video/mp4">
                    </video>
                    <span class="category-badge badge-purple">AI Video</span>
                </div>
                <div class="project-info">
                    <h3>Wideo Generatywne i Dźwięk</h3>
                    <p>Pionowe wideo (9:16) promujące letnią kolekcję mody. Płynne Image-to-Video połączone z energetycznym podkładem Suno/Udio.</p>
                    <div class="project-tags">
                        <span>Image-to-Video</span>
                        <span>Audio AI</span>
                        <span>Python Skrypt</span>
                    </div>
                    <button class="btn btn-outline btn-sm open-modal-btn" data-modal="modal-ai-4">Szczegóły projektu</button>
                </div>
            </div>
        </div>
"""
    
    html = html[:match.start(2)] + "\n" + new_cards + "\n    " + html[match.end(2):]

# Now for modals
modals_new = """

    <!-- Modal AI 1 -->
    <div class="modal" id="modal-ai-1">
        <div class="modal-content glass-card">
            <div class="modal-header">
                <h3>Fotorealizm i Integracja Produktu (Packshot)</h3>
                <span class="close-modal-btn">&times;</span>
            </div>
            <div class="modal-body">
                <div class="modal-grid">
                    <div class="modal-visual-area">
                        <img src="assets/packshot_final.jpg" alt="Finalny projekt AI" class="modal-img">
                    </div>
                    <div class="modal-details-area">
                        <h4>Kontekst Marketingowy i Zadanie</h4>
                        <p>Zadaniem było wygenerowanie zintegrowanego packshotu z produktem, z zachowaniem detali obiektu referencyjnego (etykieta, kształt zakrętki) przy jednoczesnym wygenerowaniu fizycznie poprawnych interakcji świetlnych.</p>
                        
                        <h4>Proces Projektowy</h4>
                        <ul>
                            <li><strong>Gemini (Imagen 3):</strong> Użyty do wygenerowania realistycznego tła (ciepłe letnie światło, marmurowy blat, liście palmy). Zapewnił spójne odbicie szklanego słoiczka na wypolerowanym marmurze oraz miękki cień, który idealnie stapia produkt z podłożem.</li>
                            <li><strong>Python (Pillow):</strong> Skrypt użyty do wyodrębnienia oryginalnego produktu i przygotowania fizycznych warstw (background, product, shadow) w celach edycji.</li>
                        </ul>

                        <h4>Narzędzia</h4>
                        <div class="modal-tags">
                            <span>Gemini (Imagen 3)</span>
                            <span>Python (Pillow)</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal AI 2 -->
    <div class="modal" id="modal-ai-2">
        <div class="modal-content glass-card">
            <div class="modal-header">
                <h3>Spójność Stylu (Skandynawska Jesień)</h3>
                <span class="close-modal-btn">&times;</span>
            </div>
            <div class="modal-body">
                <div class="modal-grid">
                    <div class="modal-visual-area">
                        <img src="assets/1_salon_16_9.jpg" alt="Salon" class="modal-img">
                    </div>
                    <div class="modal-details-area">
                        <h4>Kontekst Marketingowy i Zadanie</h4>
                        <p>Stworzenie spójnej serii 3 grafik promocyjnych (salon, sypialnia, jadalnia) zachowujących identyczną kolorystykę i oświetlenie (styl: skandynawska jesień).</p>
                        
                        <h4>Proces Projektowy</h4>
                        <ul>
                            <li><strong>Shared Tokens:</strong> Zastosowanie techniki precyzyjnego opisywania elementów wspólnych w promptach (m.in. paleta kolorów, styl oświetlenia "Golden Hour", minimalistyczna kompozycja).</li>
                            <li><strong>Postprodukcja:</strong> Automatyczne centrowanie i kadrowanie za pomocą skryptu Python do docelowych formatów 16:9, 1:1, 9:16.</li>
                        </ul>

                        <h4>Narzędzia</h4>
                        <div class="modal-tags">
                            <span>Prompt Engineering</span>
                            <span>Gemini</span>
                            <span>Python (Pillow)</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal AI 3 -->
    <div class="modal" id="modal-ai-3">
        <div class="modal-content glass-card">
            <div class="modal-header">
                <h3>Postprodukcja i Outpainting</h3>
                <span class="close-modal-btn">&times;</span>
            </div>
            <div class="modal-body">
                <div class="modal-grid">
                    <div class="modal-visual-area">
                        <img src="assets/fixed_image.png" alt="Outpainting" class="modal-img">
                    </div>
                    <div class="modal-details-area">
                        <h4>Kontekst Marketingowy i Zadanie</h4>
                        <p>Naprawienie zdjęcia modelki (usunięcie nienaturalnego przechodnia w tle) oraz rozszerzenie go do proporcji 16:9 z wykorzystaniem techniki Outpaintingu, z zachowaniem oryginalnego tła ceglanego muru.</p>
                        
                        <h4>Proces Projektowy</h4>
                        <ul>
                            <li><strong>Inpainting/Outpainting:</strong> Użycie modelu Gemini z precyzyjnymi promptami modyfikującymi (usunięcie obiektów) oraz rozszerzającymi (kontynuacja architektury).</li>
                            <li><strong>Python (Pillow):</strong> Skryptowe wycinanie i dopasowanie proporcji kadru.</li>
                            <li><strong>Wyzwania:</strong> Analiza ograniczeń anatomii dłoni AI i uzasadnienie potrzeby ręcznego retuszu.</li>
                        </ul>

                        <h4>Narzędzia</h4>
                        <div class="modal-tags">
                            <span>Inpainting</span>
                            <span>Outpainting</span>
                            <span>Gemini</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal AI 4 -->
    <div class="modal" id="modal-ai-4">
        <div class="modal-content glass-card">
            <div class="modal-header">
                <h3>Wideo Generatywne i Dźwięk</h3>
                <span class="close-modal-btn">&times;</span>
            </div>
            <div class="modal-body">
                <div class="modal-grid">
                    <div class="modal-visual-area">
                        <video autoplay loop muted playsinline class="modal-img" style="width:100%; border-radius: 8px;">
                            <source src="assets/Zad_4_Gotowe.mp4" type="video/mp4">
                        </video>
                    </div>
                    <div class="modal-details-area">
                        <h4>Kontekst Marketingowy i Zadanie</h4>
                        <p>Stworzenie pionowego, fotorealistycznego wideo reklamowego (9:16) promującego letnią kolekcję oraz spójnego, energetycznego podkładu muzycznego z minimalistyczną nakładką tekstową.</p>
                        
                        <h4>Proces Projektowy</h4>
                        <ul>
                            <li><strong>Image-to-Video:</strong> Generacja wideo interpolującego klatki początkową i końcową (najwyższa kontrola spójności postaci).</li>
                            <li><strong>Audio AI (Suno/Udio):</strong> Generacja podkładu śródziemnomorskiego dopasowanego do klimatu sceny.</li>
                            <li><strong>Automatyczny Montaż:</strong> Połączenie audio z wideo i nałożenie napisu przy użyciu dedykowanego skryptu Python (FFmpeg & OpenCV).</li>
                        </ul>

                        <h4>Narzędzia</h4>
                        <div class="modal-tags">
                            <span>Video AI (Luma/Kling/Runway)</span>
                            <span>Audio AI (Suno/Udio)</span>
                            <span>Python & FFmpeg</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

# Replace old modals. Modals start from <!-- Modal Power BI 1 --> to <!-- Sekcja Kontakt -->
modals_pattern = re.compile(r'(<!-- Modale ze szczegółami projektów -->\s*)(.*?)(<!-- Sekcja Kontakt -->)', re.DOTALL)
match_modals = modals_pattern.search(html)

if match_modals:
    modals_content = match_modals.group(2)
    # Extract only powerbi modals
    powerbi_modals = re.findall(r'<!-- Modal Power BI \d+ -->.*?</div>\s*</div>\s*</div>', modals_content, re.DOTALL)
    
    new_modals_section = "\n".join(powerbi_modals) + "\n" + modals_new + "\n    "
    html = html[:match_modals.start(2)] + new_modals_section + html[match_modals.end(2):]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully.")
