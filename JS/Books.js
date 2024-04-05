function isMobileDevice() {
  return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|SamsungBrowser/i.test(
    navigator.userAgent
  );
}

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
