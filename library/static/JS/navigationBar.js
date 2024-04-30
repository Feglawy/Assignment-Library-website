document.body.classList.toggle("white-theme");

// change menu icon
function ToggleMenu() {
  let menuIcon = document.getElementById("menu");
  if (menuIcon.classList.contains("fa-bars")) {
    menuIcon.classList.remove("fa-bars");
    menuIcon.classList.add("fa-xmark");
  } else {
    menuIcon.classList.remove("fa-xmark");
    menuIcon.classList.add("fa-bars");
  }
}

// as soon as the window load it will do this function
document.addEventListener("DOMContentLoaded", function () {
  // --------- get the avtive page and add .active class to it ------------
  const navbarElements = document.querySelectorAll(".pages");

  // Get the current URL path without query parameters
  const currentPath = window.location.pathname;

  // Loop over each navbar element
  navbarElements.forEach(function (navbar) {
    // Find all <a> tags within the current navbar element
    const navLinks = navbar.querySelectorAll("a");

    // Add 'active' class to the link whose URL matches the current path
    navLinks.forEach(function (link) {
      const linkPath = new URL(link.href).pathname;
      if (linkPath === currentPath) {
        link.classList.add("active");
      }
    });
  });
});
