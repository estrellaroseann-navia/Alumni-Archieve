// Function to toggle the dropdown menu for the profile
function toggleDropdown() {
    const dropdownMenu = document.getElementById("dropdown-menu");
    dropdownMenu.classList.toggle("show"); // Toggle the dropdown display
}

// Event listener for profile image click to toggle dropdown
document.getElementById('navbarProfileImg').addEventListener('click', toggleDropdown);

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.navbar-profile img')) {
        const dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show'); // Hide dropdown if clicked outside
            }
        }
    }
};
