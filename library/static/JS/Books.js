// _____ Remove book popup _____
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
  let RemoveBookAdminBtns = document.querySelectorAll(".Delete");

  let RemoveBookPopupElements = `<div id="overlay">
        <div id="confirmationPopup">
          <h1>Are you sure you want to delete the book?</h1>
          <div class="inputs">
            <button id="ConfirmDeletion">Yes</button>
            <button id="cancelDeletion">No</button>
          </div>
        </div>
      </div>`;

  let popupDiv = document.getElementById("popup");
  if (popupDiv != null) {
    popupDiv.innerHTML = RemoveBookPopupElements;
  }

  if (RemoveBorrowedBtns != null) {
    RemoveBorrowedBtns.forEach(function (button) {
      button.addEventListener("click", function () {
        let confirm = document.getElementById("ConfirmDeletion");
        let cancel = document.getElementById("cancelDeletion");

        showPopup();
        // Get the parent element
        let parentDiv = button.parentNode;

        confirm.addEventListener("click", function () {
          parentDiv.remove();
          hidePopup();
        });
        cancel.addEventListener("click", function () {
          parentDiv = null;
          hidePopup();
        });
      });
    });
  }

  if (RemoveBookAdminBtns != null) {
    RemoveBookAdminBtns.forEach(function (button) {
      button.addEventListener("click", function () {
        let confirm = document.getElementById("ConfirmDeletion");
        let cancel = document.getElementById("cancelDeletion");

        showPopup();
        // Get the parent element
        let parentDiv = button.parentNode;

        confirm.addEventListener("click", function () {
          parentDiv.remove();
          parentDiv = null;
          hidePopup();
        });
        cancel.addEventListener("click", function () {
          parentDiv = null;
          hidePopup();
        });
      });
    });
  }

  // ________________________
  // show book's details
  var previewButtons = document.querySelectorAll(".previewButton");
  previewButtons.forEach(function (button) {
    // click event listener to the button
    button.addEventListener("click", function () {
      // Get the book ID from the custom 'book-id' attribute
      var bookId = button.getAttribute("book-id");

      // Redirect to the preview page with the corresponding book ID
      window.location.href = "/preview?bookId=" + bookId;
    });
  });
});
