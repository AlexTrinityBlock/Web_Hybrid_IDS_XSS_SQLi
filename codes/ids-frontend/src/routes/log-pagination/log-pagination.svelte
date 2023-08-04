<script>
// @ts-nocheck

    import { page } from "$app/stores";
    import { getLogPagination } from "$lib/log-pagination";
    import { onMount } from "svelte";

    // @ts-ignore
    let logPaginationDatas = [];
    onMount(async () => {
        logPaginationDatas = await getLogPagination(
            Number($page.params.slug)
        );
    });
</script>

<br />
<div class="container">
    <div class="row">
        <div class="col">
            <nav aria-label="Page navigation example">
                <ul
                    class="pagination justify-content-center"
                    id="log-pagination"
                >
                    {#each logPaginationDatas as logPaginationData}
                        <li class="page-item">
                            <a data-sveltekit-reload class="page-link" href={logPaginationData.url} aria-label="Previous">
                                <span aria-hidden="true">{logPaginationData.token}</span>
                            </a>
                        </li>
                    {/each}
                </ul>
            </nav>
        </div>
    </div>
</div>
<br />
