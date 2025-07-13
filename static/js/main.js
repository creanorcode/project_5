document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("menuToggle");
    const nav = document.getElementById("mainNav");
    const dropbtn = document.querySelectorAll(".accountDropdownBtn");
    const dropdown = dropbtn?.closest(".dropdown");

    // Toggle hamburger meny på mobil
    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            nav.classList.toggle("show");
        });
    }

    // Toggle dropdown för "My Account" på mobil
    if (dropbtn && dropdown) {
        dropbtn.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation(); // hindrar att menyn stängs direkt
            dropdown.classList.toggle("show");
        });

        // Stäng dropdown om man klickar utanför
        document.addEventListener("click", (e) => {
            if (!dropdown.contains(e.target) && !dropbtn.contains(e.target)) {
                dropdown.classList.remove("show");
            }
        });
    }

    // Stäng nav + dropdown vid klick på länk (mobil)
    nav?.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", () => {
            nav.classList.remove("show");
            dropdown?.classList.remove("show");
        });
    });
});
