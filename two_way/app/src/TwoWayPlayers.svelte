<svelte:head>
	<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</svelte:head>

<script context="module">
    // import Handsontable from "handsontable";
    import gql from 'graphql-tag';
    import { client } from './apollo';

    const TWO_WAY_PLAYERS = gql`{
        two_way_headshots(order_by: {withNbaDays: desc}) {
            playerId
            player
            totalDays
            withNbaDays
            activeForNbaGameDays
            travelWithNbaDays
            nonNbaDays
            nonNbaGlgDays
            playerImageURL
        }
    }`;

    export async function preload() {
        return {
            cache: await client.query({ query: TWO_WAY_PLAYERS })
        };
    }
</script>

<script>
    import { restore, query } from 'svelte-apollo';

    export let cache;
    restore(client, TWO_WAY_PLAYERS, cache.data);

    let two_way_players = query(client, { query: TWO_WAY_PLAYERS });
</script>

<style>
    .player-card {
        width: 16em;
        height: 20em;
        border-style: dashed;
        padding: 2em;
        display: inline-block;
        text-align: center;
    }
    .player-headshot {
        width: 10em;
    }
</style>

<main>
    <div id='player-content'>
        {#await $two_way_players} 
            <p>Loading players...</p>
        {:then result}
            {#each result.data.two_way_headshots as player (player.playerId)}
                <div class="player-card">
                    <img class="player-headshot" src={player.playerImageURL} alt='Headshot of {player.player}'/>
                    <li>Full Name: {player.player}</li>
                    <li>Player ID: {player.playerId}</li>
                    <li> Total Days: {player.totalDays}</li>
                        <li>With NBA Days: {player.withNbaDays}</li>
                        <li>Active NBA Game Days: {player.activeForNbaGameDays}</li>
                        <li>NBA Travel Days: {player.travelWithNbaDays}</li>
                        <li>Non-NBA Days: {player.nonNbaDays}</li>
                        <li>Non-NBA G League Days: {player.nonNbaGlgDays}</li>
                </div>
            {:else}
                <li>No players found.</li>
            {/each}
        {:catch error}
            <li>There was an error loading the players.</li>
        {/await}
    </div>
</main>