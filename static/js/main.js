document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("menuToggle");
    const nav = document.getElementById("mainNav");
    const dropdowns = document.querySelectorAll(".dropdown");

    // 1. Toggle hamburger-menyn
    toggle.addEventListener("click", () => {
        nav.classList.toggle("show");
    });

    // Dropdown toggling on click
    dropdowns.forEach(drop => {
        const btn = drop.querySelector(".dropbtn");
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            e.stopPropagation();
            drop.classList.toggle("open");
        });
    });

    // Klick utanför dropdown stänger den
    document.addEventListener("click", () => {
        dropdowns.forEach(drop => drop.classList.remove("open"));
    });
});
