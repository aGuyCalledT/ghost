document.addEventListener('DOMContentLoaded', function() {
    const body = document.body;
    const darkmodeToggle = document.getElementById('darkmode-toggle');
    const darkmodeToggleButton = document.getElementById('darkmode-toggle-button');
    const darkModeLogo = document.querySelector('.dark-mode-logo');
    const lightModeLogo = document.querySelector('.light-mode-logo');

    function toggleDarkMode(theme) {
        if (theme === 'light' || (!theme && body.classList.contains('dark-mode'))) {
            document.documentElement.classList.remove('dark-mode');
            document.documentElement.classList.add('light-mode');
            if (darkmodeToggle) darkmodeToggle.textContent = 'Dark Mode';
            if (darkmodeToggleButton) darkmodeToggleButton.textContent = 'Dark Mode';
            if (darkModeLogo) darkModeLogo.style.display = 'none';
            if (lightModeLogo) lightModeLogo.style.display = 'block';
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.classList.remove('light-mode');
            document.documentElement.classList.add('dark-mode');
            if (darkmodeToggle) darkmodeToggle.textContent = 'Light Mode';
            if (darkmodeToggleButton) darkmodeToggleButton.textContent = 'Light Mode';
            if (darkModeLogo) darkModeLogo.style.display = 'block';
            if (lightModeLogo) lightModeLogo.style.display = 'none';
            localStorage.setItem('theme', 'dark');
        }
    }

    // Initialen Zustand aus localStorage laden
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        toggleDarkMode(savedTheme);
    }

    // Event Listener für beide Buttons
    const toggleButtons = [darkmodeToggle, darkmodeToggleButton].filter(Boolean); // Entfernt undefined Buttons
    toggleButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            toggleDarkMode();
        });
    });
});