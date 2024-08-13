// mood_widget.js

function selectMood(element) {
    // Get the value of the clicked mood image
    var moodValue = element.getAttribute('data-value');
    
    // Update the hidden input field with the selected mood value
    var hiddenInput = element.parentElement.querySelector('input[type="hidden"]');
    hiddenInput.value = moodValue;
    
    // Optionally, update the appearance of the images to show which one is selected
    var moodImages = element.parentElement.querySelectorAll('.mood-image');
    moodImages.forEach(function(img) {
        img.classList.remove('checked');
    });
    element.classList.add('checked');
}