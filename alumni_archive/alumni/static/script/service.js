// Object containing college-program pairs
const collegePrograms = {
    "College of Science": ["Bachelor of Science in Biology", "Bachelor of Science in Marine Biology", "Bachelor of Science in Computer Science", "Bachelor of Science in Environmental Science", "Bachelor of Science in Information Technology"],
    "College of Engineering Architecture and Technology": ["Bachelor of Science in Architecture", "Bachelor of Science in Civil Engineering", "Bachelor of Science in Electrical Engineering", "Bachelor of Science in Mechanical Engineering", "Bachelor of Science in Petroleum Engineering"],
    "College of Arts and Humanities": ["Bachelor of Arts in Communication", "Bachelor of Arts in Political Science", "Bachelor of Arts in Philippine Studies", "Bachelor of Science in Social Work", "Bachelor of Science in Psychology"],
    "College of Business and Accountancy": ["Bachelor of Science in Accountancy", "Bachelor of Science in Management Accounting", "Bachelor of Science in Business Administration", "Bachelor of Science in Entrepreneurship"],
    "College of Criminal Justice Education": ["Bachelor of Science in Criminology"],
    "College of Teacher Education": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Physical Education"],
    "College of Nursing and Health Sciences": ["Bachelor of Science in Nursing", "Bachelor of Science in Midwifery", "Diploma in Midwifery"],
    "College of Hospitality Management and Tourism": ["Bachelor of Science in Hospitality Management", "Bachelor of Science in Tourism Management"],
    "Graduate School": ['Doctor of Education', 'Master in Business Administration', 'Master of Science in Technopreneurship', 
        'Master of Arts in Teaching', 'Master of Science in Environmental Management', 'Master in Public Administration', 'Diploma in Teaching', 'Master of Science in Nursing']
};

// Object containing cluster-campuses pairs
const campusesByCluster = {
    'Main': ['PUERTO PRINCESA CITY'],
    'Cluster 1': ['ROXAS', 'ARACELI', 'DUMARAN', 'SAN VICENTE'],
    'Cluster 2': ['TAYTAY', 'EL NIDO', 'LINAPACAN', 'CORON'],
    'Cluster 3': ['NARRA', 'QUEZON', 'RIZAL'],
    'Cluster 4': ['ESPAÑOLA', 'BROOKES POINT', 'BATARAZA','BATARAZA'],
    'PCAT Cuyo': ['Cuyo']
    // Add more clusters and campuses as needed
};

// Object containing campus-program pairs for specific campuses
const programsByCampus = {
    'PUERTO PRINCESA CITY': [], // Programs for this campus will be handled in the updatePrograms function
    'ROXAS': ["Bachelor of Science in Criminology", "Bachelor of Science in Business Administration",
        'Bachelor of Science in Hospitality Management', 'Bachelor of Science in Computer Science',
        'Bachelor of Elementary Education', 'Bachelor of Secondary Education'
    ],

    'ARACELI': ["Bachelor of Science in Business Administration", "Bachelor of Science in Entrepreneurship"],

    'DUMARAN': ["Bachelor of Science in Entrepreneurship", "Bachelor of Science in Agriculture"],

    'SAN VICENTE': ["Bachelor of Arts in Political Science", "Bachelor of Science in Entrepreneurship",
        'Bachelor of Science in Tourism Management', 'Bachelor of Science in Environmental Science',
        'Bachelor of Science in Computer Science'
    ],

    'TAYTAY': ["Bachelor of Science in Business Administration", "Bachelor of Science in Hospitality Management",
        'Bachelor of Science in Information Technology'
    ],

    'EL NIDO': ["BBachelor of Science in Entrepreneurship", "Bachelor of Science in Hospitality Management",
        'Bachelor of Science in Tourism Management'
    ],

    'LINAPACAN': ["Bachelor of Science in Tourism Management", "Bachelor of Science in Fisheries"],

    'CORON': ["Bachelor of Science in Criminologyt", "Bachelor of Science in Business Administration", 
        'Bachelor of Science in Hospitality Management', 'Bachelor of Science in Tourism Management', 'Bachelor of Elementary Education',
        'Bachelor of Secondary Education'
    ],

    'NARRA': ["Bachelor of Arts in Political Science", "Bachelor of Science in Criminology",
        "Bachelor of Science in Business Administration", 'Bachelor of Science in Entrepreneurship', 'Bachelor of Science in Hospitality Management',
        'Bachelor of Science in Tourism Management', 'Bachelor of Science in Agriculture', 'Bachelor of Science in Computer Science', 'Bachelor of Elementary Education'
    ],

    'QUEZON': ["Bachelor of Science in Business Administration", "Track 2-Agri-business", 'Bachelor of Science in Hospitality Management',
        'Bachelor of Science in Agriculture', 'Bachelor of Science in Information Technology', 'Bachelor of Elementary Education', 'Bachelor of Secondary Education'
    ],

    'RIZAL': ["Bachelor of Science in Entrepreneurship", "Bachelor of Science in Agriculture",
        'Bachelor of Science in Computer Science', 'Bachelor of Science in Environmental Science'],

    'ESPAÑOLA':['Financial Management', 'Bachelor of Science in Entrepreneurship', 'Bachelor of Science in Agriculture',
        'Bachelor of Elementary Education'
    ],

    'BROOKES POINT': ['Bachelor of Science in Criminology', 'Bachelor of Science in Business Administration',
        'Bachelor of Science in Hospitality Management', 'Bachelor of Science in Agriculture', 'Bachelor of Science in Information Technology',
        'Bachelor of Elementary Education', 'Bachelor of Secondary Education English'],

    'BATARAZA': ['Bachelor of Science in Business Administration', 'Bachelor of Science in Agriculture',
        'Bachelor of Science in Information Technology', 'Bachelor of Elementary Education'],

    'BALABAC': ['Bachelor of Science in Entrepreneurship', 'Bachelor of Science in Agriculture'],

    'Cuyo': ["Bachelor of Arts in Political Science", "Bachelor of Industrial Technology", "Marine Engineering Technology",
        "Bachelor of Science in Criminology", "Bachelor of Science in Business Administration", "Bachelor of Science in Hospitality Management",
        "Bachelor of Science in Tourism Management", "Bachelor of Elementary Education", "Bachelor of Secondary Education","Bachelor of Technical-Vocational Teacher Education"
    ]
    // Add more campuses and programs as needed
};

