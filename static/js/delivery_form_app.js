const divDeliveryAddress = document.querySelector("#delivery_address");
const inputsDeliveryAddress = document.querySelectorAll("div#delivery_address input");
const input1 = document.querySelector("#id_delivery_type_0");
const input2 = document.querySelector("#id_delivery_type_1");
const input3 = document.querySelector("#id_delivery_type_2");

if (input1.checked) {
    divDeliveryAddress.style.display = 'none'
    inputsDeliveryAddress.forEach(el => {
        el.removeAttribute("required")
    })
}

input1.addEventListener('focus', evt => {
    divDeliveryAddress.style.display = 'none'
    inputsDeliveryAddress.forEach(el => {
        el.removeAttribute("required")
    })
})

input2.addEventListener('focus', evt => {
    divDeliveryAddress.style.display = 'block'
    inputsDeliveryAddress.forEach(el => {
        el.setAttribute("required", 'True')
    })
})

input3.addEventListener('focus', evt => {
    divDeliveryAddress.style.display = 'block'
    inputsDeliveryAddress.forEach(el => {
        el.setAttribute("required", 'True')
    })
})