(function () {
  'use strict';
  var systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  var preference = null;
  var storageKey = 'syncnuke-theme';
  try {
    var saved = localStorage.getItem(storageKey);
    if (saved === 'light' || saved === 'dark') preference = saved;
  } catch (error) { /* Use the system theme when storage is unavailable. */ }

  function applyTheme() {
    var dark = preference ? preference === 'dark' : systemTheme.matches;
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    var stylesheet = document.getElementById('night-theme');
    if (stylesheet) stylesheet.media = dark ? 'all' : 'not all';
    var button = document.querySelector('.theme-toggle');
    if (button) {
      button.hidden = false;
      var label = dark ? 'Switch to light mode' : 'Switch to night mode';
      button.setAttribute('aria-label', label);
      button.title = label;
      button.querySelector('.theme-icon-moon').toggleAttribute('hidden', dark);
      button.querySelector('.theme-icon-sun').toggleAttribute('hidden', !dark);
    }
  }
  // Apply before the body renders to avoid flashing the wrong theme.
  applyTheme();
  document.addEventListener('DOMContentLoaded', function () {
    applyTheme();
    document.querySelector('.theme-toggle').addEventListener('click', function () {
      preference = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem(storageKey, preference); } catch (error) { /* Keep the in-page choice. */ }
      applyTheme();
    });
  });
  systemTheme.addEventListener('change', applyTheme);
  window.addEventListener('storage', function (event) {
    if (event.key === storageKey || event.key === null) {
      preference = event.newValue === 'light' || event.newValue === 'dark' ? event.newValue : null;
      applyTheme();
    }
  });
}());
