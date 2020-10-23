const modal = document.getElementById("modal");
const selectedImg = document.getElementById("modal-image");

function showImage(src) {
  selectedImg.src = src;
  modal.classList.add("is-active");
}

function closeImage() {
  modal.classList.remove("is-active");
}
