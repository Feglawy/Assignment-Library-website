document.addEventListener("DOMContentLoaded", () => {
  let book_name = document.getElementById("Book_name");
  const deleteBtns = document.querySelectorAll(".Delete");
  const popupOverlay = document.getElementById("popup_overlay");
  const confirmBtn = document.getElementById("confirm_button");
  const cancelBtn = document.getElementById("cancel_button");

  let bookId;
  let bookDiv;

  deleteBtns.forEach((button) => {
    button.addEventListener("click", (event) => {
      bookDiv = event.target.closest(".book");
      bookId = event.target.getAttribute("book_id");
      book_name.innerHTML = event.target.getAttribute("book_name");
      popupOverlay.classList.add("visible");
    });
  });

  const closePopup = () => {
    popupOverlay.classList.remove("visible");
  };

  confirmBtn.addEventListener("click", async () => {
    try {
      const response = await fetch(`/api/book/delete/${bookId}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
      });
      if (response.ok) {
        const successMessage = "Book deleted!";
        toastr.success(successMessage, "Success", {
          closeButton: true,
          progressBar: true,
        });
        bookDiv.remove();
      } else {
        const failedMessage = "There an error occured!";
        toastr.error(failedMessage, "Error");
      }
    } catch (error) {
      alert("Error: " + error.message);
    }
    closePopup();
  });

  cancelBtn.addEventListener("click", () => {
    closePopup();
  });

  popupOverlay.addEventListener("click", (e) => {
    if (e.target === popupOverlay) {
      closePopup();
    }
  });
});

async function suggest(event) {
  let bookId = event.target.getAttribute("book_id");

  try {
    const response = await fetch(`/api/add_recommendation/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({
        book_id: bookId,
      }),
    });
    if (response.ok) {
      const successMessage = "successfully added to the recommended books";
      toastr.success(successMessage, "Success");
      book_suggested(event);
    } else {
      const failedMessage = "There an error occurred";
      toastr.error(failedMessage, "Failed");
    }
  } catch (error) {
    alert(`Error: ${error}`);
  }
}

async function un_suggest(event) {
  try {
    let bookId = event.target.getAttribute("book_id");
    const response = await fetch(`/api/delete_recommendation/${bookId}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
    });

    if (response.ok) {
      const successMessage =
        "successfully removed the book from recommendations";
      toastr.success(successMessage, "success");
      book_unsuggested(event);
    } else {
      const failedMessage = "There is an error occured";
      toastr.error(failedMessage, "failed");
    }
  } catch (error) {
    alert(`Error: ${error}`);
  }
}

function book_suggested(event) {
  let button = event.target;
  button.classList.add("RED");
  const un_suggested = `
    <span class="symbol">&#215</span>
    <span class="symbol-text">Unsuggest</span>
  `;
  button.innerHTML = un_suggested;
  button.setAttribute("onclick", "un_suggest(event)");
}

function book_unsuggested(event) {
  let button = event.target;
  button.classList.remove("RED");
  const suggested = `
    <span class="symbol">+</span>
    <span class="symbol-text">Suggest</span>
  `;
  button.innerHTML = suggested;
  button.setAttribute("onclick", "suggest(event)");
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
