const form = document.querySelector(".needs-validation")
const phoneInput = document.getElementById("validationPhone")
const passwordInput = document.getElementById("validationPassword")

patterns = {
    phone_number: /^\+7\d{10}$/,
    password_reg: /^(?=.*[A-Z])(?=.*[a-z]).{8,}$/
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
     console.log(1)
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

form.addEventListener("submit", event =>{
    const isPhoneValid = validatePhone()
    const isPasswordValid = validatePassword()

    if (!isPhoneValid && !isPasswordValid)
     {
        event.preventDefault()
    }
})