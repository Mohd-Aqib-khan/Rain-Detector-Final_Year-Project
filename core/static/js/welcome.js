const subForm = document.getElementById("newsletter_form")
subForm.addEventListener('submit', function(e) {
    e.preventDefault();
    console.log("submitted");
    const hal = document.querySelector(".newsletter_form_container");
    hal.after(welcome)    
    const btn = document.querySelector('.newsletter_button');
    document.getElementById("newsletter_form").setAttribute('class', 'd-none')
    document.getElementById("welcome").setAttribute("class",'block')
    
});