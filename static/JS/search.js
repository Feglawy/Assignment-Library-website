function search_the_db() {
  let search_bar = document.getElementById("search-bar");
  let search_by = document.querySelector('input[name="searchBy"]:checked');
  fetch(
    "/api/search/?search=" + search_bar.value + "&searchBy=" + search_by.value,
    {
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    }
  )
    .then((response) => response.json())
    .then((data) => {
      add_search_results(data);
    })
    .catch((error) => {
      console.log("Error: ", error);
    });

  let result_container = document.getElementById("auto_compelete_container");
  let result_list = document.getElementById("auto_compelete_list");

  if (search_bar.value === "") {
    result_list.innerHTML = ``;
    result_container.classList.remove("visible");
    return;
  }
  let search_like_url;
  if (search_by.value === "title") {
    search_like_url = `book_like`;
  } else if (search_by.value === "author") {
    search_like_url = `autor_like`;
  } else {
    search_like_url = `genre_like`;
  }

  fetch(`/api/${search_like_url}/${search_bar.value}`)
    .then((response) => response.json())
    .then((data) => {
      result_list.innerHTML = ``;
      result_container.classList.add("visible");
      const topResults = data.slice(0, 5);
      topResults.forEach((item) => {
        const result = document.createElement("li");
        result.className = "result";
        if (item.title) {
          result.textContent = item.title;
        } else {
          result.textContent = item.name;
        }
        result.addEventListener("click", () => {
          document.getElementById("search-bar").value = result.textContent;
        });
        result_list.appendChild(result);
      });
    })
    .catch((error) => {
      alert(error);
    });
}

function add_search_results(results) {
  let result_section = document.getElementById("The-result-Books-section");

  result_section.innerHTML = "";
  if (results.length === 0) {
    result_section.innerHTML =
      '<h1 style="text-align:center">Sorry the books you are searching for not found.</h1>';
  }
  results.forEach(function (res) {
    result_section.innerHTML +=
      '<div class="book"><a href="' +
      res.url +
      '"><img src="' +
      res.cover +
      '" alt="' +
      res.title +
      '" /> </a><h5 class="name">' +
      res.title +
      '</h5> <a class="previewButton" book-id="' +
      res.pk +
      '" href="' +
      res.url +
      '">Details</a> </div>';
  });
}
