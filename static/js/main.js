document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("menuToggle");
    const nav = document.getElementById("mainNav");
    const dropdownBtns = document.querySelectorAll(".dropbtn");

    // 1. Toggle hamburger-menyn
    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            nav.classList.toggle("show");
        });
    }

    // 2. Dropdown-knapp för "My Account"
    dropdownBtns.forEach((btn) => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            e.stopPropagation();  // 🛑 Hindrar dropdown från att stängas direkt

            // Closes all other first
            document.querySelectorAll(".dropdown").forEach(drop => {
                if (drop !== this.closest(".dropdown")) {
                    drop.classList.remove("show");
                }
            });

            // Toggle the current one
            const dropdown = this.closest(".dropdown");
            dropdown.classList.toggle("show");
        });
    });

    // 3. Stäng meny och dropdown vid klick på länk
    document.querySelectorAll(".main-nav a").forEach(link => {
        link.addEventListener("click", () => {
            nav.classList.remove("show");
            document.querySelectorAll(".dropdown").forEach(drop => drop.classList.remove("show"));
        });
    });

    // 4. Stäng dropdown om man klickar utanför
    document.addEventListener("click", function (e) {
        document.querySelectorAll(".dropdown").forEach(dropdown => {
            const button = dropdown.querySelector(".dropbtn");
            if (!dropdown.contains(e.target) && !button.contains(e.target)) {
                dropdown.classList.remove("show");
            }
        });
    });
});
