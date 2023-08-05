<script>
    import { onMount } from "svelte";
    import { detectLocal } from "$lib/call-api";
    import Nav from "./nav/nav.svelte";
    import Statistics from "./statistics/statistics.svelte";
    import IdsChart from "./ids-chart/ids-chart.svelte";
    import HomeRefreshBtn from "./refresh-btn/home-refresh-btn.svelte";
    // On browser load
    onMount(async () => {});
    let updateElement = {};
    let update = () => {
        updateElement = {};
    };
    setInterval(update, 10000);
</script>

<Nav />
<!-- For Update Chart -->
<div style="min-height: 500px; display:relative">
    {#key updateElement}
        <IdsChart />
    {/key}
</div>
<Statistics />

<!-- <HomeRefreshBtn /> -->

<style lang="scss">
    @import "/static/sass/home.sass";
</style>
