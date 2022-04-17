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




// //State card
// function changeDefOver() {
//     let e = document.getElementById("state_id")
//     e.setAttribute('data-aos', "zoom-in");


// }

// function changeDefOut() {
//     let e = document.getElementById("state_id")
//     e.setAttribute('data-aos', "zoom-out");


// }
// var states = document.querySelectorAll('#state_id');
// for (let i = 0; i < states.length; i++) {
//     let s = states[i];
//     s.addEventListener('mouseover', changeDefOver);
//     s.addEventListener('mouseout', changeDefOut);


// }