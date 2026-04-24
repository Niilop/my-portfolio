// Sticky nav shadow on scroll
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 10);
}, { passive: true });

// Intersection Observer — fade-in sections
const observer = new IntersectionObserver(
  (entries) => entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }),
  { threshold: 0.12 }
);
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

// Contact form — AJAX submit
const form = document.getElementById('contact-form');
if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn    = document.getElementById('submit-btn');
    const status = document.getElementById('form-status');
    const body   = {
      name:    form.name.value.trim(),
      email:   form.email.value.trim(),
      message: form.message.value.trim(),
    };

    btn.disabled = true;
    btn.textContent = 'Sending…';
    status.className = 'form-status';
    status.textContent = '';

    try {
      const res  = await fetch('/api/contact', {
        method:  'POST',
        headers: { 'Content-Type': 'application/json' },
        body:    JSON.stringify(body),
      });
      const data = await res.json();
      if (res.ok && data.success) {
        status.className = 'form-status success';
        status.textContent = data.message;
        form.reset();
      } else {
        throw new Error(data.detail || 'Something went wrong.');
      }
    } catch (err) {
      status.className = 'form-status error';
      status.textContent = err.message || 'Failed to send. Try emailing directly.';
    } finally {
      btn.disabled = false;
      btn.textContent = 'Send Message';
    }
  });
}
