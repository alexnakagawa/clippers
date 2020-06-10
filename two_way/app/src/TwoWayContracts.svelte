<svelte:head>
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/handsontable/dist/handsontable.full.min.css"> -->
</svelte:head>

<script>
    import { restore, query } from 'svelte-apollo';
    import gql from 'graphql-tag';
    // import Handsontable from "handsontable";
    import { client } from './apollo';

    // const TWO_WAY_CONTRACTS = gql`{}` // TODO
    // const two_way_contracts = query(client, { query: TWO_WAY_CONTRACTS });

    // var table = document.getElementById('example')
    // new Handsontable(table, {
    //     data: two_way_contract.result.data, // TODO: this may be incorrect
    //     colHeaders: ['contractId', 'contractTeamId', 'nbaDaysRemaining',
    //                  'glgEarnedSalary', 'glgSalaryDays', 'nbaEarnedSalary',
    //                  'nbaSalaryDays', 'nbaServiceDays', 'unreportedDays',
    //                  'signingDate', 'signingTeamId', 'nbaServiceLimit'],
    //     columnSorting: true
    // })
</script>

<!-- {#await $two_way_contracts}
<p>Loading contracts...</p>
{:then result}
<div id='example'></div>
{:catch error}
<p>There was an error loading the contracts.</p>
{/await} -->