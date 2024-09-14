let cards_box = document.getElementById("cards-box");


function progressBar() {
    let scroll = cards_box.scrollTop;
    let height = cards_box.scrollHeight - cards_box.clientHeight;
    let scrolled = (scroll / height) * 100;
    document.getElementById("progress-bar").style.width = scrolled + "%";
}
function resize(e) {
    let height = window.innerHeight - 150;
    cards_box.style = "height: " + height + "px;"
}
let height = window.innerHeight - 150;
cards_box.style = "height: " + height + "px;"

window.onresize = resize;
cards_box.addEventListener("scroll", progressBar);


