// script.js
// All interactive client‑side behavior for the Acme Solutions portfolio site.
// Wrapped in an IIFE and executed after DOMContentLoaded to avoid polluting the global scope.

(() => {
  /** Utility Functions */
  const $$ = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));
  const $ = (selector, scope = document) => scope.querySelector(selector);

  /** Focusable elements selector for focus trapping */
  const focusableSelector =
    'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])';

  /**
   * Traps focus within a given container element.
   * @param {HTMLElement} container
   * @param {HTMLElement} previouslyFocusedEl
   */
  const trapFocus = (container, previouslyFocusedEl) => {
    const focusableEls = $$(focusableSelector, container);
    if (focusableEls.length === 0) return;
    let firstEl = focusableEls[0];
    let lastEl = focusableEls[focusableEls.length - 1];
    const keyListener = (e) => {
      if (e.key === 'Tab') {
        if (e.shiftKey) {
          // Shift + Tab
          if (document.activeElement === firstEl) {
            e.preventDefault();
            lastEl.focus();
          }
        } else {
          // Tab
          if (document.activeElement === lastEl) {
            e.preventDefault();
            firstEl.focus();
          }
        }
      } else if (e.key === 'Escape') {
        // Allow Escape to close modal if needed (handled elsewhere)
      }
    };
    container.addEventListener('keydown', keyListener);
    // Return a cleanup function
    return () => {
      container.removeEventListener('keydown', keyListener);
      if (previouslyFocusedEl) previouslyFocusedEl.focus();
    };
  };

  /** Sticky Header Implementation */
  const initStickyHeader = () => {
    const header = $('header.site-header');
    if (!header) return;
    // Create a sentinel element after the hero section
    const hero = $('#hero');
    const sentinel = document.createElement('div');
    sentinel.id = 'header-sentinel';
    sentinel.style.position = 'absolute';
    sentinel.style.top = '0';
    sentinel.style.width = '1px';
    sentinel.style.height = '1px';
    hero.parentNode.insertBefore(sentinel, hero.nextSibling);

    const toggleSticky = (isSticky) => {
      if (isSticky) {
        header.classList.add('sticky');
      } else {
        header.classList.remove('sticky');
      }
    };

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(
        ([entry]) => toggleSticky(!entry.isIntersecting),
        { rootMargin: '-1px 0px 0px 0px', threshold: 0 }
      );
      observer.observe(sentinel);
    } else {
      // Fallback using scroll event
      const heroBottom = hero.getBoundingClientRect().bottom + window.scrollY;
      const onScroll = () => {
        toggleSticky(window.scrollY > heroBottom);
      };
      window.addEventListener('scroll', onScroll);
    }
  };

  /** Smooth Scrolling for Navigation Links */
  const initNavSmoothScroll = () => {
    const navLinks = $$('.nav-link');
    navLinks.forEach((link) => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href').replace('#', '');
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
          targetEl.scrollIntoView({ behavior: 'smooth' });
        }
      });
    });
  };

  /** Gallery Lightbox */
  const initGalleryLightbox = () => {
    const galleryItems = $$('.gallery-item');
    if (galleryItems.length === 0) return;

    // Create lightbox markup
    const lightbox = document.createElement('div');
    lightbox.id = 'lightbox';
    lightbox.className = 'lightbox';
    lightbox.setAttribute('aria-modal', 'true');
    lightbox.setAttribute('role', 'dialog');
    lightbox.style.display = 'none'; // hidden by default
    lightbox.style.alignItems = 'center';
    lightbox.style.justifyContent = 'center';
    lightbox.style.position = 'fixed';
    lightbox.style.top = '0';
    lightbox.style.left = '0';
    lightbox.style.width = '100%';
    lightbox.style.height = '100%';
    lightbox.style.backgroundColor = 'rgba(0,0,0,0.8)';
    lightbox.style.zIndex = '1000';

    const img = document.createElement('img');
    img.id = 'lightboxImage';
    img.style.maxWidth = '90%';
    img.style.maxHeight = '80%';
    img.style.boxShadow = '0 0 20px rgba(0,0,0,0.5)';
    img.alt = '';

    const closeBtn = document.createElement('button');
    closeBtn.id = 'lightboxClose';
    closeBtn.setAttribute('aria-label', 'Close');
    closeBtn.innerHTML = '&times;';
    closeBtn.style.position = 'absolute';
    closeBtn.style.top = '20px';
    closeBtn.style.right = '30px';
    closeBtn.style.fontSize = '2rem';
    closeBtn.style.color = '#fff';
    closeBtn.style.background = 'transparent';
    closeBtn.style.border = 'none';
    closeBtn.style.cursor = 'pointer';

    lightbox.appendChild(img);
    lightbox.appendChild(closeBtn);
    document.body.appendChild(lightbox);

    let currentIndex = 0;
    let cleanupFocusTrap = null;
    const previouslyFocused = () => document.activeElement;

    const openLightbox = (index) => {
      const item = galleryItems[index];
      if (!item) return;
      currentIndex = index;
      img.src = item.getAttribute('href');
      img.alt = item.querySelector('img')?.alt || '';
      lightbox.style.display = 'flex';
      // Focus management
      const prevFocused = previouslyFocused();
      cleanupFocusTrap = trapFocus(lightbox, prevFocused);
      closeBtn.focus();
    };

    const closeLightbox = () => {
      lightbox.style.display = 'none';
      if (cleanupFocusTrap) cleanupFocusTrap();
    };

    // Click handling for each gallery item
    galleryItems.forEach((item, idx) => {
      item.addEventListener('click', (e) => {
        e.preventDefault();
        openLightbox(idx);
      });
    });

    // Close button
    closeBtn.addEventListener('click', closeLightbox);

    // Keyboard navigation inside lightbox
    const onKeyDown = (e) => {
      if (lightbox.style.display !== 'flex') return;
      switch (e.key) {
        case 'Escape':
          e.preventDefault();
          closeLightbox();
          break;
        case 'ArrowRight':
          e.preventDefault();
          openLightbox((currentIndex + 1) % galleryItems.length);
          break;
        case 'ArrowLeft':
          e.preventDefault();
          openLightbox((currentIndex - 1 + galleryItems.length) % galleryItems.length);
          break;
        default:
          break;
      }
    };
    document.addEventListener('keydown', onKeyDown);
  };

  /** Testimonials Carousel */
  const initTestimonialsCarousel = () => {
    const carousel = $('.testimonial-carousel');
    if (!carousel) return;
    // Ensure carousel is focusable for keyboard navigation
    carousel.setAttribute('tabindex', '0');
    const slides = $$('.testimonial', carousel);
    const total = slides.length;
    if (total === 0) return;

    // Wrap slides in a track element for transform handling
    const track = document.createElement('div');
    track.className = 'carousel-track';
    track.style.display = 'flex';
    track.style.transition = 'transform 0.5s ease-in-out';
    track.style.width = `${total * 100}%`;
    slides.forEach((slide) => {
      slide.style.flex = '0 0 100%';
      track.appendChild(slide);
    });
    // Clear original children and insert track
    carousel.innerHTML = '';
    carousel.appendChild(track);

    let currentIndex = 0;
    let intervalId = null;
    const showSlide = (index) => {
      currentIndex = (index + total) % total;
      track.style.transform = `translateX(-${currentIndex * (100 / total)}%)`;
    };
    const nextSlide = () => showSlide(currentIndex + 1);
    const prevSlide = () => showSlide(currentIndex - 1);

    const startAutoRotate = () => {
      if (intervalId) return;
      intervalId = setInterval(nextSlide, 5000);
    };
    const stopAutoRotate = () => {
      clearInterval(intervalId);
      intervalId = null;
    };

    // Auto‑rotate
    startAutoRotate();

    // Pause on hover
    carousel.addEventListener('mouseenter', stopAutoRotate);
    carousel.addEventListener('mouseleave', startAutoRotate);

    // Keyboard navigation when carousel has focus
    carousel.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') {
        e.preventDefault();
        nextSlide();
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        prevSlide();
      }
    });

    // Optional external controls (if present in markup)
    const nextBtn = $('#carouselNext');
    const prevBtn = $('#carouselPrev');
    if (nextBtn) nextBtn.addEventListener('click', nextSlide);
    if (prevBtn) prevBtn.addEventListener('click', prevSlide);
  };

  /** Contact Form Validation */
  const initContactForm = () => {
    const form = $('#contactForm');
    if (!form) return;
    const nameInput = $('#name');
    const emailInput = $('#email');
    const phoneInput = $('#phone');
    const messageInput = $('#message');

    const showError = (input, message) => {
      input.classList.remove('valid');
      input.classList.add('invalid');
      // Remove existing error message if any
      const existing = input.parentNode.querySelector('.error-msg');
      if (existing) existing.remove();
      const span = document.createElement('span');
      span.className = 'error-msg';
      span.textContent = message;
      span.style.color = 'red';
      span.style.fontSize = '0.9em';
      input.parentNode.appendChild(span);
    };

    const clearError = (input) => {
      input.classList.remove('invalid');
      input.classList.add('valid');
      const existing = input.parentNode.querySelector('.error-msg');
      if (existing) existing.remove();
    };

    const validate = () => {
      let isValid = true;
      // Name validation
      const nameVal = nameInput.value.trim();
      if (nameVal.length < 2) {
        showError(nameInput, 'Please enter at least 2 characters.');
        isValid = false;
      } else {
        clearError(nameInput);
      }
      // Email validation
      const emailVal = emailInput.value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailVal)) {
        showError(emailInput, 'Please enter a valid email address.');
        isValid = false;
      } else {
        clearError(emailInput);
      }
      // Phone validation (optional but if present must be digits 7‑15)
      const phoneVal = phoneInput.value.trim();
      if (phoneVal !== '') {
        const phoneRegex = /^\d{7,15}$/;
        if (!phoneRegex.test(phoneVal)) {
          showError(phoneInput, 'Phone must contain 7‑15 digits.');
          isValid = false;
        } else {
          clearError(phoneInput);
        }
      } else {
        clearError(phoneInput);
      }
      // Message validation
      const messageVal = messageInput.value.trim();
      if (messageVal.length < 10) {
        showError(messageInput, 'Message must be at least 10 characters.');
        isValid = false;
      } else {
        clearError(messageInput);
      }
      return isValid;
    };

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (validate()) {
        alert('Thank you! Your message has been sent.');
        form.reset();
        // Remove any lingering validation classes
        [nameInput, emailInput, phoneInput, messageInput].forEach((el) => {
          el.classList.remove('valid', 'invalid');
          const err = el.parentNode.querySelector('.error-msg');
          if (err) err.remove();
        });
      }
    });
  };

  /** Miscellaneous Enhancements */
  const initCurrentYear = () => {
    const yearSpan = $('#current-year');
    if (yearSpan) {
      yearSpan.textContent = new Date().getFullYear();
    }
  };

  /** Initialize all modules after DOM is ready */
  document.addEventListener('DOMContentLoaded', () => {
    initStickyHeader();
    initNavSmoothScroll();
    initGalleryLightbox();
    initTestimonialsCarousel();
    initContactForm();
    initCurrentYear();
  });
})();
