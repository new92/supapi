import requests

from supapi.exceptions import *

try:
    requests.get('https://www.google.com', timeout=15)
except Exception:
    raise NetworkErrorException("[✕] No stable internet connection found.")

class Player:
    def __init__(self, tag: str, api: str):
        self.tag = tag
        if self.tag in ['', ' ']:
            raise InvalidTagException("the tag you entered is invalid.")
        self.tag = (self.tag[1:] if self.tag[0] == '#' else self.tag).upper().strip()
        self.api = api
        self.headers = {
            'Accept': 'application/json',
            'authorization': f'Bearer {self.api}'
        }
        self.name = ''
        self.exp = None
        self.trophies = None
        self.best_trophies = None
        self.wins = 0
        self.losses = 0
        self.battles = 0
        self.three_crown_wins = 0
        self.challenge_cards_won = 0
        self.challenge_max_wins = 0
        self.tournament_cards_won = 0
        self.tournament_battles = 0
        self.donations = 0
        self.donations_rcv = 0
        self.total_donations = 0
        self.war_day_wins = 0
        self.clan_cards_collected = 0
        self.arena = None
        self.current_trophies = 0
        self.previous_trophies = 0
        self.badges = []
        self.achievements = []
        self.cards = []
        self.chests_wins = []
        self.chests = []
        self.all = {}
        self.fetch()
        self.chest()
    
    def fetch(self):
        resp = requests.get(f'https://api.clashroyale.com/v1/players/%23{self.tag}', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.name = js['name']
            self.exp = js['expLevel']
            self.trophies = js['trophies']
            self.best_trophies = js['bestTrophies']
            self.wins = js['wins']
            self.losses = js['losses']
            self.battles = js['battleCount']
            self.three_crown_wins = js['threeCrownWins']
            self.challenge_cards_won = js['challengeCardsWon']
            self.challenge_max_wins = js['challengeMaxWins']
            self.tournament_cards_won = js['tournamentCardsWon']
            self.tournament_battles = js['tournamentBattleCount']
            self.donations = js['donations']
            self.donations_rcv = js['donationsReceived']
            self.total_donations = js['totalDonations']
            self.war_day_wins = js['warDayWins']
            self.clan_cards_collected = js['clanCardsCollected']
            self.arena = js['arena']['name']
            self.current_trophies = js['leagueStatistics']['currentSeason']['trophies']
            self.previous_trophies = js['leagueStatistics']['previousSeason']['trophies']
            self.badges = [js['badges'][i]['name'] + ' | ' + str(js['badges'][i]['level']) for i in range(len(js['badges']))]
            self.achievements = [js['achievements'][i]['name'] for i in range(len(js['achievements']))]
            self.cards = [js['cards'][i]['name'] + ' | ' + str(js['cards'][i]['level']) for i in range(len(js['cards']))]
            self.all = {
                'name': self.name,
                'exp': self.exp,
                'trophies': self.trophies,
                'best_trophies': self.best_trophies,
                'wins': self.wins,
                'losses': self.losses,
                'battles': self.battles,
                'three_crown_wins': self.three_crown_wins,
                'challenge_cards_won': self.challenge_cards_won,
                'challenge_max_wins': self.challenge_max_wins,
                'tournament_cards_won': self.tournament_cards_won,
                'tournament_battles': self.tournament_battles,
                'donations': self.donations,
                'donations_rcv': self.donations_rcv,
                'total_donations': self.total_donations,
                'war_day_wins': self.war_day_wins,
                'clan_cards_collected': self.clan_cards_collected,
                'arena': self.arena,
                'current_trophies': self.current_trophies,
                'previous_trophies': self.previous_trophies,
                'badges': self.badges,
                'achievements': self.achievements,
                'cards': self.cards
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error: {js["message"]}')  
    
    def chest(self):
        """
        Returns the upcoming chests of a player
        """
        resp = requests.get(f'https://api.clashroyale.com/v1/players/%23{self.tag}/upcomingchests', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.chests_wins = [js['items'][i]['index'] for i in range(len(js['items']))]
            self.chests = [js['items'][i]['name'] for i in range(len(js['items']))]

class Clan:
    def __init__(self, tag: str, api: str):
        self.tag = tag
        if self.tag in ['', ' ']:
            raise InvalidTagException("the tag you entered is invalid.")
        self.tag = (self.tag[1:] if self.tag[0] == '#' else self.tag).upper().strip()
        self.api = api
        self.headers = {
            'Accept': 'application/json',
            'authorization': f'Bearer {self.api}'
        }
        self.name = ''
        self.type = None
        self.description = ''
        self.location = ''
        self.members = 0
        self.clan_score = 0
        self.clan_war_trophies = 0
        self.required_trophies = 0
        self.donations_per_week = 0
        self.names = []
        self.roles = []
        self.exp_lvls = []
        self.trophies = []
        self.arenas = []
        self.ranks = []
        self.donations = []
        self.donations_rcv = []
        self.all = {}
        self.allMems = {}
        self.fetch()
        self.fetchMembers()
    
    def fetch(self):
        resp = requests.get(f'https://api.clashroyale.com/v1/clans/%23{self.tag}', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.name = js['name']
            self.type = js['type']
            self.description = js['description']
            self.location = js['location']['name']
            self.members = js['members']
            self.clan_score = js['clanScore']
            self.clan_war_trophies = js['clanWarTrophies']
            self.required_trophies = js['requiredTrophies']
            self.donations_per_week = js['donationsPerWeek']
            self.all = {
                'name': self.name,
                'type': self.type,
                'description': self.description,
                'location': self.location,
                'members': self.members,
                'clan_score': self.clan_score,
                'clan_war_trophies': self.clan_war_trophies,
                'required_trophies': self.required_trophies,
                'donations_per_week': self.donations_per_week
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error: {js["message"]}')
        
    def fetchMembers(self):
        resp = requests.get(f'https://api.clashroyale.com/v1/clans/%23{self.tag}/members', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.names = [js['items'][i]['name'] for i in range(len(js['items']))]
            self.roles = [js['items'][i]['role'] for i in range(len(js['items']))]
            self.exp_lvls = [js['items'][i]['expLevel'] for i in range(len(js['items']))]
            self.trophies = [js['items'][i]['trophies'] for i in range(len(js['items']))]
            self.arenas = [js['items'][i]['arena']['name'] for i in range(len(js['items']))]
            self.ranks = [js['items'][i]['clanRank'] for i in range(len(js['items']))]
            self.donations = [js['items'][i]['donations'] for i in range(len(js['items']))]
            self.donations_rcv = [js['items'][i]['donationsReceived'] for i in range(len(js['items']))]
            self.allMems = {
                'names': self.names,
                'roles': self.roles,
                'exp_lvls': self.exp_lvls,
                'trophies': self.trophies,
                'arenas': self.arenas,
                'ranks': self.ranks,
                'donations': self.donations,
                'donations_rcv': self.donations_rcv
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error: {js["message"]}')

class Cards:
    def __init__(self, api: str):
        self.api = api
        self.cards = []
        self.number_of_cards = 0
        self.all = {}
        self.headers = {
            'Accept': 'application/json',
            'authorization': f'Bearer {self.api}'
        }
        self.fetch()
    
    def fetch(self):
        resp = requests.get('https://api.clashroyale.com/v1/cards', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.cards = [js['items'][i]['name'] + ' | ' + str(js['items'][i]['maxLevel']) for i in range(len(js['items']))]
            self.number_of_cards = len(self.cards)
            self.all = {
                'number_of_cards': self.number_of_cards,
                'cards': self.cards
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error: {js["message"]}')

class Tournament:
    def __init__(self, tag: int, api: str):
        self.tag = tag
        if len(str(self.tag)) != 8:
            raise InvalidTagException("the tag you entered is invalid.")
        self.api = api
        self.headers = {
            'Accept': 'application/json',
            'authorization': f'Bearer {self.api}'
        }
        self.name = ''
        self.type = None
        self.description = ''
        self.status = None
        self.capacity = 0
        self.max_capacity = 0
        self.prep_time = 0
        self.duration = 0
        self.all = {}
        self.fetch()
    
    def fetch(self):
        def convert(x: int, y: int) -> int:
            if x == 1: 
                return y // 60
            else: 
                return y // 24
        resp = requests.get(f'https://api.clashroyale.com/v1/tournaments/%23{self.tag}', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.name = js['name']
            self.type = js['type']
            self.description = js['description']
            self.status = js['status']
            self.capacity = js['capacity']
            self.max_capacity = js['maxCapacity']
            self.prep_time = convert(1,convert(1,js['preparationDuration'])) + ' hours'
            self.duration = convert(2,convert(1,convert(1,js['duration']))) + ' days'
            self.all = {
                'name': self.name,
                'type': self.type,
                'description': self.description,
                'status': self.status,
                'capacity': self.capacity,
                'max_capacity': self.max_capacity,
                'prep_time': self.prep_time,
                'duration': self.duration
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error: {js["message"]}')