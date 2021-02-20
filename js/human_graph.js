google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

setInterval(() => {
    google.charts.load('current', {'packages':['corechart']});
    
    google.charts.setOnLoadCallback(drawChart);
}, 1000);

let myPeople = new Array();
let myTime = new Array();
function Makerow(datat){ 
    fetch("http://158.108.182.18:3000/people_graph?f=0")
          .then((data1) => data1.json())
          .then((data1) => {
            myPeople = data1.result.people;
            myTime = data1.result.time;
          });
    for (let i=0; i<myTime.length; i++){
        datat.addRows([
            [myTime[i],  myPeople[i]]
        ]);
    }
    document.getElementById("time-of-graph").innerHTML = myTime[myTime.length-1];
    document.getElementById("people-of-graph").innerHTML = myPeople[myPeople.length-1] + "  " + "People";
}

function drawChart() {
    var datat = new google.visualization.DataTable();
    datat.addColumn('string', 'Time');
    datat.addColumn('number', 'People');
    
    Makerow(datat);
    
    var options = {
        //fontName: 'LucidaBrightRegular',
        title: 'Number of people use this room',
        height: 500,
        width: 900,
        //curveType: 'function',
        hAxis: {title: 'Time(sec)',
                titleTextStyle: {
                    color: '#000000'}
                },  
        vAxis: {title: 'People',
                titleTextStyle: {
                    color: '#000000'},
                ticks: [0, 1, 2, 3],
                //gridlines: { count: 5 }
        },
        lineWidth: 3,  
        colors: ['#191970'],
        //backgroundColor: '#D3D3D3',
        backgroundColor: {
                        stroke: '#000000',
                        strokeWidth: 5,
                        fill: '#FFFFCC'},
        legend: 'right',
        // animation: {
        //     //startup: true,
        //     duration: 500,
        //     easing: 'in',
        // }
    }
    
    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
    chart.draw(datat, options);
}
