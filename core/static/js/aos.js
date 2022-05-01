AOS.init({
    offset: 100,
    duration: 1500,
});

function myProfile(x) {
    if (x.matches) {
        elements = document.querySelectorAll("#profile_id");
        for (let i = 0; i < elements.length; i++) {
            let e = elements[i]
            e.setAttribute('data-aos', "zoom-in");
        }

    }
}

var x = window.matchMedia("(max-width: 992px)")
x.addEventListener("change", myProfile(x))



