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
