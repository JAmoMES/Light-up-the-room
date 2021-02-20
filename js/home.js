function map_color(x){
    if(x == false){
        return 0;
    }
    if(x == true){
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
    console.log("yep")
    fetch("http://158.108.182.18:3000/switch", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ID: id, Status: status, b: b_value, g: g_value, r: r_value, w: w_value }),
    })
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.log("error", error));
}

// // สร้าง function ไว้ส่งข้อมูล2
// function open_update(r_value, g_value, b_value, w_value, status, id) {
//     fetch("http://158.108.182.18:3000/switch", {
//       method: "PATCH",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify({ ID: id, Status: status, b: b_value, g: g_value, r: r_value, w: w_value }),
//     })
//       .then((response) => response.text())
//       .then((result) => console.log(result))
//       .catch((error) => console.log("error", error));
// }


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

// switch color
let grey_color = "rgba(107, 107, 107, 0.7)";
let yellow_color = "rgba(255, 255, 0, 0.8)";
let white_color = "rgba(255, 255, 255, 0.8)";
let red_color =  "rgba(255, 0, 0, 0.8)";
let green_color = "rgba(0, 255, 0, 0.8)";
let blue_color = "rgba(0, 0, 255, 0.8)";

function status1_set_light_on() {

    document.getElementById("status1_text").innerHTML = "ON";
    document.getElementById("status1").style.background = yellow_color;

    white1 = document.getElementById("whiteswitch1").checked
    red1 = document.getElementById("redswitch1").checked
    green1 = document.getElementById("greenswitch1").checked
    blue1 = document.getElementById("blueswitch1").checked

    if (white1 == false && red1 == false && green1 == false && blue1 == false){
        document.getElementById("w1").style.background = white_color; 
        white1 = true;
        document.getElementById("whiteswitch1").checked = true;
    }

    else{
    
        if (white1 == true) {
            document.getElementById("w1").style.background = white_color;
        }

        if (red1 == true) {
            document.getElementById("r1").style.background = red_color;
        }
    
        if (green1 == true) {
            document.getElementById("g1").style.background = green_color;
        }
    
        if (blue1 == true) {
            document.getElementById("b1").style.background = blue_color;
        }
    }
    

    // update database

    // if(checkStatus(1) == 1){
  
    //     open_update(map_color(red1), map_color(green1), map_color(blue1), map_color(white1), 1, 1);
    // }

    //else if(checkStatus(1) != 1){
    open_new(map_color(red1), map_color(green1), map_color(blue1), map_color(white1), 1, 1);
    //}

}

function status1_set_light_off() {
    document.getElementById("status1_text").innerHTML = "OFF";
    document.getElementById("status1").style.background = grey_color;
    document.getElementById("w1").style.background = grey_color;
    document.getElementById("r1").style.background = grey_color;
    document.getElementById("g1").style.background = grey_color;
    document.getElementById("b1").style.background = grey_color;
    
    ws1 = document.getElementById("whiteswitch1");
    rs1 = document.getElementById("redswitch1");
    gs1 = document.getElementById("greenswitch1");
    bs1 = document.getElementById("blueswitch1");

    ws1.checked = false;
    rs1.checked = false;
    gs1.checked = false;
    bs1.checked = false;

    close(1);
}

function status2_set_light_on() {
    document.getElementById("status2_text").innerHTML = "ON";
    document.getElementById("status2").style.background = "yellow";

    white2 = document.getElementById("whiteswitch2").checked
    red2 = document.getElementById("redswitch2").checked
    green2 = document.getElementById("greenswitch2").checked
    blue2 = document.getElementById("blueswitch2").checked

    if (white2 == false && red2 == false && green2 == false && blue2 == false){
        document.getElementById("w2").style.background = white_color; 
        white2 = true;
        document.getElementById("whiteswitch2").checked = true;
    }

    else{
    
        if (white2 == true) {
            document.getElementById("w2").style.background = white_color;
        }

        if (red2 == true) {
            document.getElementById("r2").style.background = red_color;
        }
    
        if (green2 == true) {
            document.getElementById("g2").style.background = green_color;
        }
    
        if (blue2 == true) {
            document.getElementById("b2").style.background = blue_color;
        }
    }
   

    // if(checkStatus(2) == 1){
    //     open_update(red1, green1, blue1, white1, 1, 2);
    // }

    // else if(checkStatus(2) != 1){
    open_new(map_color(red2), map_color(green2), map_color(blue2), map_color(white2), 1, 2);
    // }
}

