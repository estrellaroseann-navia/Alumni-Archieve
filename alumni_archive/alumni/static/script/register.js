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

     if (clusterValue === 'main') {
         campusGroup.style.display = 'block';
         collegeGroup.style.display = 'block';
         campusSelect.innerHTML += '<option value="main">Puerto Princesa City</option>';
         collegeSelect.innerHTML += '<option value="cs">College of Sciences</option><option value="ceat">College of Engineering Architechture and Technology</option><option value="cah">College of Arts and Humanities</option><option value="cba">College of Business and Accountancy</option><option value="ccje">College of Criminal Justice Education</option><option value="cte">College of Teacher Education</option><option value="chtm">College of Nursing and Health Sciences</option><option value="ceat">College of Hospitality Management and Tourism</option><option value="graduate-school">College of PSU-Graduate School</option>';
     } else if (clusterValue === 'cluster1') {
         campusGroup.style.display = 'block';
         collegeGroup.style.display = 'block';
         campusSelect.innerHTML += '<option value="cluster1-campus1">ROXAS</option><option value="cluster1campus2">ARACELI</option><option value="cluster1campus3">DUMARAN</option><option value="clustercampus4">SAN VICENTE</option>';
         collegeSelect.innerHTML += '<option value="cs">College of Sciences</option><option value="ceat">College of Engineering Architechture and Technology</option><option value="cah">College of Arts and Humanities</option><option value="cba">College of Business and Accountancy</option><option value="ccje">College of Criminal Justice Education</option><option value="cte">College of Teacher Education</option><option value="chtm">College of Nursing and Health Sciences</option><option value="ceat">College of Hospitality Management and Tourism</option><option value="graduate-school">College of PSU-Graduate School</option>';
     } else if (clusterValue === 'cluster2') {
         campusGroup.style.display = 'block';
         collegeGroup.style.display = 'block';
         campusSelect.innerHTML += '<option value="cluster2campus1">TAYTAY</option><option value="cluster2campus2">EL NIDO</option><option value="cluster2campus3">NILAPACAN</option><option value="cluster2campus4">TCORON</option>';
         collegeSelect.innerHTML += '<option value="cs">College of Sciences</option><option value="ceat">College of Engineering Architechture and Technology</option><option value="cah">College of Arts and Humanities</option><option value="cba">College of Business and Accountancy</option><option value="ccje">College of Criminal Justice Education</option><option value="cte">College of Teacher Education</option><option value="chtm">College of Nursing and Health Sciences</option><option value="ceat">College of Hospitality Management and Tourism</option><option value="graduate-school">College of PSU-Graduate School</option>';
     } else if (clusterValue === 'cluster3') {
         campusGroup.style.display = 'block';
         collegeGroup.style.display = 'block';
         campusSelect.innerHTML += '<option value="cluster3campus1">NARRA</option><option value="cluster3campus2">QUEZON</option><option value="cluster3campus3">RIZAL</option>';
         collegeSelect.innerHTML += '<option value="cs">College of Sciences</option><option value="ceat">College of Engineering Architechture and Technology</option><option value="cah">College of Arts and Humanities</option><option value="cba">College of Business and Accountancy</option><option value="ccje">College of Criminal Justice Education</option><option value="cte">College of Teacher Education</option><option value="chtm">College of Nursing and Health Sciences</option><option value="ceat">College of Hospitality Management and Tourism</option><option value="graduate-school">College of PSU-Graduate School</option>';
     } else if (clusterValue === 'cluster4') {
         campusGroup.style.display = 'block';
         collegeGroup.style.display = 'block';
         campusSelect.innerHTML += '<option value="cluster4campus1">ESPANOLA</option><option value="cluster4campus2">BROOKES POINT</option><option value="cluster4campus3">ESPANOLA</option><option value="cluster4campus4">BATARAZA</option>';
         collegeSelect.innerHTML += '<option value="cs">College of Sciences</option><option value="ceat">College of Engineering Architechture and Technology</option><option value="cah">College of Arts and Humanities</option><option value="cba">College of Business and Accountancy</option><option value="ccje">College of Criminal Justice Education</option><option value="cte">College of Teacher Education</option><option value="chtm">College of Nursing and Health Sciences</option><option value="ceat">College of Hospitality Management and Tourism</option><option value="graduate-school">College of PSU-Graduate School</option>';
     } else if (clusterValue === 'cuyo') {
        campusGroup.style.display = 'block';
        collegeGroup.style.display = 'block';
        campusSelect.innerHTML += '<option value="cuyocampus1">CUYO</option>';
        collegeSelect.innerHTML += '<option value="cs">College of Sciences</option><option value="ceat">College of Engineering Architechture and Technology</option><option value="cah">College of Arts and Humanities</option><option value="cba">College of Business and Accountancy</option><option value="ccje">College of Criminal Justice Education</option><option value="cte">College of Teacher Education</option><option value="chtm">College of Nursing and Health Sciences</option><option value="ceat">College of Hospitality Management and Tourism</option><option value="graduate-school">College of PSU-Graduate School</option>';
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
         programSelect.innerHTML += '<option value="archi">Bachelor of Science in Architecture</option><option value="civil">Bachelor of Science in Civil Engineering</option><option value="elect">Bachelor of Science in Electrical Engineering</option><option value="peteng">Bachelor of Science in Petroleum Engineering</option>';
     } else if (collegeValue === 'cah') {
         programGroup.style.display = 'block';
         programSelect.innerHTML += '<option value="com">Bachelor of Arts in Communication</option><option value="polsci">Bachelor of Arts in Political Science</option><option value="solwork">Bachelor of Arts in Social Work</option><option value="psych">Bachelor of Arts in Psychology </option>';
     } else if (collegeValue === 'cba') {
         programGroup.style.display = 'block';
         programSelect.innerHTML += '<option value="accountancy">Bachelor of Science in Accountancy</option><option value="manaccount">Bachelor of Science in Management Accounting</option><option value="bus-add">Bachelor of Science in Business Administration</option><option value="entrep">Bachelor of Science in Entreprenuership</option><option value="fm">Bachelor of Science in Financial Management</option>';
     } else if (collegeValue === 'ccje') {
         programGroup.style.display = 'block';
         programSelect.innerHTML += '<option value="crim">Bachelor of Science in Crinimology</option><option value="program10">Program 10</option>';
     } else if (collegeValue === 'cte') {
         programGroup.style.display = 'block';
         programSelect.innerHTML += '<option value="bee">Bachelor of Elementary Education</option><option value="bse">Bachelor of Secondary Education</option><option value="bpe">Bachelor of Physical Education</option>';
     } else if (collegeValue === 'cnhs') {
        programGroup.style.display = 'block';
        programSelect.innerHTML += '<option value="bsn">Bachelor of Science in Nursing</option><option value="bsm">Bachelor of Science in Midwifery</option><option value="diploma">Diploma in Midwifery</option>';
     } else if (collegeValue === 'chtm') {
        programGroup.style.display = 'block';
        programSelect.innerHTML += '<option value="hm">Bachelor of Science in Hositality Management</option><option value="btm">Bachelor of Science in Tourism Management</option><option value="diploma">Diploma in Midwifery</option>';
     } else if (collegeValue === 'graduate-school') {
        programGroup.style.display = 'block';
        programSelect.innerHTML += '<option value="de">Doctor of Education</option><option value="msa">Master of Business Administration</option><option value="mst">Master of Science in Technopreneurship</option><option value="mat">Master of Arts in Teaching</option><option value="msem">Master of Science in Environmental Management</option><option value="mpa">Master in Public Administration</option><option value="msn">Master of Science in Nursing</option>';
     }
 });

 /// Form submit event
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