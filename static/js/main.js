document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("menuToggle");
    const nav = document.getElementById("mainNav");
    const dropdownBtn = document.querySelector(".dropbtn");
    const dropdownContainer = document.querySelector(".dropdown");

    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            nav.classList.toggle("show");
        });

        // Close the menu when clicking on a link.
        nav.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", () => {
                nav.classList.remove("show");
                if (dropdownContainer) {
                    dropdownContainer.classList("show");
                }
            });
        });
    }

    // Toggle dropdown " My Account"
    if (dropdownBtn && dropdownContainer) {
        dropdownBtn.addEventListener("click", (e) => {
            e.preventDefault(); // förhindra att länken navigerar
            dropdownContainer.classList.toggle("show"); 
        });
    }
});
