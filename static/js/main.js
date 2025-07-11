document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("menuToggle");
    const nav = document.getElementById("mainNav");
    const dropdownBtns = document.querySelectorAll(".dropbtn");

    // Toggle hamburger meny på mobil
    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            nav.classList.toggle("show");
        });
    }

    // Dropdown för "My Account"
    dropdownBtns.forEach((btn) => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            e.stopPropagation();
            const dropdown = this.closest(".dropdown");
            dropdown.classList.toggle("show");
        });
    });

    // Stäng meny och dropdown vid klick på länk (mobil)
    document.querySelectorAll(".main-nav a").forEach(link => {
        link.addEventListener("click", () => {
            nav.classList.remove("show");
            document.querySelectorAll(".dropdown").forEach(drop => drop.classList.remove("show"));
        });
    });

    // Stäng dropdown när man klickar utanför
    document.addEventListener("click", function (e) {
        document.querySelectorAll(".dropdown").forEach(dropdown => {
            if (!dropdown.contains(e.target)) {
                dropdown.classList.remove("show");
            }
        });
    });
});
