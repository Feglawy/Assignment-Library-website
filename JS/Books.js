function removeBtnParent(button) {
  // Get the parent element
  const parentDiv = button.parentNode;
  parentDiv.remove();
}

function showPopup() {
  let popup = document.getElementById("popup");
  popup.style.display = "block";
  setTimeout(() => {
    popup.classList.remove("hidden");
  }, 100);
}
function hidePopup() {
  let popup = document.getElementById("popup");
  popup.classList.add("hidden");
  setTimeout(() => {
    popup.style.display = "none";
  }, 200);
}

function cancelDelete() {
  hidePopup();
}

// wait until the book is loaded
document.addEventListener("BooksAdded", function () {
  // Get all anchor elements with the specified class name
  let RemoveBorrowedBtns = document.querySelectorAll(".remove-borrowed-book");

  let popupElements = `<div id="overlay">
        <div id="confirmationPopup">
          <h1>Are you sure you want to delete the book?</h1>
          <div class="inputs">
            <button id="ConfirmDeletion">Yes</button>
            <button id="cancelDeletion">No</button>
          </div>
        </div>
      </div>`;

  let popupDiv = document.getElementById("popup");
  popupDiv.innerHTML = popupElements;

  RemoveBorrowedBtns.forEach(function (button) {
    button.addEventListener("click", function () {
      let btn = button;
      let confirm = document.getElementById("ConfirmDeletion");
      let cancel = document.getElementById("cancelDeletion");

      showPopup();
      confirm.addEventListener("click", function () {
        removeBtnParent(btn);
        hidePopup();
      });
      cancel.addEventListener("click", cancelDelete);
    });
  });

  // show book's details
  var previewButtons = document.querySelectorAll(".previewButton");
  previewButtons.forEach(function (button) {
    // click event listener to the button
    button.addEventListener("click", function () {
      // Get the book ID from the custom 'book-id' attribute
      var bookId = button.getAttribute("book-id");

      // Redirect to the preview page with the corresponding book ID
      window.location.href = "/HTML/preview.html?bookId=" + bookId;
    });
  });
});
