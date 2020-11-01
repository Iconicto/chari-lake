const modal = document.getElementById("modal");
const selectedImg = document.getElementById("modal-image");
const nextButton = document.querySelector("#modal > a.gallery-control.next")
const prevButton = document.querySelector("#modal > a.gallery-control.prev")

function showImage(src, img_index=undefined) {
  selectedImg.src = src;
  modal.classList.add("is-active");

  if (img_index === undefined){
    img_index = images.indexOf(src)
  }

  if(img_index === 0){
    prevButton.style.display = "none"
  }
  if(img_index === images.length-1){
    nextButton.style.display = "none"
  }
}

function closeImage() {
  modal.classList.remove("is-active");
}

function plusSlides(index){
  const new_index = index + images.indexOf(selectedImg.src);
  prevButton.style.display = "block"
  nextButton.style.display = "block"
  showImage(images[new_index], new_index)
}