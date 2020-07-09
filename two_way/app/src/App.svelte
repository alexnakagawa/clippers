<script>
	import ApolloClient from 'apollo-client';
	import { client } from './apollo';
	import { setClient } from 'svelte-apollo';
	import TwoWayPlayers, { preload as twoWayPlayerPreload }  from './TwoWayPlayers.svelte';
	import RemainingSchedule, {preload as teamsPreload} from './RemainingSchedule.svelte';

	// Approximate sapper preload
	const twoWayPlayerPreloading = twoWayPlayerPreload();
	const teamsPreloading = teamsPreload();

	setClient(client);
</script>

<style>
	* {
      font-family: "Open Sans", sans-serif;
    }
	/* Add a black background color to the top navigation */
	.topnav {
	background-color: #333;
	overflow: hidden;
	}

	/* Style the links inside the navigation bar */
	.topnav a {
	float: left;
	color: #f2f2f2;
	text-align: center;
	padding: 14px 16px;
	text-decoration: none;
	font-size: 17px;
	}

	/* Change the color of links on hover */
	.topnav a:hover {
	background-color: #ddd;
	color: black;
	}
</style>

<div class="topnav">
  <a href="#players">Players</a>
  <a href="#schedule">Remaining Schedule</a>
</div>

<h1>Two-Way Knowledge Base</h1>

<!-- <h2>Teams!</h2>
{#await teamsPreloading}
    Loading teams...
{:then teamsPreloaded}
    <Teams {...teamsPreloaded}/>
{:catch error}
    Error loading teams.
{/await} -->

<h2><a id="player"></a><mark>Current Two-Way Players</mark></h2>
{#await twoWayPlayerPreloading}
	<p>Preloading players...</p>
{:then preloaded}
	<TwoWayPlayers {...preloaded}/>
{:catch error}
	<p>Error preloading players: {error}</p>
{/await}

<h2><a id="schedule"></a><mark>Remaining schedule for Two-Way Players given team</mark></h2>
{#await teamsPreloading}
	<p>Preloading teams...</p>
{:then preloaded}
	<RemainingSchedule {...preloaded}/>
{:catch error}
	<p>Error preloading teams: {error}</p>
{/await}
