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
        // @ts-ignore
        dataObj = await loadLogsData(pageNumber);
    });
</script>

<div class="container">
    <div class="col-12">
        <br />
        <br />
        <div class="card log-card-frame">
            <h1>Logs</h1>
            <hr />
            {#each dataObj as data}
                <div class="card log-card">
                    <h2>#{data.id}</h2>
                    <p>
                        <b>result</b>:&nbsp;
                        {#if data.result == "True"}
                            <span class="badge text-bg-danger">
                                {data.result}
                            </span>
                        {:else if data.result == "False"}
                            <span class="badge text-bg-success">
                                {data.result}
                            </span>
                        {:else}
                            <span class="badge text-bg-warning">
                                {data.result}
                            </span>
                        {/if}
                    </p>

                    <p>
                        <b>from_ip</b>:&nbsp; {data.from_ip}
                    </p>
                    {#if data.SQLi_probability}
                        <p>
                            <b>SQLi probability</b>:&nbsp;
                            {String((data.SQLi_probability * 100).toFixed(2)) + "%"}
                        </p>

                        <p>
                            <b>XSS probability</b>:&nbsp;
                            {String((data.XSS_probability * 100).toFixed(2)) + "%"}
                        </p>

                        <p>
                            <b>Benign probability</b>:&nbsp;
                            {String((data.Benign_probability * 100).toFixed(2)) + "%"}
                        </p>
                    {/if}
                    <p>
                        <b>model type</b>:&nbsp; {data.model_type}
                    </p>
                    <p>
                        <b>timestamp</b>:&nbsp; {data.timestamp}
                    </p>
                    <div class="card log-card-payload">
                        <h4>Payload</h4>
                        <div class="card">
                            <p>{data.payload}</p>
                        </div>
                    </div>
                    {#if data.raw_gpt_response}
                        <div class="card log-card-analysis">
                            <h4>Analysis</h4>
                            <p>{data.raw_gpt_response}</p>
                        </div>
                    {/if}
                </div>
            {/each}
        </div>
    </div>
</div>
