function borrow(bookId) {
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
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      const successMessage = "Book borrowed!";
      toastr.success(successMessage, "Success", {
        closeButton: true,
        progressBar: true,
      });
    })
    .catch((error) => {
      console.error("error : ", error);
      const errorMessage = error
        ? error.message || "Unknown error occurred"
        : "Unknown error occurred";
      toastr.error(errorMessage, "There is an error occurred");
    });
}

function return_book(bookId) {
  fetch("/api/return/", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
      borrow_id: bookId,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      const successMessage = "Book returned!";
      toastr.success(successMessage, "Success", {
        closeButton: true,
        progressBar: true,
      });
    })
    .catch((error) => {
      console.error("error : ", error);
      const errorMessage = error
        ? error.message || "Unknown error occurred"
        : "Unknown error occurred";
      toastr.error(errorMessage, "There is an error occurred");
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
