/*
Created on Tue Nov 23 17:20:40 2021

Project Name: Solar PV
File: JS Sheet
@author: HR SINGH
*/
window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
