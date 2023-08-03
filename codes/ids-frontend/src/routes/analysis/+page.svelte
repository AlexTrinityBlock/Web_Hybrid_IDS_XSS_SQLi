<script>
    import { onMount } from "svelte";
    import { detectLocal } from "$lib/call-api";
    import Nav from "../nav/nav.svelte";
    import GptTextBox from "../gpt-text-box/gpt-text-box.svelte";
    // On browser load
    onMount(async () => {});
</script>

<Nav />
<GptTextBox />

<style lang="scss">
    @import "/static/sass/home.sass";
</style>
