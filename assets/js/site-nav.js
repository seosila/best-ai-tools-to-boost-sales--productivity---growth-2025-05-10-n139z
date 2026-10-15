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


    // Add BreadcrumbList structured data from the breadcrumb navigation users can see.
    // Keep the markup synchronized with the page's existing breadcrumb labels and links.
    const breadcrumbNav = document.querySelector('nav[aria-label="Breadcrumb"]');
    if (breadcrumbNav && !document.querySelector('script[data-generated-breadcrumb-schema]')) {
        const entries = [];
        const parts = Array.from(breadcrumbNav.children);
        parts.forEach(function (part) {
            if (part.matches('a')) {
                const name = part.textContent.trim();
                const href = part.getAttribute('href');
                if (name && href) {
                    entries.push({
                        '@type': 'ListItem',
                        position: entries.length + 1,
                        name: name,
                        item: new URL(href, window.location.href).href
                    });
                }
            } else if (part.matches('span') && part.getAttribute('aria-hidden') !== 'true') {
                const name = part.textContent.trim();
                if (name) {
                    const item = {
                        '@type': 'ListItem',
                        position: entries.length + 1,
                        name: name
                    };
                    entries.push(item);
                }
            }
        });

        if (entries.length >= 2) {
            const schema = document.createElement('script');
            schema.type = 'application/ld+json';
            schema.setAttribute('data-generated-breadcrumb-schema', 'true');
            schema.textContent = JSON.stringify({
                '@context': 'https://schema.org',
                '@type': 'BreadcrumbList',
                itemListElement: entries
            });
            document.head.appendChild(schema);
        }
    }

});