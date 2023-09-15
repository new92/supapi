from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='supapi',
    version='0.0.1',
    license='MIT',
    description='The supapi Python module is a versatile and powerful tool designed to simplify the process of retrieving comprehensive data about players, clans, cards, tournaments, clubs, and brawlers from three popular mobile games: Clash of Clans (CoC), Clash Royale, and Brawl Stars. This module is your all-in-one solution for accessing and analyzing game-related information, making it an invaluable resource for developers, gamers, and data enthusiasts alike.',
    long_description=long_description,
    author='new92',
    author_email='new92github@gmail.com',
    maintainer='new92',
    maintainer_email='new92github@gmail.com',
    url='https://www.github.com/new92/supapi',
    packages=find_packages(),
    install_requires=[
        'requests'
    ]
)