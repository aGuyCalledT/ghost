document.addEventListener('DOMContentLoaded', function() {
    fetch('/list_files') // Anfrage an das Backend
        .then(response => response.json())
        .then(files => {
            const fileList = document.getElementById('file-list');
            files.forEach(file => {
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                    <span>${file}</span>
                `;
                card.addEventListener('click', () => {
                    window.location.href = '/' + file; // Download-Link
                });
                fileList.appendChild(card);
            });
        });
    
        var pfadname = window.location.pathname;
        var seitenname = pfadname.substring(pfadname.lastIndexOf('/') + 1);
        var unterseiteAnzeige = document.getElementById('unterseite-anzeige');

        if (seitenname === 'kontakt.html') {
            unterseiteAnzeige.textContent = '/Kontakt';
        } else if (seitenname === 'ueber_mich.html') {
            unterseiteAnzeige.textContent = '/Über mich';
        } else if (seitenname === 'aktuelle_projekte.html') {
            unterseiteAnzeige.textContent = '/Aktuelle Projekte';
        } else if (seitenname === 'cloud.html') {
            unterseiteAnzeige.textContent = '/Cloud';
        } else if (seitenname === 'python.html') {
            unterseiteAnzeige.textContent = '/python_toolbox';
        } else if (seitenname === 'unsinn.html') {
            unterseiteAnzeige.textContent = '/Unsinn';
        } else if (seitenname === 'arch_linux.html') {
            unterseiteAnzeige.textContent = '/I use arch btw';
        } else if (seitenname === 'chat.html') {
            unterseiteAnzeige.textContent = '/Chat';
        } else if (seitenname === 'nachricht.html') {
            unterseiteAnzeige.textContent = '/Nachricht hinterlassen';
        } else if (seitenname === 'web_scraper.html') {
            unterseiteAnzeige.textContent = '/Web Scraper';
        } else if (seitenname === 'burn.html') {
            unterseiteAnzeige.textContent = '/Burn';
        } else if (seitenname === 'console.html') {
            unterseiteAnzeige.textContent = '/Server Control';
        } else if (seitenname === 'cat.html') {
            unterseiteAnzeige.textContent = '/Cat 🐱';
        } else if (seitenname === 'index.html') {
            unterseiteAnzeige.textContent = '/#';
        } else {
            unterseiteAnzeige.textContent = ''; 
        }
});