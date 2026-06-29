document.addEventListener('DOMContentLoaded', () => {
    // 1. Obsługa Mobilnego Menu
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navbar = document.querySelector('.navbar');
    const menuIcon = document.getElementById('menu-icon');

    if (mobileMenuBtn && navbar && menuIcon) {
        mobileMenuBtn.addEventListener('click', () => {
            navbar.classList.toggle('active');
            
            // Zmiana ikony menu z hamburgera na "X"
            if (navbar.classList.contains('active')) {
                menuIcon.className = 'bx bx-x';
            } else {
                menuIcon.className = 'bx bx-menu';
            }
        });

        // Zamknięcie menu po kliknięciu w link
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navbar.classList.remove('active');
                menuIcon.className = 'bx bx-menu';
            });
        });
    }

    // 2. Filtrowanie Projektów
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Usunięcie klasy active ze wszystkich przycisków
            filterButtons.forEach(button => button.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectCards.forEach(card => {
                const category = card.getAttribute('data-category');
                
                if (filterValue === 'all' || category === filterValue) {
                    card.style.display = 'flex';
                    // Animacja pojawiania się
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.95)';
                    // Ukrycie po zakończeniu animacji
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // 3. Obsługa Interaktywnego Suwaka Przed / Po (Comparison Slider)
    const sliders = document.querySelectorAll('.comparison-slider');

    sliders.forEach(slider => {
        const rangeInput = slider.querySelector('.slider-range-input');
        const imgAfter = slider.querySelector('.image-after');
        const handle = slider.querySelector('.slider-handle');

        if (rangeInput && imgAfter && handle) {
            rangeInput.addEventListener('input', (e) => {
                const value = e.target.value;
                
                // Ustawienie szerokości górnego obrazka (Final AI)
                imgAfter.style.width = `${value}%`;
                
                // Ustawienie pozycji pionowej kreski z uchwytem
                handle.style.left = `${value}%`;
            });
        }
    });


    // 4. Obsługa Modali ze Szczegółami Projektów
    const openModalBtns = document.querySelectorAll('.open-modal-btn');
    const closeModalBtns = document.querySelectorAll('.close-modal-btn');
    const modals = document.querySelectorAll('.modal');

    openModalBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const modalId = btn.getAttribute('data-modal');
            const targetModal = document.getElementById(modalId);
            
            if (targetModal) {
                targetModal.classList.add('active');
                document.body.style.overflow = 'hidden'; // Zablokowanie przewijania strony
            }
        });
    });

    closeModalBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const activeModal = btn.closest('.modal');
            if (activeModal) {
                activeModal.classList.remove('active');
                document.body.style.overflow = 'auto'; // Przywrócenie przewijania strony
            }
        });
    });

    // Zamknięcie modala po kliknięciu poza obszarem karty
    modals.forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
                document.body.style.overflow = 'auto';
            }
        });
    });

    // 5. Obsługa Formularza Kontaktowego & Powiadomień (Toast)
    const contactForm = document.getElementById('portfolio-contact-form');
    const toast = document.getElementById('toast-message');

    if (contactForm && toast) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            // Pokazanie powiadomienia Toast
            toast.classList.add('active');

            // Czyszczenie pól formularza
            contactForm.reset();

            // Ukrycie powiadomienia po 4 sekundach
            setTimeout(() => {
                toast.classList.remove('active');
            }, 4000);
        });
    }

    // 6. Aktywacja linków w menu podczas przewijania (Scroll Spy)
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        let current = '';

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (pageYOffset >= (sectionTop - sectionHeight / 3)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

    // 7. Carousel Logic
    const carousels = document.querySelectorAll('.carousel-wrapper');
    carousels.forEach(carousel => {
        const slides = carousel.querySelector('.carousel-slides');
        const dots = carousel.querySelectorAll('.carousel-dot');
        const prevBtn = carousel.querySelector('.prev-btn');
        const nextBtn = carousel.querySelector('.next-btn');

        if (!slides || !dots.length) return;

        let currentIndex = 0;
        const totalSlides = dots.length;

        const updateCarousel = (index) => {
            slides.scrollTo({
                left: slides.clientWidth * index,
                behavior: 'smooth'
            });
            dots.forEach(d => d.classList.remove('active'));
            dots[index].classList.add('active');
            currentIndex = index;
        };

        if (prevBtn && nextBtn) {
            prevBtn.addEventListener('click', () => {
                let index = currentIndex - 1;
                if (index < 0) index = totalSlides - 1;
                updateCarousel(index);
            });
            nextBtn.addEventListener('click', () => {
                let index = currentIndex + 1;
                if (index >= totalSlides) index = 0;
                updateCarousel(index);
            });
        }

        dots.forEach((dot, idx) => {
            dot.addEventListener('click', () => {
                updateCarousel(idx);
            });
        });

        // Update dots on scroll
        slides.addEventListener('scroll', () => {
            const index = Math.round(slides.scrollLeft / slides.clientWidth);
            if (index !== currentIndex && index >= 0 && index < totalSlides) {
                dots.forEach(d => d.classList.remove('active'));
                dots[index].classList.add('active');
                currentIndex = index;
            }
        });
    });
});
