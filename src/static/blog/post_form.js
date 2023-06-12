// post_form.js

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("post-form");
    const submitButton = form.querySelector("button[type='submit']");
    const processingPopup = document.getElementById("processing-popup");
  
    form.addEventListener("submit", function() {
      // Show the processing popup
      processingPopup.classList.add("show");
  
      // Disable the submit button to prevent multiple form submissions
      submitButton.disabled = true;
    });
  });
  