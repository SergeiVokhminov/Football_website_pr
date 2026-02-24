document.getElementById("toggle-nav").addEventListener("click", function() {
    const nav = document.getElementById("navigation");

    // Переключаем видимость навигации
    nav.classList.toggle("visible");

    // Сдвигаем фон страницы
    if (nav.classList.contains("visible")) {
        document.body.style.backgroundPosition = "200px 0";
    } else {
        document.body.style.backgroundPosition = "0 0";
    }
});
