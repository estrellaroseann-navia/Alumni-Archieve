document.addEventListener("DOMContentLoaded", function () {
    const getStartedButton = document.querySelector(".get-started-btn");

    getStartedButton.addEventListener("click", function (event) {
        event.preventDefault(); 

        window.location.href = "login.html"; 
    });
});