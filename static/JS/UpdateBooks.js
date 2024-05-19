document.addEventListener("DOMContentLoaded", () => {
  let book_name = document.getElementById("Book_name");
  const deleteBtns = document.querySelectorAll(".Delete");
  const popupOverlay = document.getElementById("popup_overlay");
  const confirmBtn = document.getElementById("confirm_button");
  const cancelBtn = document.getElementById("cancel_button");

  let bookId;

  deleteBtns.forEach((button) => {
    button.addEventListener("click", (event) => {
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
