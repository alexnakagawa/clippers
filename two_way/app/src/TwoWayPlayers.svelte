<svelte:head>
    <script src="node_modules/handsontable/dist/handsontable.full.min.js"></script>
    <link href="node_modules/handsontable/dist/handsontable.full.min.css" rel="stylesheet" media="screen">
</svelte:head>

<script context='module'>
    import gql from 'graphql-tag';
    import { client } from './apollo';

    const TWO_WAY_PLAYERS = gql`{}` // TODO 
    export async function preload() {
        return {
            cache: await client.query({ query: TWO_WAY_CONTRACTS })
        };
    }
</script>

<script>
    import { restore, query } from 'svelte-apollo';
  
    export let cache;
    restore(client, TWO_WAY_PLAYERS, cache.data);

    const two_way_players = query(client, { query: TWO_WAY_CONTRACTS });

    var table = document.getElementById('example')
    new Handsontable(table, {
        data: two_way_players.result.data, // TODO: this may be incorrect
        colHeaders: [],
        columnSorting: true
    })
</script>

<ul>
    {#await $two_way_players}
        <li>Loading players...</li>
    {:then result}
        {#each result.data.two_way_player as player (player.playerId)}
            <li>Player ID: {player.playerId}</li>
            <li>Full Name: {player.rosterFirstName} {player.rosterLastName}</li>
            <li>Total Days: {player.totalDays}</li>
            <li>Active NBA Days: {player.activeForNbaGameDays}</li>
            <li>Non-NBA Days: {player.nonNbaDays}</li>
            <li>Non-NBA G League Days: {player.nonNbaGlgDays}</li>
        {:else}
            <li>No players found.</li>
        {/each}
    {:catch error}
        <li>There was an error loading the players.</li>
    {/await}
</ul>