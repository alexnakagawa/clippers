<svelte:head>
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/handsontable/dist/handsontable.full.min.css"> -->
</svelte:head>

<script>
    import { restore, query } from 'svelte-apollo';
    import gql from 'graphql-tag';
    import { TWO_WAY_CONTRACT } from './queries';
    import { client } from './apollo';

    export let playerId;
    // let playerIdComparison = { "_eq": Number(playerId) };
    const two_way_contract = query(client, { query: TWO_WAY_CONTRACT,
                                             variables: { playerId }
    });
    $: two_way_contract.refetch({ playerId });
</script>

<style>
    /* your styles go here */
    img {
        height: 3em;
    }
</style>

<h4>Contracts</h4>
{#await $two_way_contract}
    <p>Loading contract(s)...</p>
{:then result}
    {#each result.data.two_way_contract_card as contract (contract.contractId)}
        <img src={contract.teamLogoURL} alt={contract.teamNameShort}/>
    {:else}
        <li>No contracts found</li>
    {/each}
{:catch error}
    <p>There was an error loading the contract.</p>
{/await}
