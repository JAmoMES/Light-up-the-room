var Time = ["Sec", "Min", "Hour"];

function drawChart(Freq) {

    let f = Number(Freq);
    var datat0 = new google.visualization.DataTable();
        datat0.addColumn('string', 'Time');
        datat0.addColumn('number', 'Cost');
        Makerow(datat0);
    var optionsSec = {
        title: 'Total Cost',
        height: 500,
        width: 900,
        hAxis: {title: 'Time('+Time[f]+')',
                titleTextStyle: {
                    color: '#000000'}
                },  
        vAxis: {title: 'Cost(Baht)',
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

function Makerow(datat0,Freq){ 
    let myCost = new Array();
    let myTime = new Array();
    fetch("http://158.108.182.18:3000/elecbill?f="+String(Freq))
          .then((data1) => data1.json())
          .then((data1) => {
            myCost = data1.result.cost;
            myTime = data1.result.time;
          });
    for (let i=0; i<myTime.length; i++){
        datat0.addRows([
            [myTime[i],  myCost[i]*(10**4)]
        ]);
    }
    document.getElementById("time-of-graph").innerHTML = myTime[myTime.length-1];
    document.getElementById("cost-of-graph").innerHTML = myCost[myCost.length-1] + "  " + "Baht";
}