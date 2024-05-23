document.addEventListener("DOMContentLoaded", () => {
  handle_form_popup();
  handle_delete_popup();
});

function handle_delete_popup() {
  let author_name = document.getElementById("tag_name");
  const deleteBtns = document.querySelectorAll(".Delete");
  const DeletePopupOverlay = document.getElementById("popup_overlay");
  const confirmBtn = document.getElementById("confirm_button");
  const cancelBtn = document.getElementById("cancel_button");

  let author_id;
  let tagDiv;

  deleteBtns.forEach((button) => {
    button.addEventListener("click", (event) => {
      openPopup(event);
    });
  });

  const openPopup = (event) => {
    tagDiv = event.target.closest(".item");
    author_id = event.target.getAttribute("tag_id");
    author_name.innerHTML = event.target.getAttribute("tag_name");
    DeletePopupOverlay.classList.add("visible");
  };

  const closePopup = () => {
    DeletePopupOverlay.classList.remove("visible");
  };

  confirmBtn.addEventListener("click", async () => {
    try {
      const response = await fetch(`/api/authors/${author_id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
      });
      if (response.ok) {
        const successMessage = "tag deleted!";
        toastr.success(successMessage, "Success", {
          closeButton: true,
          progressBar: true,
        });
        tagDiv.remove();
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

  DeletePopupOverlay.addEventListener("click", (e) => {
    if (e.target === DeletePopupOverlay) {
      closePopup();
    }
  });
}

function handle_form_popup() {
  let author_id;
  let item_name_element;
  let tagDiv;

  const editBtns = document.querySelectorAll(".edit");
  const submitBtn = document.getElementById("submit");
  let formPopupOverlay = document.getElementById("create_edit_popup_overlay");
  let form = document.getElementById("create_edit_form");
  $("#add_new").click(() => {
    author_id = "";
    document.getElementById("id_name").value = "";
    openPopup();
  });

  editBtns.forEach((button) => {
    button.addEventListener("click", (event) => {
      tagDiv = event.target.closest(".item");
      item_name_element = tagDiv.children[0];
      author_id = event.target.getAttribute("tag_id");
      openEditPopup(author_id);
    });
  });

  const openEditPopup = (author_id) => {
    initialize_edit_form(author_id);
    formPopupOverlay.classList.add("visible");
  };

  const initialize_edit_form = (author_id) => {
    fetch(`/api/authors/${author_id}/`)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        let nameInp = document.getElementById("id_name");
        nameInp.value = data.name;
      })
      .catch((error) => {
        alert("error");
      });
  };

  const submit_form = async () => {
    let isEdit = author_id ? true : false;
    let url = `/api/authors/`;
    if (isEdit) {
      url = `/api/authors/${author_id + `/`}`;
    }
    let request_method = isEdit ? "PUT" : "POST";
    let new_name = document.getElementById("id_name").value;
    const response = await fetch(url, {
      method: request_method,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({
        name: new_name,
      }),
    });
    if (response.ok) {
      if (isEdit) {
        item_name_element.innerHTML = new_name;
      } else {
        location.reload();
      }
    } else {
      alert("error");
    }
  };

  $("#create_edit_form").submit(function (event) {
    event.preventDefault();
    submit_form();
    closePopup();
  });

  formPopupOverlay.addEventListener("click", (e) => {
    if (e.target === formPopupOverlay) {
      closePopup();
    }
  });

  const openPopup = () => {
    formPopupOverlay.classList.add("visible");
  };

  const closePopup = () => {
    formPopupOverlay.classList.remove("visible");
  };
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
