'''
Module Unit Tests
'''

import datetime
import fab

def test_module_name():
    '''
    Tests the name of the module.
    '''
    assert fab.__name__ == 'fab'

# ----- Example Cards -----

C1 = fab.Card(
    body         = '**Bravo Specialization** *(You may only have Crippling Crush in your deck if your hero is Bravo.)*\n\n**Crush** - If Crippling Crush deals 4 or more damage to a hero, they discard 2 random cards.',
    cost         = 7,
    defense      = 3,
    flavor_text  = None,
    full_name    = 'Crippling Crush (1)',
    grants       = [],
    health       = None,
    identifiers  = ['1HP050', 'WTR043'],
    image_urls   = ['https://storage.googleapis.com/fabmaster/media/images/1HP050.width-450.png', 'https://storage.googleapis.com/fabmaster/media/images/WTR_43.width-450.png', 'https://storage.googleapis.com/fabmaster/media/images/U-WTR43.width-450.png'],
    intelligence = None,
    keywords     = ['Bravo Specialization', 'Crush'],
    name         = 'Crippling Crush',
    pitch        = 1,
    power        = 11,
    rarities     = ['M', 'M'],
    sets         = ['1HP', 'WTR'],
    tags         = ['example-1'],
    type_text    = 'Guardian Action - Attack',
    types        = ['Guardian', 'Action', 'Attack']
)

C2 = fab.Card(
    body         = 'If the next card you defend with this turn is a card with **combo**, it gains +2{d}.',
    cost         = 0,
    defense      = 3,
    flavor_text  = 'Silver flashes under the pale moonlight, blades slicing through air as Ira twisted and turned, narrowly avoiding their ambush.',
    full_name    = 'Flic Flak (2)',
    grants       = [],
    health       = None,
    identifiers  = ['1HP114', 'WTR093'],
    image_urls   = ['https://storage.googleapis.com/fabmaster/media/images/1HP114.width-450.png', 'https://storage.googleapis.com/fabmaster/media/images/WTR_93.width-450.png', 'https://storage.googleapis.com/fabmaster/media/images/U-WTR93.width-450.png'],
    intelligence = None,
    keywords     = [],
    name         = 'Flic Flak',
    pitch        = 2,
    power        = None,
    rarities     = ['R', 'R'],
    sets         = ['1HP', 'WTR'],
    tags         = ['example-2'],
    type_text    = 'Ninja - Defense Reaction',
    types        = ['Ninja', 'Defense Reaction']
)

C3 = fab.Card(
    body         = '**Once per Turn Action** - Create a Soul Shackle token: Your next Runeblade or Shadow action this turn gains **go again. Go again** *(It\'s a Shadow Runeblade aura with "At the beginning of your action phase, banish the top card of your deck.")*',
    cost         = None,
    defense      = None,
    flavor_text  = None,
    full_name    = 'Chane',
    grants       = ['Go again'],
    health       = 20,
    identifiers  = ['HER037', 'CHN001', 'MON154'],
    image_urls   = ['https://storage.googleapis.com/fabmaster/media/images/HER037.width-450.png', 'https://storage.googleapis.com/fabmaster/media/images/CHN001.width-450.png', 'https://storage.googleapis.com/fabmaster/media/images/MON154.width-450.png', 'https://storage.googleapis.com/fabmaster/media/images/U-MON154.width-450.png'],
    intelligence = 4,
    keywords     = ['Go again'],
    name         = 'Chane',
    pitch        = None,
    power        = None,
    rarities     = ['P', 'R', 'T'],
    sets         = ['HER', 'CHN', 'MON'],
    tags         = ['example-3'],
    type_text    = 'Shadow Runeblade Hero - Young',
    types        = ['Shadow', 'Runeblade', 'Hero', 'Young']
)


# ----- Example Card Lists -----

CL1 = fab.CardList([C1, C2, C3])


# ----- Example Card Sets -----

CS1 = fab.CardSet(
    editions     = ['F', 'U'],
    identifier   = 'MON',
    name         = 'Monarch',
    release_date = datetime.date(2021, 5, 7)
)

CS2 = fab.CardSet(
    editions     = ['A', 'U'],
    identifier   = 'WTR',
    name         = 'Welcome to Rathe',
    release_date = datetime.date(2019, 10, 11)
)

CS3 = fab.CardSet(
    editions     = ['N'],
    identifier   = 'UPR',
    name         = 'Uprising',
    release_date = datetime.date(2022, 6, 24)
)


# ----- Example Card Set Collections -----

CSC1 = fab.CardSetCollection({'MON': CS1, 'WTR': CS2, 'UPR': CS3})


# ----- Example Decks -----

D1 = fab.Deck(
    cards = fab.CardList([C1, C2]),
    hero  = C3,
    name  = 'Test'
)
