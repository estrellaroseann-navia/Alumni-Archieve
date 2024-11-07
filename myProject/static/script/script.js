const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

        function sendResetLink(event) {
            event.preventDefault(); // Prevent default form submission

            // Show the confirmation message
            document.getElementById('confirmation-message').style.display = 'block';

            // Hide the form after submission
            document.querySelector('.forgot-password-container form').style.display = 'none';
        }

        // Function to validate login
        function validateLogin() {
            const email = document.getElementById("login-email").value;
            const password = document.getElementById("login-password").value;

            if (email === "" || password === "") {
                alert("Please enter both email and password.");
                return;
            }

            // Simulate successful login and redirect to dashboard
            location.href = 'homepage.html';
        }

        // Function to handle registration (Placeholder)
        function register() {
            alert("Account created successfully!");
        }

        let slideIndex = 1;
        showSlides(slideIndex);
        
        // Function to change slides automatically
        function autoSlide() {
            showSlides(slideIndex += 1);
        }
        
        // Next/previous controls
        function plusSlides(n) {
            clearInterval(autoSlideInterval); // Stop automatic sliding when manual control is used
            showSlides(slideIndex += n);
        }
        
        // Display slides based on the index
        function showSlides(n) {
            let i;
            let slides = document.getElementsByClassName("slide");
            if (n > slides.length) { slideIndex = 1 } // Loop to the first slide
            if (n < 1) { slideIndex = slides.length } // Loop to the last slide
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none"; // Hide all slides
            }
            slides[slideIndex - 1].style.display = "block"; // Show the current slide
        }
        
        // Set up automatic slideshow
        const autoSlideInterval = setInterval(autoSlide, 5000); // Change slide every 5 seconds

        // landingpage container
        document.getElementById("container").classList.toggle("active");

        //survey
        document
          .getElementById("surveyForm")
          .addEventListener("submit", function (event) {
            event.preventDefault();

            const name = document.getElementById("name").value;
            const email = document.getElementById("email").value;
            const gradYear = document.getElementById("gradYear").value;
            const feedback = document.getElementById("feedback").value;

            if (name && email && gradYear && feedback) {
              document.getElementById("responseMessage").textContent =
                "Thank you for your feedback!";
              document.getElementById("surveyForm").reset();
            } else {
              document.getElementById("responseMessage").textContent =
                "Please fill out all fields.";
            }
          });


           