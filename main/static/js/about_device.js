let box = document.getElementById("box");

function progressBar() {
    let scroll = box.scrollTop;
    let height = box.scrollHeight - box.clientHeight;
    let scrolled = (scroll / height) * 100;
    document.getElementById("progress-bar").style.width = scrolled + "%";
}
function resize(e) {
    let height = window.innerHeight - 85;
    box.style = "height: " + height + "px;"
}
let height = window.innerHeight - 85;
box.style = "height: " + height + "px;"

window.onresize = resize;
box.addEventListener("scroll", progressBar);
