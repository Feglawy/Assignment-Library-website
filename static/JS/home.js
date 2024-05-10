function setTheme(theme) {
  document.body.className = theme;
  localStorage.setItem("theme", theme);
}

themeToggle.addEventListener("change", function () {
  if (this.checked) {
    setTheme("dark");
  } else {
    setTheme("light");
  }
});

let loadingAnimation = document.getElementById("loading-animation");

function removeLastAtSymbol(str) {
  // Check if the string is not empty and the last character is '@'
  if (str.length > 0 && str[str.length - 1] === "@") {
    return str.slice(0, -1);
  }
  return str;
}

fetch("api/random/quote/")
  .then((response) => response.json())
  .then((data) => {
    // hide the animation
    loadingAnimation.style.display = "none";

    // the api might return the quote with '@' char in the end i dont know why
    let quote = removeLastAtSymbol(data.quote);

    // adding the quote data to the html page
    document.getElementById("quote").innerHTML = `
                    <blockquote>
                        <p><cite>“${quote}”</cite></p>
                         ~ ${data.author}
                    </blockquote>
                `;
  })
  .catch((error) => {
    // hide the animation
    loadingAnimation.style.display = "none";

    console.error("Error:", error);
  });
