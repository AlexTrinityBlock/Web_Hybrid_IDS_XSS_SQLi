<script>
    // @ts-nocheck

    import Nav from "../nav/nav.svelte";
    let data = null;
</script>

<Nav />

<div class="container">
    <div class="col-12">
        <br />
        <br />

        <!-- Result -->

        <div class="card card-frame">
            <div class="card input-card">
                <h1>Manual Input</h1>
                <div class="col-md-3">
                    <label for="input-ip" class="form-label">IP address</label>
                    <input
                        type="text"
                        class="form-control"
                        id="input-ip"
                        placeholder="0.0.0.0"
                    />
                </div>
                <br />
                <div class="col-md-12">
                    <label for="input-payload" class="form-label">Payload</label
                    >
                    <textarea
                        class="form-control"
                        id="input-payload"
                        rows="5"
                        placeholder="' or 1 = 1"
                    />
                </div>
                <br />
                <div class="col-md-12">
                    <button

                        type="button"
                        class="btn btn-outline-secondary"
                        id="ids-chat-btn"
                    >
                        <b>Submit</b>
                    </button>
                </div>
            </div>

            {#if data}
                <div class="card result-card">
                    <h1>Result</h1>
                    <p>
                        <b>result</b>:&nbsp;
                        <!-- {#if data.result == "True"} -->
                        <span class="badge text-bg-danger">
                            <!-- {data.result} -->
                        </span>
                        <!-- {:else if data.result == "False"} -->
                        <span class="badge text-bg-success">
                            <!-- {data.result} -->
                        </span>
                        <!-- {:else} -->
                        <span class="badge text-bg-warning">
                            <!-- {data.result} -->
                        </span>
                        <!-- {/if} -->
                    </p>

                    <p>
                        <!-- <b>from_ip</b>:&nbsp; {data.from_ip} -->
                    </p>

                    <p>
                        <!-- <b>SQLi probability</b>:&nbsp; {data.SQLi_probability} -->
                    </p>

                    <p>
                        <!-- <b>XSS probability</b>:&nbsp; {data.XSS_probability} -->
                    </p>

                    <p>
                        <!-- <b>Benign probability</b>:&nbsp; {data.Benign_probability} -->
                    </p>
                    <p>
                        <!-- <b>model type</b>:&nbsp; {data.model_type} -->
                    </p>
                    <p>
                        <!-- <b>timestamp</b>:&nbsp; {data.timestamp} -->
                    </p>
                    <div class="card result-card-payload">
                        <h4>Payload</h4>
                        <div class="card">
                            <!-- <p>{data.payload}</p> -->
                        </div>
                    </div>
                    <!-- {#if data.raw_gpt_response} -->
                    <div class="card result-card-analysis">
                        <h4>Analysis</h4>
                        <!-- <p>{data.raw_gpt_response}</p> -->
                    </div>
                    <!-- {/if} -->
                </div>
            {/if}
        </div>
    </div>
</div>

<style lang="scss">
    @import "/static/sass/home.sass";
</style>
