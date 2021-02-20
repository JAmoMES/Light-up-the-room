let m = {}; 
let a = {};
let e = {};


function getMorning(){
    
    url = "http://158.108.182.18.:3000/people"
    return fetch(url, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    })
    .then((data) => data.json())
    .then((result) => {
        m = {
            "key": result.result[0].total_people,
            "value": result.result[0].time
        }
    })
}


function getAfternoon(){
    
    url = "http://158.108.182.18.:3000/people"
    return fetch(url, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    })
    .then((data) => data.json())
    .then((result) => {
        a = {
            "key": result.result[1].total_people,
            "value": result.result[1].time
        }
    })
}


function getEvening(){
    
    url = "http://158.108.182.18.:3000/people"
    return fetch(url, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    })
    .then((data) => data.json())
    .then((result) => {
        e = {
            "key": result.result[2].total_people,
            "value": result.result[2].time
        }
    })
}


function getSuggest(){

    let array = [];
    let array2 = [];

    getMorning().then(() => {
       
        getAfternoon().then(() => {
        
            getEvening().then(() => {
                
                array.push(m);
                array.push(a);
                array.push(e);
                array2.push(array[0]["key"]);
                array2.push(array[1]["key"]);
                array2.push(array[2]["key"]);
                array2.sort();
                
                high_box = document.getElementById("high").checked;
                mid_box = document.getElementById("mid").checked;
                low_box = document.getElementById("low").checked;

                if(high_box){
                    for (let i = 0; i < 3; i++) {
                        if(array2[2] == array[i]["key"]){
                            console.log(array[i]["value"])
                            document.getElementById("output").innerHTML = array[i]["value"];
                            break;
                        }
                    }
                }

                if(mid_box){
                    for (let i = 0; i < 3; i++) {
                        if(array2[1] == array[i]["key"]){
                            console.log(array[i]["value"])
                            document.getElementById("output").innerHTML = array[i]["value"];
                            break;
                        }
                    }
                }

                if(low_box){
                    for (let i = 0; i < 3; i++) {
                        if(array2[0] == array[i]["key"]){
                            console.log(array[i]["value"])
                            document.getElementById("output").innerHTML = array[i]["value"];
                            break;
                        }
                    }
                }

                array.pop(m);
                array.pop(a);
                array.pop(e);
            })
        })
    })
}

document.getElementById("submit-button").onclick = getSuggest;
