const color_samples = document.querySelectorAll("div.color-palette-sample");

color_samples.forEach(el => {
    const color = el.parentElement.querySelector("input").getAttribute('value');
    if (color === "Natural") {
        el.innerText = 'Naturalny kolor drewna, z którego wykonano mebel';
        el.style.border = 0;
    } else {
        el.style.backgroundColor = color;
    }
})
