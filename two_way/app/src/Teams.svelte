<script context="module">
    // import Handsontable from "handsontable";
    import gql from 'graphql-tag';
    import { client } from './apollo';
    import { TEAMS } from './queries';

    export async function preload() {
        return {
            cache: await client.query({ query: TEAMS })
        };
    }
</script>

<script>
    import { restore, query } from 'svelte-apollo';

    export let cache;
    restore(client, TEAMS, cache.data);

    let teams = query(client, { query: TEAMS });
</script>

<style>
    .team-logos {
        display: table;
    }
</style>

<div class="team-logos">
    {#await $teams}
        Loading teams...
    {:then result}
        {#each result.data.team as team (team.teamId)}
            <img src={team.teamLogoURL} alt="Logo of NBA/G-League team" style="height:100px;">
        {:else}
            <li>No teams found</li>
        {/each}
    {:catch error}
        Error on loading teams.
    {/await}
</div>