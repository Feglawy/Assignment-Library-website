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

let addNewBtn = document.getElementById("add-new");

addNewBtn.addEventListener("click" , addNew);
//add new button
function addNew(){
    // access the add_new_book btn
    let addBtn = document.getElementById("add-new");
   
    addBtn.addEventListener('click', addBook);

    function addBook(value , key) {
        
        let bk = `
<div class="book">
    <img src="/Images/covers/Blank.png">
    <h5 class="name">Blank </h5>
    <button>Edit</button>
    <button class="Delete">Delete</button>
</div>
`;
 // add the book to the page
        let booksSection = document.getElementById("Update-books-section");
        booksSection.innerHTML += bk;


      // just to check function is working will delete later
      console.log('worked');
    }
  }
