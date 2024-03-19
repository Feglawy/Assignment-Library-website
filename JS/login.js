function ShowPassword() {
  var passwordBox = document.getElementById("inp-pass");
  var confirmPasswordBox = document.getElementById("confirm-inp-pass");
  var iconBox = document.getElementById("visibility");
  if (passwordBox.type === "password") {
    passwordBox.type = "text";
    iconBox.innerHTML = "visibility_off";
    confirmPasswordBox.type = "text";
  } else {
    passwordBox.type = "password";
    iconBox.innerHTML = "visibility";
    confirmPasswordBox.type = "password";
  }
}
