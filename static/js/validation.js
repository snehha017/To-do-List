
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function isValidUsername(username) {
    const usernameRegex = /^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{3,20}$/;
    return usernameRegex.test(username);
}

function isValidPassword(password) {
    return password.length >= 5 && password.length <= 20;
}

// SIGN UP
function validateSignupForm() {

    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirmPassword = document.getElementById("confirm_password").value;

    const usernameResult = document.getElementById("usrrslt");
    const emailResult = document.getElementById("emlrslt");
    const passwordResult = document.getElementById("pwdrslt");
    const confirmPasswordResult = document.getElementById("cnfpwdrslt");


    let isValid = true;
    //VALIDATE EMAIL
    emailResult.textContent = "";
    if (!isValidEmail(email)) {
        emailResult.textContent = "Invalid Email!";
        emailResult.style.color = "red";
        emailResult.style.fontSize = "15px";  
        isValid = false;
    } 

    //VALIDATE USERNAME
    usernameResult.textContent = "";
    if (!isValidUsername(username)) {
        usernameResult.textContent = "Invalid Username!";
        usernameResult.style.color = "red";
        usernameResult.style.fontSize = "15px";  
        isValid = false;
    }

    //VALIDATE PASSWORD
    passwordResult.textContent = "";
    if (!isValidPassword(password)) {
        passwordResult.textContent = "Invalid Password!";
        passwordResult.style.color = "red";
        passwordResult.style.fontSize = "15px";  
        isValid = false;
    } 

    //VALIDATE CONFIRM PASSWORD
    confirmPasswordResult.textContent = "";
    if (password !== confirmPassword) {
        confirmPasswordResult.textContent = "Passwords do not match!";
        confirmPasswordResult.style.color = "red";
        confirmPasswordResult.style.fontSize = "15px";
        isValid = false;
    }
    return isValid;
}

//LOGIN
function ValidateLogin(){
    const login_username = document.getElementById("login_username").value.trim();
    const login_password = document.getElementById("login_password").value.trim();

    const usernameResult = document.getElementById("login_usrrslt");
    const passwordResult = document.getElementById("login_pwdrslt");

    let isValid = True ;

    //VALIDATE USERNAME
    usernameResult.textContent = "";
    if (!/^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{3,20}$/.test(login_username)) {
    usernameResult.textContent = "Invalid Username!";
    usernameResult.style.color = "red";
    usernameResult.style.fontSize = "15px";  
    isValid = false;
    }

    //VALIDATE PASSWORD
    passwordResult.textContent = "";
    if (!(login_password.length >= 5 && login_password.length <= 20)) {
    passwordResult.textContent = "Invalid Password!";
    passwordResult.style.color = "red";
    passwordResult.style.fontSize = "15px";  
    isValid = false;
    } 
return isValid;
}