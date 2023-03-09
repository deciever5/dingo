var contactInfoElements = document.querySelectorAll(".contact-info");

// Set the initial delay time
var delay = 0.2;

// Loop through each element and add a delay before fading in
contactInfoElements.forEach(function (element) {
  element.style.transition = "opacity 1s ease-in-out " + delay + "s";
  element.style.opacity = 0;
  setTimeout(function () {
    element.style.opacity = 1;
  }, delay * 500);
  delay += 0.2;
});