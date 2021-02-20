
var Time = ["Sec", "Min", "Hour"];

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

setInterval(() => {
    google.charts.load('current', {'packages':['corechart']});
    
    google.charts.setOnLoadCallback(drawChart);
}, 1000);

let Freq = 0;
let myCost = new Array();
let myTime = new Array();

function Makerow(datat0,Freq){ 
    
    fetch("http://158.108.182.18:3000/elecbill?f="+String(Freq))
          .then((data1) => data1.json())
          .then((data1) => {
            myCost = data1.result.cost;
            myTime = data1.result.time;
          });
    for (let i=1; i<myTime.length; i++){
        datat0.addRows([
            [String(myTime[i]),  myCost[i]*(10**4)]
        ]);
        // myTime[i] = 0;
        // myCost[i] = 0;
    }
    document.getElementById("time-of-graph").innerHTML = myTime[myTime.length-1];
    document.getElementById("cost-of-graph").innerHTML = myCost[myCost.length-1].toFixed(4) + "  " + "Baht";
}

function drawChart() {
    let f = Number(Freq);
    var datat0 = new google.visualization.DataTable();
        datat0.addColumn('string', 'Time');
        datat0.addColumn('number', 'Cost');
        Makerow(datat0,Freq);
    var optionsSec = {
        title: 'Total Cost',
        height: 500,
        width: 900,
        hAxis: {title: 'Time('+Time[f]+')',
                titleTextStyle: {
                    color: '#000000'}
                },  
        vAxis: {title: 'Cost(Baht) 10**(-4)',
                titleTextStyle: {
                    color: '#000000'},
                scaleType: 'log',
                gridlines: { count: 5 }
        },
        lineWidth: 3,  
        colors: ['#191970'],
        backgroundColor: {
                        stroke: '#000000',
                        strokeWidth: 5,
                        fill: '#FFFFCC'},
        legend: 'right',
    }
    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
    chart.draw(datat0, optionsSec);
}

function Second(){
    Freq = 0;
    setInterval(() => {
        google.charts.load('current', {'packages':['corechart']});
        
        google.charts.setOnLoadCallback(drawChart);
    }, 1000);
    document.getElementById("cost-label").innerHTML = "Current Cost Per Second"
}

function Minute(){
    Freq = 1;
    setInterval(() => {
        google.charts.load('current', {'packages':['corechart']});
        
        google.charts.setOnLoadCallback(drawChart);
    }, 1000);
    document.getElementById("cost-label").innerHTML = "Current Cost Per Minute"
}


function Hour(){
    Freq = 2;
    setInterval(() => {
        google.charts.load('current', {'packages':['corechart']});
        
        google.charts.setOnLoadCallback(drawChart);
    }, 1000);
    document.getElementById("cost-label").innerHTML = "Current Cost Per Hour"
}


document.getElementById("second").onclick = Second;
document.getElementById("minute").onclick = Minute;
document.getElementById("hour").onclick = Hour;

