function borrow(event, bookId) {
  fetch("/api/borrow/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
      book_id: bookId,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        return Promise.reject(response);
      }
      return response.json();
    })
    .then((data) => {
      book_borrowed(event, data.borrowed_book.id);
      const successMessage = "Book borrowed!";
      toastr.success(successMessage, "Success", {
        closeButton: true,
        progressBar: true,
      });
    })
    .catch((error) => {
      error.json().then((json) => {
        errorMessage = json.error;
        toastr.error(errorMessage, "There is an error occurred");
      });
    });
}

function return_book(event, bookId) {
  fetch("/api/return/", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
      book_id: bookId,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        return Promise.reject(response);
      }
      return response.json();
    })
    .then((data) => {
      book_returned(event, data.borrowed_book.id);
      const successMessage = "Book returned!";
      toastr.success(successMessage, "Success", {
        closeButton: true,
        progressBar: true,
      });
    })
    .catch((error) => {
      error.json().then((json) => {
        errorMessage = json.error;
        toastr.error(errorMessage, "There is an error occurred");
      });
    });
}

function borrow_timeout(bookId) {
  fetch("/api/borrow_timeout/", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
      book_id: bookId,
    }),
  }).then((response) => {
    return response.json();
  });
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function book_borrowed(event, book_id) {
  var button = event.target;
  button.innerText = "Return";
  button.classList.add("Borrowed");
  button.onclick = function (event) {
    return_book(event, book_id);
  };
}

function book_returned(event, book_id) {
  var button = event.target;
  button.innerText = "Borrow";
  button.classList.remove("Borrowed");
  button.onclick = function (event) {
    borrow(event, book_id);
  };
}



///________________________
// function borrow(event, bookId) {
//   $.ajax({
//     url: "/api/borrow/",
//     method: "POST",
//     headers: {
//       "X-CSRFToken": getCookie("csrftoken"),
//     },
//     contentType: "application/json",
//     data: JSON.stringify({ book_id: bookId }),
//     success: function (data) {
//       book_borrowed(event, data.borrowed_book.id);
//       const successMessage = "Book borrowed!";
//       toastr.success(successMessage, "Success", {
//         closeButton: true,
//         progressBar: true,
//       });
//     },
//     error: function (jqXHR, textStatus, errorThrown) {
//       errorMessage = errorThrown;
//       toastr.error(errorMessage, "There is an error occurred");
//     },
//   });
// }

// function return_book(event, bookId) {
//   $.ajax({
//     url: "/api/return/",
//     method: "PUT",
//     headers: {
//       "X-CSRFToken": getCookie("csrftoken"),
//     },
//     contentType: "application/json",
//     data: JSON.stringify({ book_id: bookId }),
//     success: function (data) {
//       book_returned(event, data.borrowed_book.id);
//       const successMessage = "Book returned!";
//       toastr.success(successMessage, "Success", {
//         closeButton: true,
//         progressBar: true,
//       });
//     },
//     error: function (jqXHR, textStatus, errorThrown) {
//       errorMessage = errorThrown;
//       toastr.error(errorMessage, "There is an error occurred");
//     },
//   });
// }

// function borrow_timeout(bookId) {
//   $.ajax({
//     url: "/api/borrow_timeout/",
//     method: "PUT",
//     headers: {
//       "X-CSRFToken": getCookie("csrftoken"),
//     },
//     contentType: "application/json",
//     data: JSON.stringify({ book_id: bookId }),
//     success: function (data) {
//       console.log(data);
//     },
//     error: function (jqXHR, textStatus, errorThrown) {
//       console.log(
//         "There has been an error with the borrow timeout",
//         textStatus,
//         errorThrown
//       );
//     },
//   });
// }

// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       if (cookie.substring(0, name.length + 1) === name + "=") {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }

// function book_borrowed(event, book_id) {
//   var button = event.target;
//   button.innerText = "Return";
//   button.classList.add("Borrowed");
//   button.onclick = function (event) {
//     return_book(event, book_id);
//   };
// }

// function book_returned(event, book_id) {
//   var button = event.target;
//   button.innerText = "Borrow";
//   button.classList.remove("Borrowed");
//   button.onclick = function (event) {
//     borrow(event, book_id);
//   };
// }
/// _________