// Function to update campuses based on selected cluster
function updateCampuses() {
    // Get selected cluster
    const clusterSelect = document.getElementById('cluster');
    const selectedCluster = clusterSelect.value;

    // Get the campuses select element
    const campusesSelect = document.getElementById('campuses');

    // Clear existing options
    campusesSelect.innerHTML = '<option value="" disabled selected>Select a Campus</option>';

    // Populate new options based on selected cluster
    if (selectedCluster && campusesByCluster[selectedCluster]) {
        campusesByCluster[selectedCluster].forEach(campus => {
            const option = document.createElement('option');
            option.value = campus;
            option.textContent = campus;
            campusesSelect.appendChild(option);
        });
    }

    // Reset program dropdown when cluster changes
    resetProgram();
}

// Function to update the Program dropdown based on the selected College and Campus
function updatePrograms() {
    // Get selected college
    const collegeSelect = document.getElementById('college');
    const selectedCollege = collegeSelect.value;

    // Get selected campus
    const campusSelect = document.getElementById('campuses');
    const selectedCampus = campusSelect.value;

    // Get the program select element
    const programSelect = document.getElementById('program');

    // Clear existing options
    programSelect.innerHTML = '<option value="" disabled selected>Select a Program</option>';

    // Check if PUERTO PRINCESA CITY is selected
    if (selectedCampus === 'PUERTO PRINCESA CITY') {
        // Populate programs from collegePrograms based on selected college only
        if (selectedCollege && collegePrograms[selectedCollege]) {
            collegePrograms[selectedCollege].forEach(program => {
                const option = document.createElement('option');
                option.value = program;
                option.textContent = program;
                programSelect.appendChild(option);
            });
        }
    } else {
        // Populate programs based on selected campus
        if (selectedCampus && programsByCampus[selectedCampus]) {
            programsByCampus[selectedCampus].forEach(program => {
                const option = document.createElement('option');
                option.value = program;
                option.textContent = program;
                programSelect.appendChild(option);
            });
        }
    }
}

// Function to reset Program dropdown
function resetProgram() {
    const programSelect = document.getElementById('program');
    programSelect.innerHTML = '<option value="" disabled selected>Select a Program</option>';
}

// Event listeners for select elements
document.getElementById('cluster').addEventListener('change', updateCampuses);
document.getElementById('college').addEventListener('change', updatePrograms);
document.getElementById('campuses').addEventListener('change', updatePrograms);

// Function to toggle profile dropdown menu visibility
function toggleProfileDropdown() {
    const profileDropdown = document.getElementById('profile-dropdown');
    profileDropdown.style.display = profileDropdown.style.display === 'block' ? 'none' : 'block';
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.profile-icon')) {
        const dropdowns = document.getElementsByClassName("profile-dropdown");
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.style.display === 'block') {
                openDropdown.style.display = 'none';
            }
        }
    }
};
