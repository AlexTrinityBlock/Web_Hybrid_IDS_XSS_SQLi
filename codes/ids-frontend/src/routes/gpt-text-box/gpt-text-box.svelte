<script>
    import { onMount } from "svelte";
    import { loadLogsAnalysiscache } from "$lib/gpt-text-box";
    onMount(async () => {});
</script>

<div class="container ids-chart-container">
    <div class="row">
        <div class="col-md-12">
            <div class="card" id="ids-chat-card">
                <div class="card-body">
                    <h5 class="card-title">Threat Analysis</h5>
                    <hr />
                    <p class="card-text">
                        Some quick example text to build on the card title and
                        make up the bulk of the card's content.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>
