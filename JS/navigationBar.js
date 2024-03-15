function ToggleMenu() {
  var menuBox = document.getElementById("menu");
  if (menuBox.innerHTML === "menu") {
    menuBox.innerHTML = "close";
  } else {
    menuBox.innerHTML = "menu";
  }
}
