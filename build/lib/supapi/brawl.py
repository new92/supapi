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
        self.trophies = 0
        self.exp = None
        self.highest_trophies = 0
        self.solo_wins = 0
        self.duo_wins = 0
        self.three_wins = 0
        self.club_name = ''
        self.club_tag = ''
        self.all = {}
        self.fetch()
        
    def fetch(self):
        resp = requests.get(f'https://api.brawlstars.com/v1/players/%23{self.tag}', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.name = js['name']
            self.trophies = js['trophies']
            self.exp = js['expLevel']
            self.highest_trophies = js['highestTrophies']
            self.solo_wins = js['soloVictories']
            self.duo_wins = js['duoVictories']
            self.three_wins = js['3vs3Victories']
            self.club_name = js['club']['name']
            self.club_tag = js['club']['tag']
            self.all = {
                'name': self.name,
                'trophies': self.trophies,
                'exp': self.exp,
                'highest_trophies': self.highest_trophies,
                'solo_wins': self.solo_wins,
                'duo_wins': self.duo_wins,
                'three_wins': self.three_wins,
                'club_name': self.club_name,
                'club_tag': self.club_tag
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error: {js["message"]}')
        
class Club:
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
        self.description = ''
        self.trophies = 0
        self.type = None
        self.required_trophies = 0
        self.number_of_mems = 0
        self.names = []
        self.tags = []
        self.roles = []
        self.ctrophies = []
        self.all = {}
        self.allMems = {}
        self.fetch()
        self.fetchMembers()
        
    def fetch(self):
        resp = requests.get(f'https://api.brawlstars.com/v1/clubs/%23{self.tag}', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.name = js['name']
            self.description = js['description']
            self.trophies = js['trophies']
            self.type = js['type']
            self.required_trophies = js['requiredTrophies']
            self.all = {
                'name': self.name,
                'description': self.description,
                'trophies': self.trophies,
                'type': self.type,
                'required_trophies': self.required_trophies
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error: {js["message"]}')
    
    def fetchMembers(self):
        resp = requests.get(f'https://api.brawlstars.com/v1/clubs/%23{self.tag}/members', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.names = [js['items'][i]['name'] for i in range(len(js['items']))]
            self.tags = [js['items'][i]['tag'] for i in range(len(js['items']))]
            self.roles = [js['items'][i]['role'] for i in range(len(js['items']))]
            self.ctrophies = [js['items'][i]['trophies'] for i in range(len(js['items']))]
            self.number_of_mems = len(js['items'])
            self.allMems = {
                'names': self.names,
                'tags': self.tags,
                'roles': self.roles,
                'ctrophies': self.ctrophies,
                'number_of_mems': self.number_of_mems
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error: {js["message"]}')

class Brawlers:
    def __init__(self, api: str):
        self.api = api
        self.brawlers = []
        self.number_of_brawlers = 0
        self.all = {}
        self.headers = {
            'Accept': 'application/json',
            'authorization': f'Bearer {self.api}'
        }
        self.fetch()

    def fetch(self):
        resp = requests.get('https://api.brawlstars.com/v1/brawlers', allow_redirects=False, headers=self.headers)
        js = resp.json()
        if resp.status_code == 200:
            self.brawlers = [js['items'][i]['name'] for i in range(len(js['items']))]
            self.number_of_brawlers = len(self.brawlers)
            self.all = {
                'number_of_brawlers': self.number_of_brawlers,
                'brawlers': self.brawlers
            }
        else:
            raise NoDataFetchedException(f'unable to fetch data. Error: {js["message"]}')