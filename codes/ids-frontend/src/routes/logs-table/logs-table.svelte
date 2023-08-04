<script>
    import { page } from "$app/stores";
    import { getLogsByID } from "$lib/call-api";
    import { onMount } from "svelte";
    import { loadLogsData } from "$lib/logs-tables";

    const pageNumber = Number($page.params.slug);
    /**
     * @type {any[]}
     */
    let dataObj = [];
    onMount(async () => {
        dataObj = await loadLogsData(pageNumber);
    });
</script>

<div class="container-fluid">
    <div class="col-12">
        <br />
        <br />
        <div class="card">
            <h1>Logs</h1>
            <hr />
            {#each dataObj as data} 
                {data.id}
            {/each}
        </div>
    </div>
</div>
