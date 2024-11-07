// You can add functionality here if needed
document.querySelector('.yes-btn').addEventListener('click', function() {
    // Logic to log out the user
    alert('You have been logged out successfully.');
    // Redirect to login page or homepage after logout
    window.location.href = 'login.html'; // Adjust the redirect URL as needed
});

document.querySelector('.no-btn').addEventListener('click', function() {
    // Close the confirmation dialog or redirect back to the previous page
    window.history.back(); // Go back to the previous page
});
