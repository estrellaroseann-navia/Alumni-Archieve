document.addEventListener("DOMContentLoaded", function () {
    // Select the "Get Started" button
    const getStartedButton = document.querySelector(".get-started-btn");

    // Add a click event listener to the button
    getStartedButton.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent default anchor behavior

        // Redirect to the admin login page
        window.location.href = "login.html"; // Change to your actual admin login page URL
    });
});
