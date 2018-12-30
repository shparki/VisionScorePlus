class Constants(object):

    VERSIONS = {
        'champion_mastery':         'v4',
        'league':                   'v4',
        'match':                    'v4',
        'spectator':                'v4',
        'summoner':                 'v4',
        'third_party_code':         'v4'
    }

    RESPONSE_CODES = {
        '400':                      'Bad request',
        '401':                      'Unauthorized',
        '403':                      'Forbidden',
        '404':                      'Not found',
        '405':                      'Method not allowed',
        '415':                      'Unsupported media type',
        '422':                      'Player exists, but hasn\'t played since match history collection began',
        '429':                      'Rate limit exceeded',
        '500':                      'Internal server error',
        '502':                      'Bad gateway',
        '503':                      'Service unavailable',
        '504':                      'Gateway timeout'
    }

    SEASONS = [
        'Preseason 3',
        'Season 3',
        'Preseason 2014',
        'Season 2014',
        'Preseason 2015',
        'Season 2015',
        'Preseason 2016',
        'Season 2016',
        'Preseason 2017',
        'Season 2017',
        'Preseason 2018',
        'Season 2018'
    ]

    # Populate the queue, queueId, and gameQueueConfigId fields; not including deprecated queues
    MATCHMAKING_QUEUES = {
        '0': {
            'Map':                  'Custom Games',
            'Description':          None,
        },
        '72': {
            'Map':                  'Howling Abyss',
            'Description':          '1v1 Snowdown Showdown games',
        },
        '73': {
            'Map':                  'Howling Abyss',
            'Description':          '2v2 Snowdown Showdown games',
        },
        '75': {
            'Map':                  'Summoner\'s Rift',
            'Description':          '6v6 Hexakill games',
        },
        '76': {
            'Map':                  'Summoner\'s Rift',
            'Description':          'Ultra Rapid Fire games',
        },
        '78': {
            'Map':                  'Howling Abyss',
            'Description':          'One For All: Mirror Mode games',
        },
        '83': {
            'Map':                  'Summoner\'s Rift',
            'Description':          'Co-op vs AI Ultra Rapid Fire games',
        },
        '98': {
            'Map':                  'Twisted Treeline',
            'Description':          '6v6 Hexakill games',
        },
        '100': {
            'Map':                  'Butcher\'s Bridge',
            'Description':          '5v5 ARAM games',
        },
        '310': {
            'Map':                  'Summoner\'s Rift',
            'Description':          'Nemesis games',
        },
        '313': {
            'Map':                  'Summoner\'s Rift',
            'Description':          'Black Market Brawlers games',
        },
    }

    # DEPRECATED_QUEUES = {

    # }

    ENDPOINTS = {
        # Regional Endpoints
        'br':                       'br1.api.riotgames.com',
        'eune':                     'eun1.api.riotgames.com',
        'euw':                      'euw1.api.riotgames.com',
        'jp':                       'jp1.api.riotgames.com',
        'kr':                       'kr.api.riotgames.com',
        'lan':                      'la1.api.riotgames.com',
        'las':                      'la2.api.riotgames.com',
        'na':                       'na.api.riotgames.com',
        'na-old':                   'na1.api.riotgames.com',
        'oce':                      'oc1.api.riotgames.com',
        'tr':                       'tr1.api.riotgames.com',
        'ru':                       'ru.api.riotgames.com',
        'pbe':                      'pbe1.api.riotgames.com',

        # Regional Proxies
        'americas':                 'americas.api.riotgames.com',
        'europe':                   'europe.api.riotgames.com',
        'asia':                     'asia.api.riotgames.com'
    }

    # URLS; Convention: all urls start in '/' but do not end in one
    URLS_BASE = {
        # Main base for all URLs
        'base':                     'https://{endpoint}{url}',

        # Primary midpoints for all sub-apis
        'champion_mastery':         '/lol/champion-mastery/{version}',
        'league':                   '/lol/league/{version}',
        'match':                    '/lol/match/{version}',
        'spectator':                '/lol/spectator/{version}',
        'summoner':                 '/lol/summoner/{version}',
        'third_party_code':         '/lol/platform/{version}'
    }

    URLS_CHAMPION_MASTERY = {
        # Get all champion mastery entities sorted by number of champion points descending.
        'all masteries':            URLS_BASE['champion_mastery'] + \
                                    '/champion-masteries/by-summoner/{summoner_id}',

        # Get a champion mastery by player ID and champion ID.
        'champion mastery':         URLS_BASE['champion_mastery'] + \
                                    '/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}',

        # Get a player's total champion mastery score, which is the sum of individual champion mastery levels.
        'total mastery':            URLS_BASE['champion_mastery'] + \
                                    '/scores/by-summoner/{summoner_id}'
    }

    URLS_LEAGUE = {
        # Get the challenger league for given queue.
        'challenger league':        URLS_BASE['league'] + \
                                    '/challengerleagues/by-queue/{queue}',

        #Get the master league for given queue.
        'master league':            URLS_BASE['league'] + \
                                    '/masterleagues/by-queue/{queue}',

        #Get the grandmaster league for a given queue
        'grandmaster league':       URLS_BASE['league'] + \
                                    '/grandmasterleagues/by-queue/{queue}',

        # Get league with given ID, including inactive entries.
        'league':                   URLS_BASE['league'] +  \
                                    '/leagues/{league_id}',

        # Get league positions in all queues for a given summoner ID.
        'league positions':         URLS_BASE['league'] + \
                                    '/positions/by-summoner/{summoner_id}'
    }

    URLS_MATCH = {
        # Get match IDs by tournament code.
        'matches by tournmanet':    URLS_BASE['match'] +\
                                    '/matches/by-tournament-code/{tournament_code}/ids',

        #Get match by match ID.
        'match':                    URLS_BASE['match'] + \
                                    '/matches/{match_id}',

        #Get match by match ID and tournament code.
        'match by tournament':      URLS_BASE['match'] + \
                                    '/matches/{match_id}/by-tournament-code/{tournament_code}',

        # Get matchlist for games played on given account ID and platform ID and filtered using given filter parameters, if any.
        'matchlist':                URLS_BASE['match'] + \
                                    '/matchlists/by-account/{account_id}',

        # Get match timeline by match ID.
        'timeline':                 URLS_BASE['match'] + \
                                    '/timelines/by-match/{match_id}'
    }

    URLS_SPECTATOR = {
        # Get current game information for the given summoner ID.
        'active match':             URLS_BASE['spectator'] + \
                                    '/active-games/by-summoner/{summoner_id}',

        # Get list of featured games.
        'featured games':           URLS_BASE['spectator'] + \
                                    '/featured-games'
    }

    URLS_SUMMONER = {
        # Get a summoner by account ID.
        'summoner by account id':   URLS_BASE['summoner'] + \
                                    '/summoners/by-account/{account_id}',

        # Get a summoner by summoner name.
        'summoner by name':         URLS_BASE['summoner'] + \
                                    '/summoners/by-name/{summoner_name}',

        # Get a summoner by summoner ID.
        'summoner by summoner id':  URLS_BASE['summoner'] + \
                                    '/summoners/{summoner_id}',

        # get a summoner  by PUUID.
        'summoner by puuid':        URLS_BASE['summoner'] + \
                                    '/summoners/by-puuid/{puuid}'
    }

    URLS_THIRD_PARTY_CODE = {
        # Get third party code for a given summoner ID. (?)
        'summoner id':              URLS_BASE['third_party_code'] + \
                                    '/third-party-code/by-summoner/{summoner_id}'
    }


























