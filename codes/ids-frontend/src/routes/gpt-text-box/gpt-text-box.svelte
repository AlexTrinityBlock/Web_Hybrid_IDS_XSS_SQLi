<script>
    import { onMount } from "svelte";
    import { loadLogsAnalysiscache, loadLogsAnalysis } from "$lib/gpt-text-box";
    onMount(async () => {
        loadLogsAnalysiscache();
    });
</script>

<div class="container ids-chart-container">
    <div class="row">
        <div class="col-md-12">
            <div class="card" id="ids-chat-card">
                <div class="card-body text-center">
                    <h1 class="card-title">Threat Analysis</h1>
                    <hr />
                    <div class="text-start" id='ids-chat-content'>
                        <p class="card-text" id="ids-chat-analysis-text">
                            None
                        </p>
                    </div>
                    <hr />
                    <div
                        class="spinner-border text-warning"
                        role="status"
                        id="ids-chat-spinner"
                    />
                    <button
                        on:click={loadLogsAnalysis}
                        type="button"
                        class="btn btn-outline-secondary"
                        id="ids-chat-btn"
                    >
                        <b>Update</b>
                    </button>
                </div>
            </div>
            <br />
        </div>
    </div>
</div>
