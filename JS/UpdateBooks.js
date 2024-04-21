import { bookMap } from "./AvailableBooks.js";

document.addEventListener("DOMContentLoaded", function () {
  let booksSection = document.getElementById("Update-books-section");
  bookMap.forEach((value, key) => {
    let Book = `
<div class="book">
    <img src=${value.cover} alt="${key}" />
    <h5 class="name">${value.tittle}</h5>
    <button class="Edit">Edit</button>
    <button class="Delete">Delete</button>
</div>
`;
    booksSection.innerHTML += Book;
  });

  // Attach event listener for edit buttons
  editFunction();

  // Event listener to ensure that the books added
  const BooksAdded = new Event("BooksAdded");
  document.dispatchEvent(BooksAdded);
});

// POPUP
const openModalBtn = document.querySelectorAll("[data-modal-target]");
const closeModalBtn = document.querySelectorAll("[data-close-btn]");
const overlayModal = document.getElementById("overlay-modal");

openModalBtn.forEach((button) => {
  button.addEventListener("click", () => {
    const modalId = button.getAttribute("data-modal-target");
    const modal = document.querySelector(modalId);
    openModal(modal);
  });
});

overlayModal.addEventListener("click", () => {
  const modals = document.querySelectorAll(".modal.active");
  modals.forEach((modal) => {
    closeModal(modal);
  });
});

closeModalBtn.forEach((button) => {
  button.addEventListener("click", () => {
    const modal = button.closest(".modal");
    closeModal(modal);
  });
});

function openModal(modal) {
  if (modal == null) {
    return;
  }
  document.body.style.overflow = "hidden"; // Disable page scrolling
  modal.classList.add("active");
  overlayModal.classList.add("active");
}

function closeModal(modal) {
  if (modal == null) {
    return;
  }
  document.body.style.overflow = "auto"; // Enable page scrolling
  modal.classList.remove("active");
  overlayModal.classList.remove("active");
}

document.querySelector("#uploadInput").addEventListener("change", function () {
  const file = this.files[0];
  const reader = new FileReader();

  reader.onload = function (e) {
    const imgElement = document.querySelector("#uploadedImage"); //To display the book's cover
    imgElement.src = e.target.result;
  };

  if (file) {
    reader.readAsDataURL(file);
  }
});

//////////////////////////////////////    Submit button functionality                          /////////////////////////////////////////////////////

document.getElementById("Submit-book").addEventListener("click", addBook);

function addBook() {
  const title = document.querySelector("#modal input[type='title']").value;
  const author = document.querySelector("#modal input[type='author']").value;
  const description = document.querySelector(
    "#modal input[type='description']"
  ).value;
  const type = document.querySelector("#modal input[type='type']").value;
  const cover = document.querySelector("#uploadedImage").src;

  let bookHTML = `
    <div class="book">
      <img src="${cover}" alt="${title}" />
      <h5 class="name">${title}</h5>
      <button class="Edit">Edit</button>
      <button class="Delete">Delete</button>
    </div>
  `;

  let booksSection = document.getElementById("Update-books-section");
  booksSection.innerHTML += bookHTML;

  const modal = document.getElementById("modal");
  closeModal(modal);

  // to be able to use the edit on the new added books
  editFunction();
}

// Function to attach event listener for edit buttons
function editFunction() {
  const editButtons = document.querySelectorAll(".Edit");
  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const bookDiv = button.closest(".book");
      const title = bookDiv.querySelector(".name").textContent;
      const cover = bookDiv.querySelector("img").src;


       // Add the "editing" class to the book element
      bookDiv.classList.add("editing");

      // putting the existing data in the popup
      document.getElementById("edit-uploadedImage").src = cover;
      document.getElementById("edit-book-title").value = title;

      // Open the edit popup
      const modal = document.getElementById("edit-modal");
      openModal(modal);
    });
  });
}

document.getElementById("save-edit").addEventListener("click", editSave);


document.querySelector("#edit-uploadInput").addEventListener("change", function () {
  const file = this.files[0];
  const reader = new FileReader();

 reader.onload = function (e) {
  console.log("File read successfully:", e.target.result);
  const imgElement = document.querySelector("#edit-uploadedImage");
  console.log("Image element:", imgElement);
  imgElement.src = e.target.result;
};

  if (file) {
    reader.readAsDataURL(file);
  }
});
function editSave(){
  const newCover = document.getElementById("edit-uploadInput").src ;
  const newTitle = document.getElementById("edit-book-title").value; 
  console.log("test");
  
  const editedBook = document.querySelector(".book.editing");
  console.log("editedBook:", editedBook);
  const coverElement = editedBook.querySelector("img");
  console.log("edited img");
  
  const titleElement = editedBook.querySelector(".name");
  console.log("edited naame");
  
  
  coverElement.src = newCover;
  titleElement.textContent = newTitle;
  
  
  editedBook.classList.remove("editing");
  
  // close popup
  const modal = document.getElementById("edit-modal");
  closeModal(modal);
  console.log("Changes saved successfully!");
  
}

