import requests

from src.exceptions import *

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
        self.name = ''
        self.th = ''
        self.role = ''
        self.war_pref = ''
        self.trophies = None
        self.best_trophies = None
        self.war_stars = None
        self.attack_wins = None
        self.defense_wins = None
        self.builder_hall_lvl = None
        self.vs_trophies = None
        self.best_vs_trophies = None
        self.donations = None
        self.donations_rcv = None
        self.clan_tag = None
        self.clan_name = None
        self.clan_lvl = None
        self.clan_icon = None
        self.vs_battle_wins = None
        self.labels = []
        self.achievements = []
        self.troops = []
        self.heroes = []
        self.spells = []
        self.all = {}
        self.headers = {
            'Accept': 'application/json',
            'authorization': f'Bearer {self.api}'
        }
        self.fetch()
    
    def fetch(self):
        def complete(num: int) -> bool:
            return True if num == 3 else False
        resp = requests.get(f'https://api.clashofclans.com/v1/players/%23{self.tag}', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            if js['role'] == 'admin':
                self.role = 'Elder'
            elif js['role'] == 'coLeader':
                self.role = 'Co-Leader'
            else:
                self.role = 'Leader'
            self.name = js['name']
            self.th = js['townHallLevel']
            self.war_pref = js['warPreference']
            self.trophies = js['trophies']
            self.best_trophies = js['bestTrophies']
            self.war_stars = js['warStars']
            self.attack_wins = js['attackWins']
            self.defense_wins = js['defenseWins']
            self.builder_hall_lvl = js['builderHallLevel']
            self.vs_trophies = js['versusTrophies']
            self.best_vs_trophies = js['bestVersusTrophies']
            self.donations = js['donations']
            self.donations_rcv = js['donationsReceived']
            self.clan_tag = js['clan']['tag']
            self.clan_name = js['clan']['name']
            self.clan_lvl = js['clan']['clanLevel']
            self.clan_icon = js['clan']['badgeUrls']['medium']
            self.vs_battle_wins = js['versusBattleWins']
            self.labels = [js['labels'][i]['name'] for i in range(len(js['labels']))] if len(js['labels']) != 0 else []
            self.achievements = [js['achievements'][i]['name'] + ' | ' + str(complete(js['achievements'][i]['stars'])) for i in range(len(js['achievements']))]
            self.troops = [js['troops'][i]['name'] + ' | ' + str(js['troops'][i]['level']) for i in range(len(js['troops'])) if js['troops'][i]['village'] == 'home' and 'Spell' not in js['troops'][i]['name']]
            self.heroes = [js['heroes'][i]['name'] + ' | ' + str(js['heroes'][i]['level']) for i in range(len(js['heroes']))]
            self.spells = [js['spells'][i]['name'] + ' | ' + str(js['spells'][i]['level']) for i in range(len(js['spells']))]
            self.all = {
                'name': self.name,
                'th': self.th,
                'war_pref': self.war_pref,
                'trophies': self.trophies,
                'best_trophies': self.best_trophies,
                'war_stars': self.war_stars,
                'attack_wins': self.attack_wins,
                'defense_wins': self.defense_wins,
                'builder_hall_lvl': self.builder_hall_lvl,
                'vs_trophies': self.vs_trophies,
                'best_vs_trophies': self.best_vs_trophies,
                'donations': self.donations,
                'donations_rcv': self.donations_rcv,
                'clan_tag': self.clan_tag,
                'clan_name': self.clan_name,
                'clan_lvl': self.clan_lvl,
                'clan_icon': self.clan_icon,
                'vs_battle_wins': self.vs_battle_wins,
                'labels': self.labels,
                'achievements': self.achievements,
                'troops': self.troops,
                'heroes': self.heroes,
                'spells': self.spells
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error {js["message"]}')

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
        self.description = None
        self.lvl = None
        self.icon = None
        self.fam = None
        self.members = None
        self.required_trophies = None
        self.required_th_lvl = None
        self.required_vs_trophies = None
        self.points = None
        self.war_frequency = None
        self.war_win_streak = None
        self.war_wins = None
        self.war_ties = None
        self.war_losses = None
        self.is_war_log_public = None
        self.war_league = None
        self.capital_league = None
        self.capital_hall = None
        self.labels = None
        self.districts = None
        self.all = {}
        self.fetch()

    def fetch(self):
        resp = requests.get(f'https://api.clashofclans.com/v1/clans/%23{self.tag}', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.name = js['name']
            self.type = js['type']
            self.description = js['description']
            self.lvl = js['clanLevel']
            self.icon = js['badgeUrls']['medium']
            self.fam = js['isFamilyFriendly']
            self.members = js['members']
            self.required_trophies = js['requiredTrophies']
            self.required_th_lvl = js['requiredTownhallLevel']
            self.required_vs_trophies = js['requiredVersusTrophies']
            self.points = js['clanPoints']
            self.war_frequency = js['warFrequency']
            self.war_win_streak = js['warWinStreak']
            self.war_wins = js['warWins']
            self.war_ties = js['warTies']
            self.war_losses = js['warLosses']
            self.is_war_log_public = js['isWarLogPublic']
            self.war_league = js['warLeague']['name']
            self.capital_league = js['capitalLeague']['name']
            if js['clanCapital'] != {}:
                self.capital_hall = js['clanCapital']['capitalHallLevel']
                self.districts = [js['clanCapital']['districts'][i]['name'] + ' | ' + str(js['clanCapital']['districts'][i]['districtHallLevel']) for i in range(len(js['clanCapital']['districts']))]
            self.labels = [js['labels'][i]['name'] + ' | ' + js['labels'][i]['iconUrls']['medium'] for i in range(len(js['labels']))]
            self.all = {
                'name': self.name,
                'type': self.type,
                'description': self.description,
                'lvl': self.lvl,
                'icon': self.icon,
                'fam': self.fam,
                'members': self.members,
                'required_trophies': self.required_trophies,
                'required_th_lvl': self.required_th_lvl,
                'required_vs_trophies': self.required_vs_trophies,
                'points': self.points,
                'war_frequency': self.war_frequency,
                'war_win_streak': self.war_win_streak,
                'war_wins': self.war_wins,
                'war_ties': self.war_ties,
                'war_losses': self.war_losses,
                'is_war_log_public': self.is_war_log_public,
                'war_league': self.war_league,
                'capital_league': self.capital_league,
                'labels': self.labels,
                'capital_hall': self.capital_hall,
                'districts': self.districts
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error: {js["message"]}')

class League:
    def __init__(self, api: str):
        self.api = api
        self.headers = {
            'Accept': 'application/json',
            'authorization': f'Bearer {self.api}'
        }
        self.leagues = []
        self.fetch()
        self.clan_capital_leagues()
        self.war_leagues()

    def fetch(self):
        resp = requests.get('https://api.clashofclans.com/v1/leagues', allow_redirects=False, headers=self.headers)
        js = resp.json()
        self.leagues = [js['items'][i]['name'] + ' | ' + js['items'][i]['iconUrls']['small'] for i in range(len(js['items']))] if resp.status_code == 200 else []
    
    def clan_capital_leagues(self):
        resp = requests.get('https://api.clashofclans.com/v1/capitalleagues', allow_redirects=False, headers=self.headers)
        js = resp.json()
        self.leagues = [js['items'][i]['name'] for i in range(len(js['items']))] if resp.status_code == 200 else []
    
    def war_leagues(self):
        resp = requests.get('https://api.clashofclans.com/v1/warleagues', allow_redirects=False, headers=self.headers)
        js = resp.json()
        self.leagues = [js['items'][i]['name'] for i in range(len(js['items']))] if resp.status_code == 200 else []