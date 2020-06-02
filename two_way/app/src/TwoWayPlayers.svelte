<svelte:head>
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/handsontable/dist/handsontable.full.min.css"> -->
</svelte:head>

<script>
    import { restore, query } from 'svelte-apollo';
    // import Handsontable from "handsontable";
    import gql from 'graphql-tag';
    import { client } from './apollo';

    const TWO_WAY_PLAYERS = gql`{}` // TODO 
    const two_way_players = query(client, { query: TWO_WAY_CONTRACTS });
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