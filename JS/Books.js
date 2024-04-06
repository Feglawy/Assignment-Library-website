// checls if the device is a mobile device or not
function isMobileDevice() {
  return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|SamsungBrowser/i.test(
    navigator.userAgent
  );
}

// disable the hover effect of the books if the device is a mobile device
var bookDivs = document.querySelectorAll(".book");
if (isMobileDevice()) {
  bookDivs.forEach(function (bookDiv) {
    bookDiv.classList.add("no-hover");
  });
}

// Get all anchor elements with the specified class name
var BorrowedBtns = document.querySelectorAll(".Borrowed");

// Loop through each anchor element
BorrowedBtns.forEach(function (anchor) {
  // Add mouseover event listener
  anchor.addEventListener("mouseover", function () {
    // Change the text of the hovered anchor
    anchor.textContent = "\u00D7 Remove"; // Using Unicode for '×' symbol
  });

  // Add mouseout event listener
  anchor.addEventListener("mouseout", function () {
    // Restore the original text when the mouse moves out
    anchor.textContent = "Borrowed";
  });
});

document.addEventListener("BooksAdded", function () {
  var previewButtons = document.querySelectorAll(".previewButton");
  previewButtons.forEach(function (button) {
    // Add click event listener to the button
    button.addEventListener("click", function () {
      // Get the book ID from the custom 'data-book-id' attribute
      var bookId = button.getAttribute("book-id");

      // Redirect to the preview page with the corresponding book ID
      window.location.href = "HTML/preview.html?bookId=" + bookId;
    });
  });
});
