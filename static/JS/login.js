function ShowPassword() {
  var passwordBox = document.getElementById("inp-pass");
  var confirmPasswordBox = document.getElementById("confirm-inp-pass");
  var iconBox = document.getElementById("visibility");

  if (passwordBox.type === "password") {
    // change icon
    iconBox.classList.remove("fa-eye");
    iconBox.classList.add("fa-eye-slash");

    // show password
    passwordBox.type = "text";
    confirmPasswordBox.type = "text";
  } else {
    // change icon
    iconBox.classList.remove("fa-eye-slash");
    iconBox.classList.add("fa-eye");

    // show password
    passwordBox.type = "password";
    confirmPasswordBox.type = "password";
  }
}