document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("menuToggle");
    const nav = document.getElementById("mainNav");
    const dropdownBtn = document.querySelector(".dropbtn");
    const dropdownContent = document.querySelector(".dropdown-content");
    const dropdownContainer = document.querySelector(".dropdown");

    // Hamburger toggle for small screens
    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            nav.classList.toggle("show");
        });

        nav.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", () => {
                if (dropdownContainer) {
                    dropdownContainer.classList.remove("show");
                }
            });
        });
    }

    // Dropdown toggle on click for mobile
    if (dropdownBtn && dropdownContainer) {
        dropdownBtn.addEventListener("click", function (e) {
            // Only allow toggle on small screens
            if (window.innerWidth <= 768) {
                e.preventDefault();
                e.stopPropagation();
                dropdownContainer.classList.toggle("show");
            }
        });
    }

    // CLose dropdown when clicking outside (on mobile only)
    document.addEventListener("click", function (e) {
        if (
            window.innerWidth <= 768 &&
            dropdownContainer &&
            !dropdownContainer.contains(e.target)
        ) {
            dropdownContainer.classList.remove("show");
        }
    });
});
