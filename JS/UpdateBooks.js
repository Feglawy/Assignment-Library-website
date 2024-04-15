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

const openModalBtn = document.querySelectorAll('[data-modal-target]');
const closeModalBtn = document.querySelectorAll('[data-close-btn]');
const overlayModal = document.getElementById('overlay-modal');

openModalBtn.forEach(button => {
  button.addEventListener('click', () => {
    const modalId = button.getAttribute('data-modal-target');
    const modal = document.querySelector(modalId);
    openModal(modal);
  });
});


overlayModal.addEventListener('click', () => {
  const modals = document.querySelectorAll('.modal.active');
  modals.forEach(modal => {
    closeModal(modal);
  });
});

closeModalBtn.forEach(button => {
  button.addEventListener('click', () => {
    const modal = button.closest('.modal');
    closeModal(modal);
  });
});

function openModal(modal) {
  if(modal == null) {return}
  modal.classList.add('active');
  overlayModal.classList.add('active');
}

function closeModal(modal) {
  if(modal == null) {return}
  modal.classList.remove('active');
  overlayModal.classList.remove('active');
}

// let addNewBtn = document.getElementById("Submit-book");

// addNewBtn.addEventListener("click", addBook);
// //add new button
// function addBook(value, key) {
//   let bk = `
// <div class="book">
//     <img src="/Images/covers/Blank.png">
//     <h5 class="name">Blank </h5>
//     <button>Edit</button>
//     <button class="Delete">Delete</button>
// </div>
// `;
//   // add the book to the page
//   let booksSection = document.getElementById("Update-books-section");
//   booksSection.innerHTML += bk;
//   // event listner to ensure that the books added
//   const BooksAdded = new Event("BooksAdded");                                              WILL DO IT LATER
//   document.dispatchEvent(BooksAdded);
// }