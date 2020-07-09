<svelte:head>
	<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</svelte:head>

<script context="module">
    // import Handsontable from "handsontable";
    import gql from 'graphql-tag';
    import { client } from './apollo';
    import { TWO_WAY_PLAYERS } from './queries';

    export async function preload() {
        return {
            cache: await client.query({ query: TWO_WAY_PLAYERS })
        };
    }
</script>

<script>
    import { restore, query } from 'svelte-apollo';
    import TwoWayContract from './TwoWayContract.svelte';

    export let cache;
    restore(client, TWO_WAY_PLAYERS, cache.data);

    let two_way_players = query(client, { query: TWO_WAY_PLAYERS });
</script>

<style>
    .player-card {
        box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.5);
        border-radius: 4px;
        box-sizing: border-box;
        cursor: pointer;
        width: 16em;
        height: 20em;
        padding: 2em;
        margin: 1em;
        display: inline-block;
    }
    .player-card:hover {
        background-color: bisque;
    }
    .player-headshot {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .player-name {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 1em;
    }
    #player-contract {
        position: relative;
        bottom: 0;
    }
</style>

<main>
    <div id='player-content'>
        {#await $two_way_players} 
            <p>Loading players...</p>
        {:then result}
            {#each result.data.two_way_headshots as player (player.playerId)}
                <div class="player-card">
                    <div class="player-headshot">
                        <img src={player.playerImageURL} alt='Headshot of {player.player}' style="width:9em"/>
                    </div>
                    <div class="player-info">
                        <div class="player-name">
                            <strong>{player.player}</strong>
                        </div>
                        <li>Player ID: {player.playerId}</li>
                    </div>
                    <div id="player-contract">
                        <TwoWayContract playerId="{player.playerId}"/>
                    </div>
                </div>
            {:else}
                <li>No players found.</li>
            {/each}
        {:catch error}
            <li>There was an error loading the players.</li>
        {/await}
    </div>
</main>