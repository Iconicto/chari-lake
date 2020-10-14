var modal = document.getElementById("modal");
var selectedImg = document.getElementById("modal-image");
var gallery = document.getElementById("gallery");

// setImages();

function showImage(src) {
  selectedImg.src = src;
  modal.classList.add("is-active");
}

function closeImage() {
  console.log("object");
  modal.classList.remove("is-active");
}

function setImages() {
  for (i = 1; i < 23; i++) {
    var galleryCell = document.createElement("div");
    galleryCell.setAttribute("class", "column is-4");
    var image = document.createElement("img");
    image.setAttribute("src", `https://cdn.iconicto.com/ChariLake/img/gallery/chari-lake-${i}.jpg`);
    image.setAttribute("class", "gallery-image");
    image.setAttribute("onclick", "showImage(this.src)");
    galleryCell.appendChild(image);
    gallery.appendChild(galleryCell);
  }
}
