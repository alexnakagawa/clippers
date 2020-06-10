import xml.etree.ElementTree as ET
import json

PARSER = ET.XMLParser(encoding='utf-8')
TREE = ET.parse('../two_way_data/two-way.xml', parser=PARSER)

ROOT = TREE.getroot()
PLAYERS_ELEM = ROOT.find('two-way-extract').find('two-way-seasons') \
                   .find('two-way-season').find('two-way-players')

def convert_player_xml_to_json(players_elem, json_name):
    json_data = []
    for player in PLAYERS_ELEM.findall('two-way-player'):
        p = {}
        p['playerId'] = int(player.find('playerId').text)
        p['rosterFirstName'] = player.find('rosterFirstName').text
        p['rosterLastName'] = player.find('rosterLastName').text
        p['activeForNbaGameDays'] = int(player.find('activeForNbaGameDays').text)
        p['nonNbaDays'] = int(player.find('nonNbaDays').text)
        p['nonNbaGlgDays'] = int(player.find('nonNbaGlgDays').text)
        p['totalDays'] = int(player.find('totalDays').text)
        p['travelWithNbaDays'] = int(player.find('travelWithNbaDays').text)
        p['withNbaDays'] = int(player.find('withNbaDays').text)
        json_data.append(p)
    with open('../two_way_data/{}'.format(json_name), 'w') as fp:
        json.dump(json_data, fp)
    print('Player JSON creation successful')


def convert_contract_xml_to_json(players_elem, json_name):
    json_data = []
    for player in PLAYERS_ELEM.findall('two-way-player'):
        p = {}
        p['playerId'] = int(player.find('playerId').text)
        contracts_elem = player.find('two-way-contracts')
        for contract in contracts_elem:
            p['contractId'] = int(contract.find('contractId').text)
            p['contractTeamId'] = int(contract.find('contractTeamId').text)
            p['nbaDaysRemaining'] = int(contract.find('nbaDaysRemaining').text)
            p['glgEarnedSalary'] = int(contract.find('glgEarnedSalary').text)
            p['glgSalaryDays'] = int(contract.find('glgSalaryDays').text)
            p['nbaEarnedSalary'] = int(contract.find('nbaEarnedSalary').text)
            p['nbaSalaryDays'] = int(contract.find('nbaSalaryDays').text)
            p['nbaServiceDays'] = int(contract.find('nbaServiceDays').text)
            p['unreportedDays'] = int(contract.find('unreportedDays').text)
            p['signingDate'] = contract.find('signingDate').text
            p['signingTeamId'] = int(contract.find('signingTeamId').text)
            p['nbaServiceLimit'] = int(contract.find('nbaServiceLimit').text)
            json_data.append(p)
    with open('../two_way_data/{}'.format(json_name), 'w') as fp:
        json.dump(json_data, fp)
    print('Contract JSON creation successful')


def convert_status_xml_to_json(players_elem, json_name):
    json_data = []
    for player in PLAYERS_ELEM.findall('two-way-player'):
        p = {}
        p['playerId'] = int(player.find('playerId').text)
        statuses_elem = player.find('two-way-statuses')
        for status in statuses_elem:
            p['date'] = status.find('date').text
            p['dayOfSeason'] = int(status.find('dayOfSeason').text)
            p['teamId'] = int(status.find('teamId').text)
            p['twoWayDailyStatus'] = status.find('twoWayDailyStatus').text
            p['twoWayDailyStatusLk'] = status.find('twoWayDailyStatusLk').text
            json_data.append(p)
    with open('../two_way_data/{}'.format(json_name), 'w') as fp:
        json.dump(json_data, fp)
    print('Status JSON creation successful')

if __name__ == '__main__':
    print("Executing two-way.py")
    convert_player_xml_to_json(PLAYERS_ELEM, 'two-way-player.json')
    convert_contract_xml_to_json(PLAYERS_ELEM, 'two-way-contract.json')
    convert_status_xml_to_json(PLAYERS_ELEM, 'two-way-status.json')
