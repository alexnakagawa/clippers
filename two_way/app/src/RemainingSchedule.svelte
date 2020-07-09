<script context="module">
    // import Handsontable from "handsontable";
    import gql from 'graphql-tag';
    import { client } from './apollo';
    import { NBA_TEAMS } from './queries';

    export async function preload() {
        return {
            cache: await client.query({ query: NBA_TEAMS })
        };
    }
</script>

<script>
    import { restore, query } from 'svelte-apollo';
    import SchedulePlayers from './SchedulePlayers.svelte'

    export let cache;
    restore(client, NBA_TEAMS, cache.data);

    let selected;
    let nbaTeams = query(client, { query: NBA_TEAMS });

</script>

<form on:submit>
	<select bind:value={selected} >
		{#await $nbaTeams}
            <!-- promise is pending -->
        {:then result}
            <!-- promise was fulfilled -->
            {#each result.data.team as team (team.teamId)}
                <option value={team}>
                    {team.teamName}
                </option>
		    {/each}
        {:catch error}
            <!-- promise was rejected -->
            Error: {error}
        {/await}
	</select>
</form>

{#if selected}
    <!-- content here -->
    <div id="players-by-team">
        <SchedulePlayers teamId={selected.teamId}/>
    </div>
{:else}
    <!-- else content here -->
    No team selected. Please select a team.
{/if}
<!-- <p>selected team {selected ? selected.teamName : '[waiting...]'}</p> -->