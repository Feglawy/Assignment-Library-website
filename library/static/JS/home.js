// import { bookMap } from "./AvailableBooks.js";

// document.addEventListener("DOMContentLoaded", function () {
//   let recommended = document.getElementById("recommended-section");
//   bookMap.forEach((value, key) => {
//     let Book = `
// <div class="book">
//     <img src=${value.cover} alt="${key}" />
//     <h5 class="name">${value.tittle}</h5>
//     <button class="previewButton" book-id="${key}">Details</button>
// </div>
// `;
//     recommended.innerHTML += Book;
//   });

//   // event listner to ensure that the books added
//   const BooksAdded = new Event("BooksAdded");
//   document.dispatchEvent(BooksAdded);
// });

let loadingAnimation = document.getElementById("loading-animation");
fetch("random/quote/")
  .then((response) => response.json())
  .then((data) => {
    // hide the animation
    loadingAnimation.style.display = "none";
    // adding the quote data to the html page
    document.getElementById("quote").innerHTML = `
                    <blockquote>
                        <p>“${data.quote}”</p>
                        <footer>author : ${data.author}</footer>
                    </blockquote>
                `;
  })
  .catch((error) => {
    // hide the animation
    loadingAnimation.style.display = "none";

    console.error("Error:", error);
  });
