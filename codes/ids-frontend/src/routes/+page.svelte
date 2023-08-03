<script>
    import { onMount } from "svelte";
    import { detectLocal } from "$lib/call-api";
    import Nav from "./nav/nav.svelte";
    import Statistics from "./statistics/statistics.svelte";
    import IdsChart from "./ids-chart/ids-chart.svelte";
    import HomeRefreshBtn from "./refresh-btn/home-refresh-btn.svelte";
    // On browser load
    onMount(async () => {
        await import("bootstrap");
    });
</script>

<Nav />
<IdsChart />
<Statistics />
<HomeRefreshBtn />

<style lang="scss">
    @import "/static/sass/home.sass";
</style>
