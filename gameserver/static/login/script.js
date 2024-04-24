document.addEventListener('DOMContentLoaded', function() {
    var inputFields = document.querySelectorAll('form input');
    inputFields.forEach(function(inputField) {
        inputField.classList.add('form-control');
    });
});
