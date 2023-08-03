<script>
    import { statisticsLoop } from "$lib/statistics-loop";
    import { onMount } from "svelte";
    // On browser load
    onMount(async () => {
        statisticsLoop();
    });
</script>

<div class="container">
    <br />
    <div class="row" id="counter-body">
        <div class="col-md-4 text-center counter-block">
            <div class="counter-text" id="negative-request-block">
                <br />
                <div id="negative-request-title">Negative <br /> request</div>
                <br />
                <div id="negative-request-body" class="align-middle">0</div>
            </div>
        </div>
        <div class="col-md-4 text-center counter-block">
            <div class="counter-text" id="positive-request-block">
                <br />
                <div id="positive-request-title">Positive <br /> request</div>
                <br />
                <div id="positive-request-body" class="align-middle">0</div>
            </div>
        </div>
        <div class="col-md-4 text-center counter-block">
            <div class="counter-text" id="total-request-block">
                <br />
                <div id="total-request-title">Total <br /> request</div>
                <br />
                <div id="total-request-body" class="align-middle">0</div>
            </div>
        </div>
    </div>
</div>
