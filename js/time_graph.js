
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
google.charts.setOnLoadCallback(drawChart2);

setInterval(() => {
    google.charts.load('current', {'packages':['corechart']});
    
    google.charts.setOnLoadCallback(drawChart);
    google.charts.setOnLoadCallback(drawChart2);
}, 1000);

let myPeople = [];
let myTime = [];



function Makerow(datat){ 
    fetch("http://158.108.182.18:3000/people")
    .then((data1) => data1.json())
    .then((data1) => {
        for(let i=0; i<=2; i++){
            myTime[i]  = data1.result[i].time;
            myPeople[i] = data1.result[i].total_people;
        }
    });
    for(let j=0; j<=2; j++){
        datat.addRows([
            [myTime[j], myPeople[j]]
        ]) 
    }
}

function drawChart() {
    var datat = new google.visualization.DataTable();
    datat.addColumn('string', 'Time');
    datat.addColumn('number', 'People');
    
    Makerow(datat);


    var options = {
        //fontName: 'LucidaBrightRegular',
        title: 'Current amount of people in the room',
        titleTextStyle:{
            fontSize: 22
        },
        fontSize: 18,
        height: 400,
        width: 650,
        colors: ['#FFCC00', '#FF9999', '#FF6600'],
        //backgroundColor: '#D3D3D3',
        backgroundColor: {
                        stroke: '#000000',
                        strokeWidth: 5,
                        fill: '#FFFFCC'},
        legend: 'right',
        is3D: true,
        pieSliceTextStyle: {
            color: 'black',
        },
        //pieStartAngle: 90,
        //pieSliceText: 'value',
        
    }
    
    var chart = new google.visualization.PieChart(document.getElementById('curve_chart'));
    chart.draw(datat, options);
}


let myUse2 = [];
let myTime2 = [];

function Makerow2(datat2){ 
    fetch("http://158.108.182.18:3000/people")
    .then((data2) => data2.json())
    .then((data2) => {
        for(let i=0; i<=2; i++){
            myTime2[i]  = data2.result[i].time;
            myUse2[i] = data2.result[i].total_used_time;
        }
    });
    for(let j=0; j<=2; j++){
        datat2.addRows([
            [myTime2[j], myUse2[j]]
        ]) 
    }
}

function drawChart2() {
    var datat2 = new google.visualization.DataTable();
    datat2.addColumn('string', 'Time');
    datat2.addColumn('number', 'Usetime');
    
    Makerow2(datat2);


    var options2 = {
        //fontName: 'LucidaBrightRegular',
        title: 'Cumulated time of room used',
        titleTextStyle:{
            fontSize: 22
        },
        fontSize: 18,
        height: 400,
        width: 650,
        colors: ['#FFCC00', '#FF9999', '#FF6600'],
        //backgroundColor: '#D3D3D3',
        backgroundColor: {
                        stroke: '#000000',
                        strokeWidth: 5,
                        fill: '#FFFFCC'},
        legend: 'right',
        is3D: true,
        pieSliceTextStyle: {
            color: 'black',
        },
        pieStartAngle: 100,
        //pieSliceText: 'label',
        //slices: {  0: {offset: 0.2}},
    }
    
    var chart2 = new google.visualization.PieChart(document.getElementById('curve_chart2'));
    chart2.draw(datat2, options2);
}

var today = new Date();
var dd = String(today.getDate()-1).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); 
var yyyy = today.getFullYear();

today = mm + '/' + dd + '/' + yyyy;
document.getElementById("date").innerHTML = today