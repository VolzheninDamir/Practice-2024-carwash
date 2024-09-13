const pricelistButton = document.getElementById("pricelist-button");
const pricelistPopup = document.getElementById("pricelist-popup");
const closePopupButton = document.getElementById("close-popup");

const saleButton = document.getElementById("sale-button");
const salePopup = document.getElementById("sale-popup");
const closesalePopupButton = document.getElementById("close-sale-popup");

pricelistButton.addEventListener("click", () => {
    salePopup.classList.add("hidden");
    pricelistPopup.classList.remove("hidden"); // Показываем прайс-лист
});

closePopupButton.addEventListener("click", () => {
    pricelistPopup.classList.add("hidden"); // Скрываем прайс-лист
});

saleButton.addEventListener("click", () => {
    pricelistPopup.classList.add("hidden");
    salePopup.classList.remove("hidden"); // Показываем прайс-лист
});

closesalePopupButton.addEventListener("click", () => {
    salePopup.classList.add("hidden"); // Скрываем прайс-лист
});

