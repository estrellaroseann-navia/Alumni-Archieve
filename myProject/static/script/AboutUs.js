// Get the profile dropdown and profile image elements
const profileImg = document.getElementById('navbarProfileImg');
const dropdownMenu = document.getElementById('dropdown-menu');

// Function to toggle the dropdown menu visibility
function toggleDropdown() {
    dropdownMenu.classList.toggle('show');
}

// Add event listener to the profile image to toggle the dropdown menu on click
profileImg.addEventListener('click', toggleDropdown);

// Close the dropdown menu if the user clicks outside of it
window.addEventListener('click', function(event) {
    if (!event.target.matches('#navbarProfileImg')) {
        if (dropdownMenu.classList.contains('show')) {
            dropdownMenu.classList.remove('show');
        }
    }
});
