<script>
    import Nav from "../../nav/nav.svelte";
    import LogsTable from "../../logs-table/logs-table.svelte";
    import LogPagination from "../../log-pagination/log-pagination.svelte";
</script>

<Nav />
<LogsTable />
<LogPagination />

<style lang="scss">
    @import "/static/sass/home.sass";
</style>
