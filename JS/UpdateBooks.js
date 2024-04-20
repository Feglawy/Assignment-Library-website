import { bookMap } from "./AvailableBooks.js";

document.addEventListener("DOMContentLoaded", function () {
  let booksSection = document.getElementById("Update-books-section");
  bookMap.forEach((value, key) => {
    let Book = `
<div class="book">
    <img src=${value.cover} alt="${key}" />
    <h5 class="name">${value.tittle}</h5>
    <button>Edit</button>
    <button class="Delete">Delete</button>
</div>
`;
    booksSection.innerHTML += Book;
  });

  // event listner to ensure that the books added
  const BooksAdded = new Event("BooksAdded");
  document.dispatchEvent(BooksAdded);
});

////////////////////// POPUP /////////////////////

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
  document.body.style.overflow = "hidden"; // disable page scrolling
  modal.classList.add("active");
  overlayModal.classList.add("active");
}

function closeModal(modal) {
  if (modal == null) {
    return;
  }
  document.body.style.overflow = "auto"; // enable page scrolling
  modal.classList.remove("active");
  overlayModal.classList.remove("active");
}


document.querySelector("#uploadInput").addEventListener("change", function () {
  const file = this.files[0];
  const reader = new FileReader();

  reader.onload = function (e) {
    const imgElement = document.querySelector("#uploadedImage");
    imgElement.src = e.target.result;
  };

  if (file) {
    reader.readAsDataURL(file);
  }
});

document.getElementById("Submit-book").addEventListener("click", addBook);

function addBook() {
  const title = document.querySelector("#modal input[type='title']").value;
  const author = document.querySelector("#modal input[type='author']").value;
  const description = document.querySelector("#modal input[type='description']").value;
  const type = document.querySelector("#modal input[type='type']").value;
  const cover = document.querySelector("#uploadedImage").src;

  let bookHTML = `
    <div class="book">
      <img src="${cover}" alt="${title}" />
      <h5 class="name">${title}</h5>
      <button>Edit</button>
      <button class="Delete">Delete</button>
    </div>
  `;

  let booksSection = document.getElementById("Update-books-section");
  booksSection.innerHTML += bookHTML;

  const modal = document.getElementById("modal");
  closeModal(modal);}