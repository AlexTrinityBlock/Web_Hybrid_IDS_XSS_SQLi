import { Chart } from "chart.js/auto";
import { getStatistics, getLastHoureEvents } from './call-api';

// Util
function addData(chart: any, label: any, newData: any) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset: any) => {
        dataset.data.push(newData);
    });
    chart.update();
}

function removeData(chart: any) {
    chart.data.labels.pop();
    chart.data.datasets.forEach((dataset: any) => {
        dataset.data.pop();
    });
    chart.update();
}

// IDS Doughnut Chart
export const idsDoughnutChart = async function () {

    const statisticsData: any = await getStatistics();
    // Recreate
    let idsDoughnutChartElement = <HTMLCanvasElement>document.getElementById('ids-doughnut-chart-canvas')
    let chart = Chart.getChart(idsDoughnutChartElement);

    //    Data prepare
    let statisticsDataArray = [];
    statisticsDataArray[0] = statisticsData.positive_number;
    statisticsDataArray[1] = statisticsData.negative_number;
    statisticsDataArray[2] = statisticsData.total_number - (statisticsData.positive_number + statisticsData.negative_number);

    let labels = [
        'Positive ',
        'Negative',
        'Unknow'
    ]

    let data = {
        labels: labels,
        datasets: [{
            label: 'Detction Result',
            data: statisticsDataArray,
            backgroundColor: [
                '#ff5000',
                '#057859',
                '#ffd800'
            ],
            // hoverOffset: 4,
            borderColor: '#1f3039'
        }]
    };

    if (chart == null) {
        let chartObj = new Chart(
            idsDoughnutChartElement,
            {
                type: 'doughnut',
                data: data,
                options: {

                    responsive: false,
                    plugins: {
                        title:{
                            display: true,
                            text:"Proportions",
                            color:'#fff',
                            font: {
                                size: 22,
                            }
                        },
                        legend: {
                            labels: {
                                // This more specific font property overrides the global property
                                font: {
                                    // size: 18,
                                },
                                color: "#fff",
                            }
                        }
                    },
                    animation: {
                        duration: 0
                    }
                }
            }
        );
        return chartObj;
    }

}

// IDS Bar Chart
export const idsBarChart = async function () {
    const result:any = await getLastHoureEvents();
    
    
    const idsBarChartElement = <HTMLCanvasElement>document.getElementById('ids-bar-chart-canvas')
    const labels = result.timeline;
    const data:any = {
        labels: labels,
        datasets: [{
            label: 'Positive',
            data: result.positive_time_log_list,
            fill: false,
            borderColor: '#ff5000',
            tension: 0.1,
            pointStyle: false,
        },
        {
            label: 'Negative',
            data: result.negative_time_log_list,
            fill: false,
            borderColor: '#057859',
            tension: 0.1,
            pointStyle: false,
        },
        {
            label: 'Unknow',
            data: result.unknown_time_log_list,
            fill: false,
            borderColor: '#ddf800',
            tension: 0.1,
            pointStyle: false,
        }
        ]
    };

    new Chart(idsBarChartElement, {
        type: 'line',
        data: data,
        options: {
            plugins: {
                title:{
                    display: true,
                    text:"Events",
                    color:'#fff',
                    font: {
                        size: 22,
                    }
                },
                legend: {
                    labels: {
                        // This more specific font property overrides the global property
                        font: {
                            // size: 18,
                        },
                        color: "#fff",
                    }
                }
            },
            animation: {
                duration: 0
            }
        }
    });
}