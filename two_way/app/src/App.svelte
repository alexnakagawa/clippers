<script>
	import ApolloClient from 'apollo-client';
	import { client } from './apollo';
	import { setClient } from 'svelte-apollo';
	import FileUpload from './FileUpload.svelte';
	import TwoWayPlayers from './TwoWayPlayers.svelte';
	import TwoWayContracts from './TwoWayContracts.svelte';
	// Approximate sapper preload
	// const articlePreloading = articlePreload();
	// const authorPreloading = authorPreload();
	setClient(client);
</script>

<h1>Two-Way Contracts</h1>
<h3>File Upload</h3> 
<FileUpload/>
<h3>Current Two-Way Players</h3>
<TwoWayPlayers/>
<h3>Two-Way Contracts by Date</h3>
<TwoWayContracts/>