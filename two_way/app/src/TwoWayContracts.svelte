<script context='module'>
    import gql from 'graphql-tag';
    import { client } from './apollo';

    const TWO_WAY_CONTRACTS = gql`{}` // TODO 
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

    const two_way_contracts = query(client, { query: TWO_WAY_CONTRACTS });

    var table = document.getElementById('example')
    new Handsontable(table, {
        data: two_way_contract.result.data, // TODO: this may be incorrect
        colHeaders: ['contractId', 'contractTeamId', 'nbaDaysRemaining',
                     'glgEarnedSalary', 'glgSalaryDays', 'nbaEarnedSalary',
                     'nbaSalaryDays', 'nbaServiceDays', 'unreportedDays',
                     'signingDate', 'signingTeamId', 'nbaServiceLimit'],
        columnSorting: true
    })
</script>

{#await $two_way_contracts}
<p>Loading contracts...</p>
{:then result}
<div id='example'></div>
{:catch error}
<p>There was an error loading the contracts.</p>
{/await}