<script context="module">
    // import Handsontable from "handsontable";
    import gql from 'graphql-tag';
    import { client } from './apollo';
    import { PLAYERS_BY_TEAM } from './queries';

    export async function preload() {
        return {
            cache: await client.query({ query: PLAYERS_BY_TEAM })
        };
    }
</script>

<script>
    import { restore, query } from 'svelte-apollo';
    export let teamId;

    let playersByTeam = query(client, { query: PLAYERS_BY_TEAM,
                                        variables: {teamId} });
    
    $: playersByTeam.refetch({ teamId });

    function numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
</script>

<style>
    mark {
        background-color: rgba(255, 127, 80);
    }
    .player-card {
        box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.5);
        border-radius: 4px;
        box-sizing: border-box;
        cursor: pointer;
        width: 20em;
        height: 24em;
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
</style>

{#await $playersByTeam}
    <!-- promise is pending -->
{:then result}
    {#each result.data.two_way_contract_card as player (player.playerId)}
        <div class="player-card">
            <div class="player-headshot">
                <img src={player.playerImageURL} alt='Headshot of {player.player}' style="width:11em"/>
            </div>
            <div class="player-info">
                <div class="player-name">
                    <strong>{player.player}</strong>
                </div>
                <ul>
                    <li>Player ID: {player.playerId}</li>
                    <li>NBA Salary: <mark>${numberWithCommas(player.nbaEarnedSalary)}</mark></li>
                    <li>NBA Salary Days: {player.nbaSalaryDays}</li>
                    <li>G-League Salary: <mark>${numberWithCommas(player.glgEarnedSalary)}</mark></li>
                    <li>G-League Salary Days: {player.glgSalaryDays}</li>
                </ul>
            </div>
        </div>
    {/each}
    <!-- promise was fulfilled -->
{:catch error}
    <!-- promise was rejected -->
    Error: {error}
{/await}