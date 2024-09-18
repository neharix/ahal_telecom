let status_desc = JSON.parse(document.querySelector("#status").textContent);

let cards_box = document.getElementById("cards-box");


function success(data) {
    try {
        let row = cards_box.querySelector("#" + data[0].device_type_slug);
        row.innerHTML = "";
        for (let i = 0; i < data.length; i++) {
            let card = document.createElement("div");
            card.setAttribute("class", "card");
            card.setAttribute("onclick", "location.href='/device/" + data[i].pk + "/'");
            let face1 = document.createElement("div");
            face1.setAttribute("class", "face face1");
            card.appendChild(face1);
            let content = document.createElement("div");
            content.setAttribute("class", "content");
            face1.appendChild(content);
            let stars_span = document.createElement("span");
            stars_span.setAttribute("class", "stars");
            let h2 = document.createElement("h2");
            h2.innerHTML = data[i].name;
            h2.setAttribute("class", "text");
            let p1 = document.createElement("p");
            p1.innerHTML = "Ýagdaýy: " + data[i].status;
            p1.setAttribute("class", "text");
            let p2 = document.createElement("p");
            p2.innerHTML = data[i].description;
            p2.setAttribute("class", "text");
            content.appendChild(stars_span);
            content.appendChild(h2);
            content.appendChild(p1);
            content.appendChild(p2);
            let face2 = document.createElement("div");
            face2.setAttribute("class", "face face2");
            face2.style = "background: linear-gradient(0deg, rgba(4, 21, 30, 0.6), rgba(5, 3, 59, 0.6)), url(/media/" + data[i].image + ");";
            console.log(face2.style);
            let device_name = document.createElement("h2");
            device_name.innerHTML = data[i].name;
            face2.appendChild(device_name);
            card.appendChild(face2);
            row.appendChild(card);
        }
    }
    catch {}
}



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

let rows = cards_box.querySelectorAll(".row");
rows.forEach(element => {
    element.innerHTML = "Hiç zat tapylmady"
    $.ajax({
        url: "/api/v1/devices/by_status/" + status_desc + "/"+ element.id +"/",
        type: 'GET',
        dataType: 'json',
        success: success,
    });
});