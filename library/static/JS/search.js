// search_bar.addEventListener("input", () => {
//   search_the_db();
// });

// let search_by_buttons = document.querySelector('input[name="searchBy"]');
// search_by_buttons.forEach((radioButton) => {
//   radioButton.addEventListener("change", () => {
//     search_the_db();
//   });
// });

function search_the_db() {
  let search_bar = document.getElementById("search-bar");
  let search_by = document.querySelector('input[name="searchBy"]:checked');
  fetch(
    "/searchAPI/?search=" + search_bar.value + "&searchBy=" + search_by.value,
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
}

function add_search_results(results) {
  let result_section = document.getElementById("The-result-Books-section");

  result_section.innerHTML = "";
  if (results.length === 0) {
    result_section.innerHTML =
      '<h1 style="text-align:center">Sorry the books you are searching for not found ☠️☠️</h1>';
  }
  results.forEach(function (res) {
    console.log(res);
    result_section.innerHTML +=
      '<div class="book"> <img src="' +
      res.cover +
      '" alt="' +
      res.pk +
      '" /> <h5 class="name">' +
      res.title +
      '</h5> <a class="previewButton" book-id="' +
      res.pk +
      '" href="' +
      res.url +
      '">Details</a> </div>';
  });
}
