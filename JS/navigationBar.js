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

// add the navigation bar dynamicaly with js
document.addEventListener("DOMContentLoaded", function () {
  // the HTML content for the navigation bar
  const navbarHtml = `
      <!-- page icon -->
      <link
        rel="shortcut icon"
        href="/Images/icons/storytelling.ico"
        type="image/x-icon"
      />
      <!-- Font awsome icons -->
      <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"
        integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A=="
        crossorigin="anonymous"
        referrerpolicy="no-referrer"
      />
      <!-- navigation bar -->
      <!-- logo -->
      <a href="/" class="logo">
        <img src="/Images/icons/storytelling.ico" width="40" height="40" />
        <span id="website-name">Library</span>
      </a>
      <!-- Pages -->
      <nav>
        <!-- menu button -->
        <input type="checkbox" id="check" />
        <label for="check">
          <i
            class="fa-solid fa-bars show-menu"
            onclick="ToggleMenu()"
            id="menu"
          ></i>
        </label>

        <ul class="pages">
          <li><a href="/">Home</a></li>
          <li><a href="/HTML/Search.html">Search</a></li>
          <li><a href="/HTML/BorrowedBooks.html">Borrowed Books</a></li>
          <li><a href="/HTML/UpdateBooks.html">Update Books</a></li>
          <li><a href="/HTML/AvailableBooks.html">Available Books</a></li>
          <li><a href="/HTML/About.html">About</a></li>
          <li><a href="/HTML/login.html">login</a></li>
        </ul>
        <!-- user profile -->
        <div id="user-profile-icon" style="display: none">
          <a class="active" href="userCard.html"></a>
        </div>

      </nav>
    `;

  // Select the navbarContainer element
  const navbarContainer = document.getElementById("nav-container");

  // Add the navigation bar HTML to the navbarContainer
  navbarContainer.innerHTML = navbarHtml;

  // Select all elements with the 'navbar' class
  const navbarElements = document.querySelectorAll(".pages");

  // Get the current URL path without query parameters
  const currentPath = window.location.pathname;

  // Loop over each navbar element
  navbarElements.forEach(function (navbar) {
    // Find all anchor tags within the current navbar element
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
