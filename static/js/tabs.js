document.addEventListener("DOMContentLoaded", function () {
    const menu = document.querySelector(".menu");
    const menuItems = document.querySelectorAll(".menu__item");
    const menuBorder = document.querySelector(".menu__border");
    const tabContents = document.querySelectorAll(".tab-content");

    let activeItem = menu.querySelector(".active");

    function clickItem(item) {
        if (activeItem === item) return;
        activeItem.classList.remove("active");

        item.classList.add("active");
        activeItem = item;
        offsetMenuBorder(activeItem, menuBorder);

        // Tab switching
        const selectedTab = item.getAttribute("data-tab");
        tabContents.forEach(content => content.classList.remove("active"));
        document.getElementById(selectedTab).classList.add("active");
    }

    function offsetMenuBorder(element, menuBorder) {
        const offsetActiveItem = element.getBoundingClientRect();
        const left = Math.floor(offsetActiveItem.left - menu.offsetLeft - (menuBorder.offsetWidth - offsetActiveItem.width) / 2) + "px";
        menuBorder.style.transform = `translate3d(${left}, 0 , 0)`;
    }

    menuItems.forEach(item => {
        item.addEventListener("click", () => clickItem(item));
    });

    window.addEventListener("resize", () => offsetMenuBorder(activeItem, menuBorder));
    offsetMenuBorder(activeItem, menuBorder);
});
