window.onscroll = function() {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("hide").style.display = "none";
    document.getElementById("navbar-main").style.display = "inline-flex";
    document.getElementById("navbar-links").style.display = "block";
  } else {
    document.getElementById("hide").style.display = "flex";
    document.getElementById("navbar-main").style.display = "none";
    document.getElementById("navbar-links").style.display = "none";
  }
}
