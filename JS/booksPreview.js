import { bookMap, BorrowedBooksMap } from "./AvailableBooks.js";

// param: BookInfo is type Book
function displayBookInfo(BookInfo) {
  if (!BookInfo) {
    return;
  }
  let bookCover = document.getElementById("preview-img");
  let bgImage = document.getElementById("bg-img");
  let BookTitle = document.getElementById("book-name");
  let bookDescripton = document.getElementById("book-description");
  let BookAuthors = document.getElementById("author");
  let BookType = document.getElementById("types");
  let BookCatagories = document.getElementById("categories");

  bgImage.src = BookInfo.cover;
  bookCover.src = BookInfo.cover;

  BookTitle.innerHTML = BookInfo.tittle;
  bookDescripton.innerHTML = BookInfo.description;

  // append list item for each author
  BookInfo.authors.forEach(function (author) {
    let authorListNode = document.createElement("li");
    let listNodeText = document.createTextNode(author);

    authorListNode.appendChild(listNodeText);
    BookAuthors.appendChild(authorListNode);
  });

  // add types
  let TypeListNode = document.createElement("li");
  let listNodeText = document.createTextNode(BookInfo.type);

  TypeListNode.appendChild(listNodeText);
  BookType.appendChild(TypeListNode);

  // append catagory list item for each catagory
  BookInfo.catagories.forEach(function (catagory) {
    let catagoryListNode = document.createElement("li");
    let listNodeText = document.createTextNode(catagory);

    catagoryListNode.appendChild(listNodeText);
    BookCatagories.appendChild(catagoryListNode);
  });
}

// param: bookId is type string
function fetchBookInfo(bookId) {
  return bookMap.get(bookId);
}

// returns the bookid parametar from the url example : http://127.0.0.1:5000/HTML/preview.html?bookId=TPN it will return TPN
function getBookIdFromUrl() {
  var queryString = window.location.search;
  var urlParams = new URLSearchParams(queryString);
  return urlParams.get("bookId");
}

// Get the book ID from the URL
let bookId = getBookIdFromUrl();

// Fetch book information from the server
// Book info is a Book object
let bookInfo = fetchBookInfo(bookId);

window.onload = function () {
  if (bookId) {
    displayBookInfo(bookInfo);
  }
};

let borrowBtn = document.getElementById("borrow-btn");
borrowBtn.addEventListener("click", function addToBorrowedBooks() {
  BorrowedBooksMap.set(bookId, bookInfo);
});
