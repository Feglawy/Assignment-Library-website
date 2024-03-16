function ShowPassword() {
  var passwordBox = document.getElementById("inp-pass");
  var confirmPasswordBox = document.getElementById("confirm-inp-pass");
  var iconBox = document.getElementById("visibility");
  if (passwordBox.type === "password") {
    passwordBox.type = "text";
    confirmPasswordBox.type = "text";
    iconBox.innerHTML = "visibility_off";
  } else {
    passwordBox.type = "password";
    confirmPasswordBox.type = "password";
    iconBox.innerHTML = "visibility";
  }
}
