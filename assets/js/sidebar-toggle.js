document.addEventListener('DOMContentLoaded', function () {
  const STORAGE_KEY = 'sidebar-collapsed';
  const body = document.body;

  // Restore saved state
  if (localStorage.getItem(STORAGE_KEY) === 'true') {
    body.classList.add('sidebar-collapsed');
  }

  // Create toggle button
  const btn = document.createElement('button');
  btn.className = 'sidebar-toggle-btn';
  btn.setAttribute('aria-label', 'Toggle sidebar');
  btn.innerHTML =
    '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';

  btn.addEventListener('click', function () {
    body.classList.toggle('sidebar-collapsed');
    localStorage.setItem(
      STORAGE_KEY,
      body.classList.contains('sidebar-collapsed')
    );
  });

  // Insert at top of sidebar
  const sideBar = document.querySelector('.side-bar');
  if (sideBar) {
    const nav = sideBar.querySelector('.nav');
    if (nav) {
      nav.parentNode.insertBefore(btn, nav);
    } else {
      sideBar.insertBefore(btn, sideBar.firstChild);
    }
  }
});
