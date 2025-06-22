document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');
    
    form.addEventListener('submit', function(event) {
        // Clear previous error messages
        clearErrors();
        
        // Validate fields
        const isValidName = validateName();
        const isValidEmail = validateEmail();
        const isValidPhone = validatePhone();
        const isValidPassword = validatePassword();
        const isValidConfirmPassword = validateConfirmPassword();
        
        // If any validation fails, prevent form submission
        if (!isValidName || !isValidEmail || !isValidPhone || !isValidPassword || !isValidConfirmPassword) {
            event.preventDefault();
        }
    });
    
    function validateName() {
        const nameInput = document.getElementById('id_name');
        const nameError = document.getElementById('nameError');
        
        if (nameInput.value.trim() === '') {
            nameError.textContent = 'Name is required';
            return false;
        }
        
        return true;
    }
    
    function validateEmail() {
        const emailInput = document.getElementById('id_email');
        const emailError = document.getElementById('emailError');
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        if (emailInput.value.trim() === '') {
            emailError.textContent = 'Email is required';
            return false;
        }
        
        if (!emailRegex.test(emailInput.value)) {
            emailError.textContent = 'Please enter a valid email address';
            return false;
        }
        
        return true;
    }
    
    function validatePhone() {
        const phoneInput = document.getElementById('id_phone_number');
        const phoneError = document.getElementById('phoneError');
        const phoneRegex = /^\+?1?\d{9,15}$/;
        
        if (phoneInput.value.trim() === '') {
            phoneError.textContent = 'Phone number is required';
            return false;
        }
        
        if (!phoneRegex.test(phoneInput.value)) {
            phoneError.textContent = 'Please enter a valid phone number (e.g., +1234567890)';
            return false;
        }
        
        return true;
    }
    
    function validatePassword() {
        const passwordInput = document.getElementById('id_password');
        const passwordError = document.getElementById('passwordError');
        
        if (passwordInput.value.trim() === '') {
            passwordError.textContent = 'Password is required';
            return false;
        }
        
        if (passwordInput.value.length < 8) {
            passwordError.textContent = 'Password must be at least 8 characters';
            return false;
        }
        
        return true;
    }
    
    function validateConfirmPassword() {
        const passwordInput = document.getElementById('id_password');
        const confirmPasswordInput = document.getElementById('id_confirm_password');
        const confirmPasswordError = document.getElementById('confirmPasswordError');
        
        if (confirmPasswordInput.value.trim() === '') {
            confirmPasswordError.textContent = 'Please confirm your password';
            return false;
        }
        
        if (passwordInput.value !== confirmPasswordInput.value) {
            confirmPasswordError.textContent = 'Passwords do not match';
            return false;
        }
        
        return true;
    }
    
    function clearErrors() {
        const errorElements = document.querySelectorAll('.error');
        errorElements.forEach(element => {
            element.textContent = '';
        });
    }
    
    // Add real-time validation on blur
    document.getElementById('id_email').addEventListener('blur', validateEmail);
    document.getElementById('id_phone_number').addEventListener('blur', validatePhone);
    document.getElementById('id_password').addEventListener('blur', validatePassword);
    document.getElementById('id_confirm_password').addEventListener('blur', validateConfirmPassword);
});