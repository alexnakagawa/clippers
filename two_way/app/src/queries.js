import gql from 'graphql-tag';

/* Players and Contracts*/
const TWO_WAY_PLAYERS = gql `{
        two_way_headshots(order_by: {withNbaDays: desc}) {
            playerId
            player
            totalDays
            withNbaDays
            activeForNbaGameDays  
            playerImageURL
        }
    }`;


const TWO_WAY_CONTRACT = gql `
    query TwoWayContractQuery($playerId: bigint) {
        two_way_contract_card( where: { playerId: { _eq: $playerId } }) {
            contractId
            playerId
            player
            signingDate
            contractTeamId
            signingTeamId
            nbaEarnedSalary
            nbaSalaryDays
            nbaServiceLimit
            glgEarnedSalary
            glgSalaryDays
            unreportedDays
            teamNameShort
            teamLogoURL
        }
}`


const PLAYERS_BY_TEAM = gql `
    query PlayersByTeamQuery($teamId: bigint) {
        two_way_contract_card(where: {
            teamId: {
                _eq: $teamId
            }
        }) {
            playerId
            player
            playerImageURL
            teamNameShort
            nbaEarnedSalary
            nbaSalaryDays
            glgEarnedSalary
            glgSalaryDays
        }
    }
`

/* Teams */
const TEAMS = gql `{
        team(order_by: {teamId: asc}) {
            teamId
            teamName
            teamNameShort
            teamLogoURL
        }
}`


const NBA_TEAMS = gql `{
        team(order_by: {
                teamId: asc
            }, where: {
                leagueLk: {
                    _eq: "NBA"
                }
            }) {
            teamId
            teamName
            teamNameShort
            teamLogoURL
        }
}`

export { TWO_WAY_PLAYERS, TWO_WAY_CONTRACT, TEAMS, NBA_TEAMS, PLAYERS_BY_TEAM };