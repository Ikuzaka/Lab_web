const form = document.querySelector(".needs-validation")
const phoneInput = document.getElementById("validationPhone")
const nameInput = document.getElementById("validationName")
const familyInput = document.getElementById("validationFamily")
const TextInput = document.getElementById("validationText")

patterns = {
    phone_number: /^\+7\d{10}$/,
    password_reg: /^(?=.*[A-Z])(?=.*[a-z]).{8,}$/,
    name_reg: /^[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?$/,

}

function validateText() {

    Text = TextInput.value;
    if (Text.length === 0) {
        TextInput.classList.add('is-invalid');
        TextInput.classList.remove('is-valid');
        return false;
    } else if (Text.length < 10) {
        TextInput.classList.add('is-invalid');
        TextInput.classList.remove('is-valid');
        return false;
    } else {
        TextInput.classList.remove('is-invalid');
        TextInput.classList.add('is-valid');
        return true;
    }
}
TextInput.addEventListener("input", validateText)

function validatePhone()
{

    phone = phoneInput.value

    if (patterns["phone_number"].test(phone))
    {
        phoneInput.classList.add("is-valid")
        phoneInput.classList.remove("is-invalid")
        return true
    }
    else
    {
        phoneInput.classList.add("is-invalid")
        phoneInput.classList.remove("is-valid")
        return false
    }
}

phoneInput.addEventListener("input", validatePhone)


function validateName()
{

     name = nameInput.value

    if (patterns["name_reg"].test(name))
    {
        nameInput.classList.add("is-valid")
        nameInput.classList.remove("is-invalid")
        return true
    }
    else
    {
        nameInput.classList.add("is-invalid")
        nameInput.classList.remove("is-valid")
        return false
    }


}

nameInput.addEventListener("input", validateName)

function validateFamily()
{

     family = familyInput.value

    if (patterns["name_reg"].test(family))
    {
        familyInput.classList.add("is-valid")
        familyInput.classList.remove("is-invalid")
        return true
    }
    else
    {
        familyInput.classList.add("is-invalid")
        familyInput.classList.remove("is-valid")
        return false
    }


}

familyInput.addEventListener("input", validateFamily)

form.addEventListener("submit", event =>{
    const isPhoneValid = validatePhone()
    const isnameValid = validateName()
    const isfamilyValid = validateFamily()
    const istextValid = validateText()


    if (!isPhoneValid || !isnameValid || !isfamilyValid || !form.checkValidity || !istextValid)
    {
        event.preventDefault()
    }
})