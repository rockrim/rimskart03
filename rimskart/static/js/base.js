    const loginForm = document.getElementById("login-form");
    const registerForm = document.getElementById("register-form");
    const indicator = document.getElementById("indicator");
    
    const loginTabBtn = document.getElementById("login-tab-btn");
    const registerTabBtn = document.getElementById("register-tab-btn");

    // Click behavior for the Register button
    registerTabBtn.onclick = function() {
        // Slide both forms 300 pixels to the left
        loginForm.style.transform = "translateX(-300px)";
        registerForm.style.transform = "translateX(-300px)";
        // Shift the orange line marker underneath the Register text label
        indicator.style.transform = "translateX(192px)";
    }

    // Click behavior for the Login button
    loginTabBtn.onclick = function() {
        // Return both forms back to their original zero positions
        loginForm.style.transform = "translateX(0px)";
        registerForm.style.transform = "translateX(25px)";
        // Shift the orange line marker back underneath the Login text label
        indicator.style.transform = "translateX(89px)";
    }