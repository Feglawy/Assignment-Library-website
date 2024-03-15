function ShowPassword() {
  var passwordBox = document.getElementById("inp-pass");
  var iconBox = document.getElementById("visibility");
  if (passwordBox.type === "password") {
    passwordBox.type = "text";
    iconBox.innerHTML = "visibility_off";
  } else {
    passwordBox.type = "password";
    iconBox.innerHTML = "visibility";
  }
}
