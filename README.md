# supapi 🚀

The supapi Python module is a versatile and powerful tool designed to simplify the process of retrieving comprehensive data about players, clans, cards, tournaments, clubs, and brawlers from three popular mobile games: Clash of Clans (CoC), Clash Royale, and Brawl Stars. This module is your all-in-one solution for accessing and analyzing game-related information, making it an invaluable resource for developers, gamers, and data enthusiasts alike.

## Installation 📥

Install supapi using pip

```bash
pip install supapi
```

## Authors ✍️

- [@new92](https://www.github.com/new92)

## Contributing 🤝

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`. For more info please check the `CODE_OF_CONDUCT.md` file

## Feedback 💭

If you have any feedback, please reach out to us at <a href="mailto:new92github@gmail.com">this email address</a>.

**Feel free to contact us anytime ! You'll get a reply within a day. Please avoid using abusive or offensive language.
If you are reporting a bug or making a suggestion please make sure your report/suggestion is as much detailed as possible.**

## License 📜

[![License](https://img.shields.io/github/license/new92/netwix?style=for-the-badge)](https://github.com/new92/netwix/blob/main/LICENSE.md)

## <a href="https://github.com/new92/supapi/tree/main/examples">Examples 🚩</a>

## API keys 🔑

#### <a href="https://developer.clashofclans.com/#/login">CoC</a>

#### <a href="https://developer.clashroyale.com/#/login">Clash Royale</a>

#### <a href="https://developer.brawlstars.com/#/login">Brawl Stars</a>

## Documentation 📄

### Example CoC player info

```python
from supapi.src.clash import *

player = Player('89YCUV9GY', 'MY_API_KEY')
print(player.name) # Output: THE KILLER
```

### Example Clash Royale clan info

```python
from supapi.src.royale import Clan

clan = Clan('PJR0RL', 'MY_API_KEY')
print(clan.location) # Output: Andorra
```

### Example Clash Royale cards

```python
from supapi.src.royale import Cards

card = Cards('MY_API_KEY')
print(card.names) # Output: A list of names of all the cards in Clash Royale
```

### Example Brawl Stars player info

```python
from supapi.src.brawl import Player

player = Player('90P9CYCV8', 'MY_API_KEY')
print(player.solo_wins) # Output: 2846
```

### Example Brawl Stars club info

```python
from supapi.src.brawl import Club

club = Club('20C0RLVGC', 'MY_API_KEY')
print(club.all) # Output: A dictionary of data
```