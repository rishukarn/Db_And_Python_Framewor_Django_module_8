
document.getElementById("doctorForm").addEventListener("submit", function (e) {
  e.preventDefault(); // prevent default form submission
  const name = document.getElementById("fullName").value.trim();
  const email = document.getElementById("email").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const date = document.getElementById("appointmentDate").value;
  const message = document.getElementById("message").value.trim();
  const feedback = document.getElementById("formMessage");

  // Simple validations
  if (name === "" || email === "" || phone === "" || date === "") {
    feedback.textContent = "Please fill in all required fields.";
    feedback.style.color = "red";
    return;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const phoneRegex = /^[0-9]{7,15}$/;

  if (!emailRegex.test(email)) {
    feedback.textContent = "Please enter a valid email address.";
    feedback.style.color = "red";
    return;
  }

  if (!phoneRegex.test(phone)) {
    feedback.textContent = "Please enter a valid phone number.";
    feedback.style.color = "red";
    return;
  }

  feedback.textContent = "Appointment booked successfully!";
  feedback.style.color = "green";

  // Optionally clear the form
  // e.target.reset();
});

