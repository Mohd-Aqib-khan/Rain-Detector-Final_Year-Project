function pieChart(data, id, statename1, statename2, name) {
    let pie_data = data
    const ctxPie = document.getElementById(id).getContext('2d');
    const myChartPie = new Chart(ctxPie, {
        type: 'doughnut',
        data: {
            labels: [statename1, statename2],
            datasets: [{
                label: name,
                data: pie_data,
                backgroundColor: [
                    'rgba(255, 99, 142, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                ],
                hoverOffset: 4
            }]
        },
        options: {
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Pie Chart Reprsentation'
                },
            },
        }
    });
    return myChartPie;
}

function barChart(data1, data2, id, statename1, statename2, name) {
    let col = [];
    let dat1 = [];
    let dat2 = [];
    name.forEach((value, index) => {
        col.push(value);
    })
    data1.forEach((value, index) => {
        dat1.push(value);
    })
    data2.forEach((value, index) => {
        dat2.push(value);
    })
    const ctxLine2 = document.getElementById(id).getContext('2d');
    const mybarChart = new Chart(ctxLine2, {
        type: 'bar',
        data: {
            labels: col,
            datasets: [
                {
                    label: statename1,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    data: dat1,
                    borderWidth: 1
                },
                {
                    label: statename2,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    data: dat2,
                    borderWidth: 1
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    return mybarChart;
}

function lineChart(data, colour, id, name) {
    const totalDuration = 10000;
    const delayBetweenPoints = totalDuration / data.length;
    const previousY = (ctx) => ctx.index === 0 ? ctx.chart.scales.y.getPixelForValue(100) : ctx.chart.getDatasetMeta(ctx
        .datasetIndex).data[ctx.index - 1].getProps(['y'], true).y;
    const ctx = document.getElementById(id).getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [{
                label: name,
                borderColor: colour,
                borderWidth: 1,
                radius: 2,
                data: data,
            }
                /*{
                    label: stateSecond,
                    borderColor: '#f67019',
                    borderWidth: 1,
                    radius: 3,
                    data: data2,
                }*/
            ]
        },
        options: {
            animation: {
                x: {
                    type: 'number',
                    easing: 'linear',
                    duration: delayBetweenPoints,
                    from: NaN, // the point is initially skipped
                    delay(ctx) {
                        if (ctx.type !== 'data' || ctx.xStarted) {
                            return 0;
                        }
                        ctx.xStarted = true;
                        return ctx.index * delayBetweenPoints;
                    }
                },
                y: {
                    type: 'number',
                    easing: 'linear',
                    duration: delayBetweenPoints,
                    from: previousY,
                    delay(ctx) {
                        if (ctx.type !== 'data' || ctx.yStarted) {
                            return 0;
                        }
                        ctx.yStarted = true;
                        return ctx.index * delayBetweenPoints;
                    }
                }
            },
            responsive: false,
            interaction: {
                intersect: false
            },
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Annual Rainfall'
                },
            },
            scales: {
                x: {
                    type: 'linear'
                }
            }
        }
    });
    return myChart;
}