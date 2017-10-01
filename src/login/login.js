$(function() {

    document.addEventListener("keydown", keydown, false);

});

// Set enter key to activate the login button
function keydown(e) {
    var $button = $("#login_button");
    if (e.which === 13){
        $button.click();
    }
}

// Validation for demo credentials
function login() {
    var $email = $("#login_email").val();
    var $password = $("#login_password").val();
    console.log($email + ", " + $password)
    if ( ($email === "student@uni.ac.za") && ($password === "student") )
        window.location.href = "../generic/generic.html";
    else if ( ($email === "coordinator@uni.ac.za") && ($password === "coordinator") )
        window.location.href = "../coordinator/coordinator.html";
    else if ( ($email === "admin@uni.ac.za") && ($password === "admin") )
        window.location.href = "../admin/admin.html";
    else {
        var snackbarContainer = document.querySelector('#snackbar');
        var data = {message: 'Incorrect email or password'};
        snackbarContainer.MaterialSnackbar.showSnackbar(data);
    }
}
