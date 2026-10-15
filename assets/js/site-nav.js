document.addEventListener('DOMContentLoaded', function () {
    const menuButton = document.querySelector('.sb-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (!menuButton || !mobileMenu) return;

    function setMenuOpen(isOpen) {
        menuButton.setAttribute('aria-expanded', String(isOpen));
        menuButton.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
        mobileMenu.hidden = !isOpen;
    }

    menuButton.addEventListener('click', function () {
        setMenuOpen(menuButton.getAttribute('aria-expanded') !== 'true');
    });

    mobileMenu.addEventListener('click', function (event) {
        if (event.target.closest('a')) setMenuOpen(false);
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') setMenuOpen(false);
    });

    window.addEventListener('resize', function () {
        if (window.innerWidth >= 800) setMenuOpen(false);
    });
});
