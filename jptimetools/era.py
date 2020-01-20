"""
Information relating to Japanese eras.
"""
from dataclasses import dataclass
from datetime import date

CURRENT_YEAR = str(date.today().year)

@dataclass
class Era:
    '''
    This class contains information about Japanese eras
    '''
    startyear: str
    endyear: str
    kanji: str
    romaji: str


@dataclass
class Reiwa(Era):
    startyear: str = '2019'
    endyear: str = CURRENT_YEAR
    kanji: str = '令和'
    romaji: str = 'reiwa'


@dataclass
class Heisei(Era):
    startyear: str = '1989'
    endyear: str = '2019'
    kanji: str = '平成'
    romaji: str = 'heisei'


@dataclass
class Showa(Era):
    startyear: str = '1926'
    endyear: str = '1989'
    kanji: str = '昭和'
    romaji: str = 'shouwa'


@dataclass
class Taisho(Era):
    startyear: str = '1912'
    endyear: str = '1926'
    kanji: str = '大正'
    romaji: str = 'taishou'


@dataclass
class Meiji(Era):
    startyear: str = '1868'
    endyear: str = '1912'
    kanji: str = '明治'
    romaji: str = 'meiji'


@dataclass
class Keiou(Era):
    startyear: str = '1865'
    endyear: str = '1868'
    kanji: str = '慶応'
    romaji: str = 'keiou'


@dataclass
class Genji(Era):
    startyear: str = '1864'
    endyear: str = '1865'
    kanji: str = '元治'
    romaji: str = 'genji'


@dataclass
class Bunkyuu(Era):
    startyear: str = '1861'
    endyear: str = '1864'
    kanji: str = '文久'
    romaji: str = 'bunkyuu'


@dataclass
class Mannen(Era):
    startyear: str = '1860'
    endyear: str = '1861'
    kanji: str = '万延'
    romaji: str = 'manen'


@dataclass
class Taisho(Era):
    startyear: str = '1912'
    endyear: str = '1926'
    kanji: str = '大正'
    romaji: str = 'taishou'