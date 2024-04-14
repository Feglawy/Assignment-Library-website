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

function confirmDelete(btn) {
  return function (event) {
    removeBtnParent(btn);
    hidePopup();
  };
}

function cancelDelete() {
  hidePopup();
}

function handleRemoveBookPopup(button) {
  return function (event) {
    let confirm = document.getElementById("ConfirmDeletion");
    let cancel = document.getElementById("cancelDeletion");

    showPopup();
    confirm.addEventListener("click", confirmDelete(button));
    cancel.addEventListener("click", cancelDelete);
  };
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
      button.addEventListener("click", handleRemoveBookPopup(button));
    });
  }

  if (RemoveBookAdminBtns != null) {
    RemoveBookAdminBtns.forEach(function (button) {
      button.addEventListener("click", handleRemoveBookPopup(button));
    });
  }
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


