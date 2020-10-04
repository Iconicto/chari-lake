//navigation transparency animation
var myNav = document.getElementById("navbar");
var hero = document.getElementById("hero");
var logo = document.getElementById("logo");
let mainNav = document.getElementById("js-menu");
let navBarToggle = document.getElementById("js-nav-toggle");
var visibilityHeight;
if (hero != null) {
  visibilityHeight = hero.clientHeight / 3;
} else {
  visibilityHeight = 0;
}
var width;
var iconNames = ["home", "about", "gallery", "contact"];

setNavBar();

window.onscroll = function() {
  "use strict";
  this.setNavBar();
};

function setNavBar() {
  if (
    document.body.scrollTop >= this.visibilityHeight ||
    document.documentElement.scrollTop >= this.visibilityHeight
  ) {
    this.setSolidNavBar();
  } else {
    this.setTransparentNavBar();
  }

  if (window.innerWidth < 800) {
    setSolidNavBar();
    hideNavIcons();
  } else {
    showNavIcons();
  }
}

window.addEventListener("resize", () => {
  setNavBarType();
});

function setNavBarType() {
  width = window.innerWidth;
  if (width < 800) {
    setSolidNavBar();
    hideNavIcons();
  } else {
    setNavBar();
    showNavIcons();
  }
}

function hideNavIcons() {
  var icons = document.getElementsByClassName("link-icons");
  for (var i = 0; i < icons.length; i++) {
    icons[i].classList.add("link-icons-hidden");
    icons[i].classList.remove("link-icons");
    hideNavIcons();
  }
}

function showNavIcons() {
  var icons = document.getElementsByClassName("link-icons-hidden");
  for (var i = 0; i < icons.length; i++) {
    icons[i].classList.add("link-icons");
    icons[i].classList.remove("link-icons-hidden");
  }
}

function setLinkColor(className, newClassName) {
  var items = document.getElementsByClassName(className);
  for (var i = 0; i < items.length; i++) {
    items[i].className = newClassName;
    setLinkColor(className, newClassName);
  }
}

function setIcons(imageTint) {
  var icons = document.getElementsByClassName("link-icons");
  for (var i = 0; i < icons.length; i++) {
    icons[i].src = "https://cdn.iconicto.com/ChariLake/img/" + iconNames[i] + "-" + imageTint + ".png";
  }
}

navBarToggle.addEventListener("click", function() {
  hideNavIcons();
  setLinkColor("navbar-links", "navbar-links-solid");
  mainNav.classList.toggle("active");
});

function setBlueLogo() {
  logo.src = "https://cdn.iconicto.com/ChariLake/img/logo-blue.png";
}

function setWhiteLogo() {
  logo.src = "https://cdn.iconicto.com/ChariLake/img/logo.png";
}

function setSolidNavBar() {
  myNav.classList.add("solid");
  myNav.classList.remove("transparent");
  setBlueLogo();
  setLinkColor("navbar-links", "navbar-links-solid");
  setIcons("blue");
}

function setTransparentNavBar() {
  myNav.classList.add("transparent");
  myNav.classList.remove("solid");
  setWhiteLogo();
  setLinkColor("navbar-links-solid", "navbar-links");
  setIcons("white");
}
