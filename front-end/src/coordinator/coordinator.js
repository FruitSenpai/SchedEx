$(function() {

    // Short hack used to override tooltip visibility
    var $search_bar = $("#search_bar");
    $search_bar.click(function(e) {
        $("#search_tooltip").hide();
    });
    $search_bar.hover(function(e) {
        $("#search_tooltip").show();
    });

    // Logout functionality
    $("#logout").click(function(e) {
        window.location.replace("../login/login.html");
    });

        $("#map").attr('src', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3580.2021587339887!2d28.024300815029793!3d-26.190101283444104!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1e950c0f6a2900bb%3A0x5f0efcdd3b0d0c18!2sMathematical+Sciences+Building!5e0!3m2!1sen!2sza!4v1506790996161");

    // Set enter key to activate the course button
    $(document).keypress(function(e) {
        if (e.which === 13){
            $("#button").click();
        }
    });

    // Snackbar appearance on button click
    (function() {
        var snackbarContainer = document.querySelector('#snackbar');
        var showToastButton = document.querySelector('#button');
        showToastButton.addEventListener('click', function() {
            var data = {message: 'Saved'};
            snackbarContainer.MaterialSnackbar.showSnackbar(data);
        });
    }());

});