$(document).ready(function () {
    $(document).on('submit', '#newsletter_form',function (e) {
        e.preventDefault();
        const name=$('#newsletter_input_name').val();
        const email=$('#newsletter_input_email').val();
        console.log(name)
        console.log(email)
        $.ajax({
            type: 'POST',
            url: 'getemail/',
            data: {
                name:name,
                email:email,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                console.log("Data saved successfully")

            },
        });

        document.getElementById("newsletter_form").setAttribute('class', 'd-none')
        document.getElementById("welcome").setAttribute("class", 'block mt-5');
        document.querySelector(".footer_contact_row").style.marginTop="0px"
    });
});