 // Access DOM elements
 const emailInput = document.getElementById('email');
 const passwordInput = document.getElementById('password');
 const confirmPasswordInput = document.getElementById('confirm-password');
 const checkbox = document.getElementById('terms-accepted');
 const submitBtn = document.getElementById('submit-btn');
 const clusterSelect = document.getElementById('cluster');
 const campusSelect = document.getElementById('campus');
 const collegeSelect = document.getElementById('college');
 const programSelect = document.getElementById('school-program');
 const campusGroup = document.getElementById('campus-group');
 const collegeGroup = document.getElementById('college-group');
 const programGroup = document.getElementById('school-program-group');

 // Function to validate the form and toggle the button
 function validateForm() {
     const isEmailFilled = emailInput.value.trim() !== '';
     const isPasswordFilled = passwordInput.value.trim() !== '';
     const isConfirmPasswordFilled = confirmPasswordInput.value.trim() !== '';
     const isCheckboxChecked = checkbox.checked;

     submitBtn.disabled = !(isEmailFilled && isPasswordFilled && isConfirmPasswordFilled && isCheckboxChecked);
 }

 // Function to check field validation and toggle error messages
 function checkFields() {
     const isPasswordMatch = passwordInput.value === confirmPasswordInput.value;
     document.getElementById('email-error').style.display = emailInput.value.trim() === '' ? 'block' : 'none';
     document.getElementById('password-error').style.display = passwordInput.value.trim() === '' ? 'block' : 'none';
     document.getElementById('confirm-password-error').style.display = confirmPasswordInput.value.trim() === '' ? 'block' : 'none';
     document.getElementById('mismatch-error').style.display = isPasswordMatch ? 'none' : 'block';
 }

 // Event listeners for input changes and checkbox
 emailInput.addEventListener('input', function() {
     validateForm();
     checkFields();
 });

 passwordInput.addEventListener('input', function() {
     validateForm();
     checkFields();
 });

 confirmPasswordInput.addEventListener('input', function() {
     validateForm();
     checkFields();
 });

 checkbox.addEventListener('change', function() {
     validateForm();
 });

 // Function to reset and populate options for campus, college, and program
 function updateOptions(clusterValue) {
     // Hide and reset campus, college, and program options
     campusGroup.style.display = 'none';
     collegeGroup.style.display = 'none';
     programGroup.style.display = 'none';
     campusSelect.innerHTML = '<option value="">Select Campus</option>';
     collegeSelect.innerHTML = '<option value="">Select College</option>';
     programSelect.innerHTML = '<option value="">Select Program</option>';

     if (clusterValue === 'main-campus') {
         campusGroup.style.display = 'block';
         campusSelect.innerHTML += '<option value="main">Puerto Princesa City</option>';
         collegeGroup.style.display = 'block';
         collegeSelect.innerHTML += '<option value="cs">College of Sciences</option><option value="ceat">College of Engineering</option>';
     } else if (clusterValue === 'cluster1') {
         campusGroup.style.display = 'block';
         campusSelect.innerHTML += '<option value="campus1">vjosvjsdj 1</option><option value="campus2">Campus 2</option>';
         collegeGroup.style.display = 'block';
         collegeSelect.innerHTML += '<option value="college1">College 1</option><option value="college2">College 2</option>';
     } else if (clusterValue === 'cluster2') {
         campusGroup.style.display = 'block';
         campusSelect.innerHTML += '<option value="campus3">Campus 3</option>';
         collegeGroup.style.display = 'block';
         collegeSelect.innerHTML += '<option value="college3">College 3</option>';
     } else if (clusterValue === 'cluster3') {
         campusGroup.style.display = 'block';
         campusSelect.innerHTML += '<option value="campus4">Campus 4</option>';
         collegeGroup.style.display = 'block';
         collegeSelect.innerHTML += '<option value="college4">College 4</option>';
     } else if (clusterValue === 'cluster4' || clusterValue === 'Cuyo') {
         campusGroup.style.display = 'block';
         campusSelect.innerHTML += '<option value="campus4">Campus 4</option>';
         collegeGroup.style.display = 'block';
         collegeSelect.innerHTML += '<option value="college4">College 4</option>';
     }
 }

 // Cluster change listener to populate campus, college, and program
 clusterSelect.addEventListener('change', function() {
     const clusterValue = clusterSelect.value;
     updateOptions(clusterValue);
 });

 // College change listener to update program options
 collegeSelect.addEventListener('change', function() {
     const collegeValue = collegeSelect.value;
     programGroup.style.display = 'none';
     programSelect.innerHTML = '<option value="">Select Program</option>';

     if (collegeValue === 'cs') {
         programGroup.style.display = 'block';
         programSelect.innerHTML += '<option value="bio">Bachelor of Science in Biology</option><option value="marbio">Bachelor of Science in Marine Biology</option><option value="comsci">Bachelor of Science in Computer Science</option><option value="envisci">Bachelor of Science in Environmental Science</option><option value="it">Bachelor of Science in Information Technology</option>';
     } else if (collegeValue === 'ceat') {
         programGroup.style.display = 'block';
         programSelect.innerHTML += '<option value="archi">Bachelor of Science in Architecture</option><option value="civil">Bachelor of Science in Civil Engineering</option>';
     } else if (collegeValue === 'college1') {
         programGroup.style.display = 'block';
         programSelect.innerHTML += '<option value="program5">Program 5</option><option value="program6">Program 6</option>';
     } else if (collegeValue === 'college2') {
         programGroup.style.display = 'block';
         programSelect.innerHTML += '<option value="program7">Program 7</option><option value="program8">Program 8</option>';
     } else if (collegeValue === 'college3') {
         programGroup.style.display = 'block';
         programSelect.innerHTML += '<option value="program9">Program 9</option><option value="program10">Program 10</option>';
     } else if (collegeValue === 'college4') {
         programGroup.style.display = 'block';
         programSelect.innerHTML += '<option value="program11">Program 11</option><option value="program12">Program 12</option>';
     }
 });

 // Form submit event
 document.getElementById('signup-form').addEventListener('submit', function(event) {
     event.preventDefault(); // Prevent default form submission

     // Redirect to UserLogIn.html after successful validation
     if (passwordInput.value === confirmPasswordInput.value) {
         // You can save data or perform any actions here if needed
         window.location.href = 'UserLogIn.html'; // Redirect to the UserLogIn page
     } else {
         alert("Please ensure that all fields are filled correctly and passwords match.");
     }
 });