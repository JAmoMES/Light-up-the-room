function map_color(x){
    if(x = false){
        return 0;
    }
    if(x = true){
        return 1;
    }
}

let status = null

function getStatus(light){
    
    url = "http://158.108.182.18:3000/switch?ID=" + String(light)
    return fetch(url, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    })
    .then((data) => data.json())
    .then((result) => {
        status = result.result.Status
    })
}

function checkStatus(light){

    getStatus(light).then(() => {
        console.log(status)
        if (status == 0){
            return false
        }
        if (status == 1){
            return true
        }
    });
}

// สร้าง function ไว้ส่งข้อมูล1
function open_new(r_value, g_value, b_value, w_value, status, id) {
    fetch("http://158.108.182.18:3000/switch", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ID: id, Status: status, b: 1, g: 1, r: 1, w: 1 }),
    })
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.log("error", error));
}

// สร้าง function ไว้ส่งข้อมูล2
function open_update(r_value, g_value, b_value, w_value, status, id) {
    fetch("http://158.108.182.18:3000/switch", {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ID: id, Status: status, b: 0, g: 1, r: 0, w: 1 }),
    })
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.log("error", error));
}


function close(id) {
    fetch("http://158.108.182.18:3000/switch", {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ID: id, Status: 0, b: 0, g: 0, r: 0, w: 0 }),
    })
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.log("error", error));
}


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

    // update database

    if(checkStatus(1) == 1){
        console.log("ok")
        open_update(map_color(red1), map_color(green1), map_color(blue1), map_color(white1), 1, 1);
    }

    else if(checkStatus(1) != 1){
        console.log("not ok")
        open_new(map_color(red1), map_color(green1), map_color(blue1), map_color(white1), 1, 1);
    }

}

function status1_set_light_off() {
    document.getElementById("status1_text").innerHTML = "OFF";
    document.getElementById("status1").style.background = "grey";
    document.getElementById("w1").style.background = "grey";
    document.getElementById("r1").style.background = "grey";
    document.getElementById("g1").style.background = "grey";
    document.getElementById("b1").style.background = "grey";
    close(1);
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

    if(checkStatus(2) == 1){
        open_update(map_color(red1), map_color(green1), map_color(blue1), map_color(white1), 1, 2);
    }

    else if(checkStatus(2) != 1){
        open_new(map_color(red1), map_color(green1), map_color(blue1), map_color(white1), 1, 2);
    }
}

function status2_set_light_off() {
    document.getElementById("status2_text").innerHTML = "OFF";
    document.getElementById("status2").style.background = "grey";
    document.getElementById("w2").style.background = "grey";
    document.getElementById("r2").style.background = "grey";
    document.getElementById("g2").style.background = "grey";
    document.getElementById("b2").style.background = "grey";
    close(2);
}

let status1 = null;
let red1 = null;
let green1 = null;
let blue1 = null;
let white1 = null;

let status2 = null;
let red2 = null;
let green2 = null;
let blue2 = null;
let white2 = null;

function getStatusUpdate1(){
    
    url = "http://158.108.182.18:3000/switch?ID=1"
    return fetch(url, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    })
    .then((data) => data.json())
    .then((result) => {
        status1 = result.result.Status
        red1 = result.result.r
        green1 = result.result.g
        blue1 = result.result.b
        white1 = result.result.w
    })
}

function getStatusUpdate2(){
    
    url = "http://158.108.182.18:3000/switch?ID=2"
    return fetch(url, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    })
    .then((data) => data.json())
    .then((result) => {
        status2 = result.result.Status
        red2 = result.result.r
        green2 = result.result.g
        blue2 = result.result.b
        white2 = result.result.w
    })
}

function update1(){

    if (status1 == 0){
        document.getElementById("status1").style.background = "grey";
    }

    if (status1 == 1) {
        document.getElementById("status1_text").innerHTML = "ON";
        document.getElementById("status1").style.background = "yellow";
    }

    if (white1 == 0){
        document.getElementById("w1").style.background = "grey";
    }

    if (white1 == 1) {
        document.getElementById("w1").style.background = "white";
    }

    if (red1 == 0){
        document.getElementById("r1").style.background = "grey";
    }

    if (red1 == 1) {
        document.getElementById("r1").style.background = "red";
    }

    if (green1 == 0) {
        document.getElementById("g1").style.background = "grey";
    }

    if (green1 == 1) {
        document.getElementById("g1").style.background = "green";
    }

    if (blue1 == 0) {
        document.getElementById("b1").style.background = "grey";
    }

    if (blue1 == 1) {
        document.getElementById("b1").style.background = "blue";
    }
}

function update2(){

    if (status2 == 0){
        document.getElementById("status2").style.background = "grey";
    }

    if (status2 == 1) {
        document.getElementById("status2_text").innerHTML = "ON";
        document.getElementById("status2").style.background = "yellow";
    }

    if (white2 == 0){
        document.getElementById("w2").style.background = "grey";
    }

    if (white2 == 1) {
        document.getElementById("w2").style.background = "white";
    }

    if (red2 == 0){
        document.getElementById("r2").style.background = "grey";
    }

    if (red2 == 1) {
        document.getElementById("r2").style.background = "red";
    }

    if (green2 == 0) {
        document.getElementById("g2").style.background = "grey";
    }

    if (green2 == 1) {
        document.getElementById("g2").style.background = "green";
    }

    if (blue2 == 0) {
        document.getElementById("b2").style.background = "grey";
    }

    if (blue2 == 1) {
        document.getElementById("b2").style.background = "blue";
    }
}


getStatusUpdate1().then(() => {
    update1();
})

getStatusUpdate2().then(() => {
    update2();
})



document.getElementById("turn_on1").onclick = status1_set_light_on;
document.getElementById("turn_off1").onclick = status1_set_light_off;

document.getElementById("turn_on2").onclick = status2_set_light_on;
document.getElementById("turn_off2").onclick = status2_set_light_off;




