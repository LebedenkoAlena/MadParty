const header = document.querySelector("header");
const burgerToggle = header.querySelector("#header-burger")

burgerToggle.addEventListener("click", () => {
    header.classList.toggle("mobile-active")
    console.log("asd")
})