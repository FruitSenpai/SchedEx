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
        window.location.replace("../home/home.html");
    });

    // Set enter key to activate the button
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