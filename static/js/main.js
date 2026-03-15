/* ═══════════════════════════════════════════════════════════════
   SuperCars — Main JavaScript
   ═══════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

    // ─── 0. Theme toggle ────────────────────────────────────────
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon   = document.getElementById('themeIcon');
    const html        = document.documentElement;

    // Load saved theme or default to dark
    const savedTheme = localStorage.getItem('supercars-theme') || 'dark';
    html.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const current = html.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', next);
            localStorage.setItem('supercars-theme', next);
            updateThemeIcon(next);
        });
    }

    function updateThemeIcon(theme) {
        if (!themeIcon) return;
        themeIcon.className = theme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
    }

    // ─── 1. Navbar scroll effect ────────────────────────────────
    const navbar = document.getElementById('navbar');
    const onScroll = () => {
        navbar.classList.toggle('scrolled', window.scrollY > 40);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // ─── 2. Mobile nav toggle ───────────────────────────────────
    const navToggle = document.getElementById('navToggle');
    const navLinks  = document.getElementById('navLinks');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navLinks.classList.toggle('open');
            document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : '';
        });

        // Close on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navLinks.classList.remove('open');
                document.body.style.overflow = '';
            });
        });
    }

    // ─── 3. Scroll-reveal animation ─────────────────────────────
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealElements.forEach(el => revealObserver.observe(el));

    // ─── 4. Car search filter (Cars page) ───────────────────────
    const searchInput = document.getElementById('carSearch');
    const carGrid     = document.getElementById('carGrid');
    const noResults   = document.getElementById('noResults');

    if (searchInput && carGrid) {
        searchInput.addEventListener('input', () => {
            const query = searchInput.value.toLowerCase().trim();
            const cards = carGrid.querySelectorAll('.car-card');
            let visibleCount = 0;

            cards.forEach(card => {
                const name = (card.dataset.name || '').toLowerCase();
                const match = name.includes(query);
                card.style.display = match ? '' : 'none';
                if (match) visibleCount++;
            });

            if (noResults) {
                noResults.style.display = visibleCount === 0 ? 'block' : 'none';
            }
        });
    }

    // ─── 5. Form validation helpers ─────────────────────────────
    const bookingForm = document.getElementById('bookingForm');
    const contactForm = document.getElementById('contactForm');

    function shakeField(field) {
        field.style.borderColor = '#ef4444';
        field.style.animation = 'shake .4s ease';
        setTimeout(() => { field.style.animation = ''; }, 400);
    }

    // Add shake animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            20%, 60% { transform: translateX(-6px); }
            40%, 80% { transform: translateX(6px); }
        }
    `;
    document.head.appendChild(style);

    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            const fields = bookingForm.querySelectorAll('[required]');
            let valid = true;
            fields.forEach(f => {
                if (!f.value.trim()) {
                    shakeField(f);
                    valid = false;
                } else {
                    f.style.borderColor = '';
                }
            });
            if (!valid) e.preventDefault();
        });
    }

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            const fields = contactForm.querySelectorAll('[required]');
            let valid = true;
            fields.forEach(f => {
                if (!f.value.trim()) {
                    shakeField(f);
                    valid = false;
                } else {
                    f.style.borderColor = '';
                }
            });
            if (!valid) e.preventDefault();
        });
    }

    // ─── 6. Smooth scroll for anchor links ──────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ─── 7. Auto-dismiss flash messages ─────────────────────────
    document.querySelectorAll('.flash').forEach(flash => {
        setTimeout(() => {
            flash.style.animation = 'slideOut .35s ease forwards';
            setTimeout(() => flash.remove(), 350);
        }, 4000);
    });

    const slideOutStyle = document.createElement('style');
    slideOutStyle.textContent = `
        @keyframes slideOut {
            to { transform: translateX(120%); opacity: 0; }
        }
    `;
    document.head.appendChild(slideOutStyle);

});
