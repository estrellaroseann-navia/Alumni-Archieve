// Slideshow Script
let slideIndex = 0; // Initialize slide index
showSlides(slideIndex); // Show the first slide

// Function to show slides
function showSlides(n) {
    const slides = document.getElementsByClassName("slide");
    if (n >= slides.length) {
        slideIndex = 0; // Reset to first slide if out of bounds
    }
    if (n < 0) {
        slideIndex = slides.length - 1; // Loop back to last slide
    }
    
    // Hide all slides
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
    }
    
    // Show the current slide
    slides[slideIndex].style.display = "block"; 
}

// Function to change slide
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Automatic slideshow
setInterval(function() {
    plusSlides(1); // Change slide every 3 seconds
}, 3000);

// Profile Dropdown Script
document.addEventListener("DOMContentLoaded", function() {
    const profileIcon = document.getElementById("navbarProfileImg");
    const dropdownMenu = document.getElementById("dropdown-menu");

    // Toggle dropdown on profile icon click
    profileIcon.addEventListener("click", function() {
        dropdownMenu.classList.toggle("show");
    });

    // Close the dropdown if the user clicks outside of it
    window.addEventListener("click", function(event) {
        if (!profileIcon.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.remove("show");
        }
    });
});
