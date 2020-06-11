<script>
	import ApolloClient from 'apollo-client';
	import { client } from './apollo';
	import { setClient } from 'svelte-apollo';
	import TwoWayPlayers, { preload as twoWayPlayerPreload } from './TwoWayPlayers.svelte';
	import TwoWayContracts from './TwoWayContracts.svelte';
	import RemainingSchedule from './RemainingSchedule.svelte'

	// Approximate sapper preload
	const twoWayPlayerPreloading = twoWayPlayerPreload();
	// const authorPreloading = authorPreload();

	setClient(client);
</script>

<h1>Two-Way Contracts</h1>

<h3>Current Two-Way Players</h3>
{#await twoWayPlayerPreloading}
	<p>Preloading players...</p>
{:then preloaded}
	<TwoWayPlayers {...preloaded}/>
{:catch error}
	<p>Error preloading players: {error}</p>
{/await}

<h3>Two-Way Contracts by Date</h3>
<TwoWayContracts/>

<h3>Remaining schedule for Two-Way Players given team</h3>
<RemainingSchedule/>
<!-- This is where the schedule will go -->