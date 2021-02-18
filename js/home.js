// $(document).ready(function(){
//     $('.header').height($(window).height());
// })

// var ready = (callback) => {
//     if (document.readyState != "loading") callback();
//     else document.addEventListener("DOMContentLoaded", callback);
// }

// function getColor(){
//     // return array and send to database
// }

// function selectColor(){
//     // get color in checkbox and put in to array
// }

// // สร้าง function ไว้ส่งข้อมูล
// function scream() {
//     fetch("???", {
//       method: "POST",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify({ author: author, content: content }),
//     })
//       .then((response) => response.text())
//       .then((result) => console.log(result))
//       .catch((error) => console.log("error", error));
// }

function status1_set_light_on() {
    document.getElementById("status1_text").innerHTML = "ON";
    document.getElementById("status1").style.background = "yellow";

    white1 = document.getElementById("white1").checked
    red1 = document.getElementById("red1").checked
    green1 = document.getElementById("green1").checked
    blue1 = document.getElementById("blue1").checked

    if (white1 == false){
        document.getElementById("w1").style.background = "grey";
    }

    if (white1 == true) {
        document.getElementById("w1").style.background = "white";
    }

    if (red1 == false){
        document.getElementById("r1").style.background = "grey";
    }

    if (red1 == true) {
        document.getElementById("r1").style.background = "red";
    }

    if (green1 == false) {
        document.getElementById("g1").style.background = "grey";
    }

    if (green1 == true) {
        document.getElementById("g1").style.background = "green";
    }

    if (blue1 == false) {
        document.getElementById("b1").style.background = "grey";
    }

    if (blue1 == true) {
        document.getElementById("b1").style.background = "blue";
    }
}

function status1_set_light_off() {
    document.getElementById("status1_text").innerHTML = "OFF";
    document.getElementById("status1").style.background = "grey";
    document.getElementById("w1").style.background = "grey";
    document.getElementById("r1").style.background = "grey";
    document.getElementById("g1").style.background = "grey";
    document.getElementById("b1").style.background = "grey";
}

function status2_set_light_on() {
    document.getElementById("status2_text").innerHTML = "ON";
    document.getElementById("status2").style.background = "yellow";

    white2 = document.getElementById("white2").checked
    red2 = document.getElementById("red2").checked
    green2 = document.getElementById("green2").checked
    blue2 = document.getElementById("blue2").checked

    if (white2 == false) {
        document.getElementById("w2").style.background = "grey";
    }

    if (white2 == true) {
        document.getElementById("w2").style.background = "white";
    }

    if (red2 == false) {
        document.getElementById("r2").style.background = "grey";
    }

    if (red2 == true) {
        document.getElementById("r2").style.background = "red";
    }

    if (green2 == false) {
        document.getElementById("g2").style.background = "grey";
    }

    if (green2 == true) {
        document.getElementById("g2").style.background = "green";
    }

    if (blue2 == false) {
        document.getElementById("b2").style.background = "grey";
    }

    if (blue2 == true) {
        document.getElementById("b2").style.background = "blue";
    }
}

function status2_set_light_off() {
    document.getElementById("status2_text").innerHTML = "OFF";
    document.getElementById("status2").style.background = "grey";
    document.getElementById("w2").style.background = "grey";
    document.getElementById("r2").style.background = "grey";
    document.getElementById("g2").style.background = "grey";
    document.getElementById("b2").style.background = "grey";
}


document.getElementById("turn_on1").onclick = status1_set_light_on;
document.getElementById("turn_off1").onclick = status1_set_light_off;

document.getElementById("turn_on2").onclick = status2_set_light_on;
document.getElementById("turn_off2").onclick = status2_set_light_off;


