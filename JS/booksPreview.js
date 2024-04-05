class Book {
  /*
  tittle : string
  description : string
  cover: string
  authors
  catagories: Array<string>
  type: string
  isAvailable: boolean = true
  */
  constructor(
    Tittle,
    Description,
    Cover,
    Authors,
    Catagories,
    Type,
    IsAvailable = true
  ) {
    this.tittle = Tittle;
    this.description = Description;
    this.cover = Cover;
    this.authors = Authors;
    this.catagories = Catagories;
    this.type = Type;
    this.isAvailable = IsAvailable;
  }
}

let bookMap = new Map();
let tpn = new Book(
  "The Promised Neverland",
  "Emma, Norman and Ray are the brightest kids at the Grace Field House orphanage. And under the care of the woman they refer to as “Mom,” all the kids have enjoyed a comfortable life. Good food, clean clothes and the perfect environment to learn—what more could an orphan ask for? One day, though, Emma and Norman uncover the dark truth of the outside world they are forbidden from seeing.",
  "/Images/covers/TPN-cover-18.webp",
  ["Kaiu shirai"],
  ["action", "Horror", "mystery"],
  "manga",
  true
);
let jjk = new Book(
  "Jujutsu kaisen",
  "In a world where cursed spirits feed on unsuspecting humans, fragments of the legendary and feared demon Ryomen Sukuna have been lost and scattered about. Should any demon consume Sukuna’s body parts, the power they gain could destroy the world as we know it. Fortunately, there exists a mysterious school of jujutsu sorcerers who exist to protect the precarious existence of the living from the supernatural! Although Yuji Itadori looks like your average teenager, his immense physical strength is something to behold! Every sports club wants him to join, but Itadori would rather hang out with the school outcasts in the Occult Research Club. One day, the club manages to get their hands on a sealed cursed object. Little do they know the terror they’ll unleash when they break the seal…",
  "/Images/covers/jjk-cover.webp",
  ["Gege akutami"],
  ["action", "Horror", "Dark fantasy"],
  "manga",
  true
);

bookMap.set("TPN", tpn);
bookMap.set("JJK", jjk);

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

window.onload = function () {
  // Get the book ID from the URL
  let bookId = getBookIdFromUrl();

  if (bookId) {
    // Fetch book information from the server
    // Book info is a Book object
    let bookInfo = fetchBookInfo(bookId);

    displayBookInfo(bookInfo);
  } else {
    alert("Could not load Book ");
  }
};
