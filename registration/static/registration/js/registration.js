const form = document.querySelector(".needs-validation")
const phoneInput = document.getElementById("validationPhone")
const passwordInput = document.getElementById("validationPassword")
const nameInput = document.getElementById("validationName")
const familyInput = document.getElementById("validationFamily")
const passwordSecondInput = document.getElementById("validationPasswordSecond")

patterns = {
    phone_number: /^\+7\d{10}$/,
    password_reg: /^(?=.*[A-Z])(?=.*[a-z]).{8,}$/,
    name_reg: /^[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?$/,

}

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

function validatePassword()
{

     password = passwordInput.value

    if (patterns["password_reg"].test(password))
    {
        passwordInput.classList.add("is-valid")
        passwordInput.classList.remove("is-invalid")
        return true
    }
    else
    {
        passwordInput.classList.add("is-invalid")
        passwordInput.classList.remove("is-valid")
        return false
    }


}

passwordInput.addEventListener("input", validatePassword)

function validatePasswordSecond()
{

    password1 = passwordInput.value
    password2 = passwordSecondInput.value

    if (patterns["password_reg"].test(password2) && password1 == password2)
    {
        passwordSecondInput.classList.add("is-valid")
        passwordSecondInput.classList.remove("is-invalid")
        return true
    }
    else
    {
        passwordSecondInput.classList.add("is-invalid")
        passwordSecondInput.classList.remove("is-valid")
        return false
    }


}

passwordSecondInput.addEventListener("input", validatePasswordSecond)

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
    const isPasswordValid = validatePassword()
    const isnameValid = validateName()
    const isfamilyValid = validateFamily()
    const ispasswordSecondValid = validatePasswordSecond()

    if (!isPhoneValid || !isPasswordValid || !isnameValid || !isfamilyValid || !ispasswordSecondValid || !form.checkValidity)
    {
        event.preventDefault()
    }
})