function status2_set_light_off() {
    document.getElementById("status2_text").innerHTML = "OFF";
    document.getElementById("status2").style.background = grey_color;
    document.getElementById("w2").style.background = grey_color;
    document.getElementById("r2").style.background = grey_color;
    document.getElementById("g2").style.background = grey_color;
    document.getElementById("b2").style.background = grey_color;

    ws2 = document.getElementById("whiteswitch2");
    rs2 = document.getElementById("redswitch2");
    gs2 = document.getElementById("greenswitch2");
    bs2 = document.getElementById("blueswitch2");

    ws2.checked = false;
    rs2.checked = false;
    gs2.checked = false;
    bs2.checked = false;
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
    
    ws1 = document.getElementById("whiteswitch1");
    rs1 = document.getElementById("redswitch1");
    gs1 = document.getElementById("greenswitch1");
    bs1 = document.getElementById("blueswitch1");

    if (status1 == 0){
        document.getElementById("status1").style.background = grey_color;
    }

    if (status1 == 1) {
        document.getElementById("status1_text").innerHTML = "ON";
        document.getElementById("status1").style.background = yellow_color;
    }

    if (white1 == 0){
        document.getElementById("w1").style.background = grey_color;
        ws1.checked = false;
    }

    if (white1 == 1) {
        document.getElementById("w1").style.background = white_color;
        ws1.checked = true;
    }

    if (red1 == 0){
        document.getElementById("r1").style.background = grey_color;
        rs1.checked = false;
    }

    if (red1 == 1) {
        document.getElementById("r1").style.background = red_color;
        rs1.checked = true;
    }

    if (green1 == 0) {
        document.getElementById("g1").style.background = grey_color;
        gs1.checked = false;
    }

    if (green1 == 1) {
        document.getElementById("g1").style.background = green_color;
        gs1.checked = true;
    }

    if (blue1 == 0) {
        document.getElementById("b1").style.background = grey_color;
        bs1.checked = false;
    }

    if (blue1 == 1) {
        document.getElementById("b1").style.background = blue_color;
        bs1.checked = true;
    }
}

function update2(){

    ws2 = document.getElementById("whiteswitch2");
    rs2 = document.getElementById("redswitch2");
    gs2 = document.getElementById("greenswitch2");
    bs2 = document.getElementById("blueswitch2");

    if (status2 == 0){
        document.getElementById("status2").style.background = grey_color;
    }

    if (status2 == 1) {
        document.getElementById("status2_text").innerHTML = "ON";
        document.getElementById("status2").style.background = yellow_color;
    }

    if (white2 == 0){
        document.getElementById("w2").style.background = grey_color;
        ws2.checked = false;
    }

    if (white2 == 1) {
        document.getElementById("w2").style.background = white_color;
        ws2.checked = true;
    }

    if (red2 == 0){
        document.getElementById("r2").style.background = grey_color;
        rs2.checked = false;
    }

    if (red2 == 1) {
        document.getElementById("r2").style.background = red_color;
        rs2.checked = true;
    }

    if (green2 == 0) {
        document.getElementById("g2").style.background = grey_color;
        gs2.checked = false;
    }

    if (green2 == 1) {
        document.getElementById("g2").style.background = green_color;
        gs2.checked = true;
    }

    if (blue2 == 0) {
        document.getElementById("b2").style.background = grey_color;
        bs2.checked = false;
    }

    if (blue2 == 1) {
        document.getElementById("b2").style.background = blue_color;
        bs2.checked = true;
    }
}

let full1 = null;
let full2 = null;

function getFull1(){
    
    url = "http://158.108.182.18:3000/switch?ID=1"
    return fetch(url, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    })
    .then((data) => data.json())
    .then((result) => {
        full1 = result.result.Status
    })
}

function getFull2(){
    
    url = "http://158.108.182.18:3000/switch?ID=2"
    return fetch(url, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    })
    .then((data) => data.json())
    .then((result) => {
        full2 = result.result.Status
    })
}

let f1 = false;
let f2 = false;

function checkFull(){
    getFull1().then(() => {
        if(full1 == 1){
            f1 = true;
        }
        getFull2().then(() => {
            if(full2 == 1){
                f2 = true;
            }
            if (f1 == true && f2 == true){
                document.getElementById("header_alert").style.visibility = "visible"
            }
        })
    })
}

getStatusUpdate1().then(() => {
    update1();
    checkFull();
})

getStatusUpdate2().then(() => {
    update2();
    checkFull();
})

document.getElementById("turn_on1").onclick = status1_set_light_on;
document.getElementById("turn_off1").onclick = status1_set_light_off;

document.getElementById("turn_on2").onclick = status2_set_light_on;
document.getElementById("turn_off2").onclick = status2_set_light_off;




