function isMobileDevice() {
  return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|SamsungBrowser/i.test(
    navigator.userAgent
  );
}

var bookDivs = document.querySelectorAll(".book");
if (isMobileDevice()) {
  bookDivs.forEach(function (bookDiv) {
    bookDiv.classList.add("no-hover");
  });
}
