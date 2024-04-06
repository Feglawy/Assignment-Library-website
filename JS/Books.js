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
let BorrowedBtns = document.querySelectorAll(".Borrowed");

// Loop through each anchor element
BorrowedBtns.forEach(function (button) {
  // Add mouseover event listener
  button.addEventListener("mouseover", function () {
    // Change the text of the hovered button
    button.textContent = "\u00D7 Remove"; // Unicode for '×' symbol
  });

  // mouseout event listener
  button.addEventListener("mouseout", function () {
    // Restore the original text when the mouse moves out
    button.textContent = "Borrowed";
  });

  button.addEventListener("click", function () {
    // Get the parent element
    const parentDiv = button.parentNode;
    parentDiv.remove();
  });
});

// wait until the book is loaded
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
