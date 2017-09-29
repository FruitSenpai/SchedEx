$(function() {

    // Set enter key to activate the login button
    $(document).keypress(function(e) {
        if (e.which === 13){
            $("#login_button").click();
        }
    });

});
