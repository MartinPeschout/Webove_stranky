// Najdeme button pro přepínání motivu
const btn = document.getElementById('theme-toggle');

// Načteme uložený motiv nebo preferenci systému
const savedTheme = localStorage.getItem('theme');
const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const currentTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');

// Nastavíme data-theme na <html>
document.documentElement.setAttribute('data-theme', currentTheme);

// Změníme ikonku tlačítka podle motivu
btn.textContent = currentTheme === 'dark' ? '☀️' : '🌙';

// Po kliknutí přepínáme theme a ukládáme volbu
btn.addEventListener('click', () => {
  const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  btn.textContent = newTheme === 'dark' ? '☀️' : '🌙';
});