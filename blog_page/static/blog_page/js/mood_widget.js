// mood_widget.js

function selectMood(element) {
    // Get the value of the clicked mood image
    var moodValue = element.getAttribute('data-value');
    console.log("Selected mood value:", moodValue);
    
    // Update the hidden input field with the selected mood value
    var hiddenInput = element.parentElement.querySelector('input[type="hidden"]');
    console.log("Hidden input found:", hiddenInput);
    if (hiddenInput) {
        hiddenInput.value = moodValue;
    } else {
        console.error("Hidden input not found!");
    }
    
    // Optionally, update the appearance of the images to show which one is selected
    var moodImages = element.parentElement.querySelectorAll('.mood-image');
    moodImages.forEach(function(img) {
        img.classList.remove('checked');
    });
    element.classList.add('checked');
}
