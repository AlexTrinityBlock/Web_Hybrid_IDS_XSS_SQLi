<script>
    import { onMount } from "svelte";
    import { idsBarChart, idsDoughnutChart } from "$lib/ids-chart";
    // import
    onMount(async () => {
        idsDoughnutChart();
        idsBarChart();
    });
</script>

<br />

<div class="container ids-chart-container">
    <div class="row">
        <div class="col-md-6 ids-chart-col">
            <div id="ids-doughnut-chart-canvas-append-point">
                <canvas
                    height="400px"
                    width="400px"
                    id="ids-doughnut-chart-canvas"
                />
            </div>
        </div>
        <div class="col-md-6 ids-chart-col">
            <div>
                <canvas
                    height="400px"
                    width="400px"
                    id="ids-bar-chart-canvas"
                />
            </div>
        </div>
    </div>
</div>
