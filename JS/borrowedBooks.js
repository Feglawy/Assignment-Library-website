import { bookMap } from "./AvailableBooks.js";

document.addEventListener("DOMContentLoaded", function () {
  let recommended = document.getElementById("borrowed-Books-section");
  bookMap.forEach((value, key) => {
    let Book = `
<div class="book">
    <img src=${value.cover} alt="${key}" />
    <h5 class="name">${value.tittle}</h5>
    <button class="remove-borrowed-book" type="button">\u00D7</button>
    <button class="Borrowed" type="button">Borrowed</button>
    <button class="previewButton" book-id="${key}" type="button">Details</button>
</div>
`;
    recommended.innerHTML += Book;
  });
  if (bookMap.size === 0) {
    recommended.innerHTML = `<h1 id="no-borrow-books">Looks like you didn't borrow any books yet.</h1>`;
  }

  // event listner to ensure that the books added
  const BooksAdded = new Event("BooksAdded");
  document.dispatchEvent(BooksAdded);
});
