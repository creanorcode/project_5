document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("menuToggle");
    const nav = document.getElementById("mainNav");
    const dropdownBtn = document.querySelector(".dropbtn");

    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            nav.classList.toggle("show");
        });
    }

    dropdownBtns.forEach((btn) => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            const dropdown = this.closest(".dropdown");
            dropdown.classList.toggle("show");
        });
    });

    // Close nav when clicking a link (optional)
    nav.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", () => {
            nav.classList.remove("show");
            document.querySelectorAll(".dropdown").forEach(drop => drop.classList.remove("show"));
        });
    });
});
