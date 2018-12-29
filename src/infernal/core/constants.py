VERSIONS = {
    'champion_mastery':         'v4',
    'champion':                 'v3',
    'league':                   'v4',
    'lol_status':               'v3',
    'match':                    'v4',
    'spectator':                'v4',
    'summoner':                 'v4',
    'third_party_code':         'v4'#,
    # 'tournament_stub':          'v4',
    # 'tournament':               'v4'
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
    'champion':                 '/lol/platform/{version}',
    'league':                   '/lol/league/{version}',
    'lol_status':               '/lol/status/{version}',
    'match':                    '/lol/match/{version}',
    'spectator':                '/lol/spectator/{version}',
    'summoner':                 '/lol/summoner/{version}',
    'third_party_code':         '/lol/platform/{version}'#,
    # 'tournament_stub':          '/lol/tournament-stub/{version}',
    # 'tournament':               '/lol/tournament/{version}'
}

URLS_CMASTERY = {
    # Get all champion mastery entities sorted by number of champion points descending.
    'all':                      URLS_BASE['cmastery'] + '/champion-masteries/by-summoner/{summoner_id}',

    # Get a champion mastery by player ID and champion ID.
    'by champion':              URLS_BASE['cmastery'] + '/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}',

    # Get a player's total champion mastery score, which is the sum of individual champion mastery levels.
    'mastery':                  URLS_BASE['cmastery'] + '/scores/by-summoner/{summoner_id}'
}

URLS_CHAMPION = {
    # Retrieve all champions.
    'all':                      URLS_BASE['champion'] + '/champions',

    # Retrieve champion by ID.
    'by champion':              URLS_BASE['champion'] + '/champions/{champion_id}'
}

URLS_LEAGUE = {
    # Get the challenger league for given queue.
    'challenger':               URLS_BASE['league'] + '/challengerleagues/by-queue/{queue}',

    # Get league with given ID, including inactive entries.
    'by league':                URLS_BASE['league'] +  '/leagues/{league_id}',

    #Get the master league for given queue.
    'master':                   URLS_BASE['league'] + '/masterleagues/by-queue/{queue}',

    # Get league positions in all queues for a given summoner ID.
    'by summoner':              URLS_BASE['league'] + '/positions/by-summoner/{summoner_id}' 
}

URLS_LOL_STATUS = {
    # Get League of Legends status for the given shard.
    'status':                   URLS_BASE['status'] + '/shard-data'
}

URLS_MATCH = {
    # Get match IDs by tournament code.
    'matchID by tournament':    URLS_BASE['match'] + '/matches/by-tournament-code/{tournament_code}/ids',

    #Get match by match ID.
    'by match':                 URLS_BASE['match'] + '/matches/{match_id}',

    #Get match by match ID and tournament code.
    'by tournament':            URLS_BASE['match'] + '/matches/{match_id}/by-tournament-code/{tournament_code}',

    # Get matchlist for games played on given account ID and platform ID and filtered using given filter parameters, if any.
    'by account':               URLS_BASE['match'] + '/matchlists/by-account/{account_id}',

    # Get matchlist for last 20 matches played on given account ID and platform ID.
    'recent by account':        URLS_BASE['match'] + '/matchlists/by-account/{account_id}/recent',

    # Get match timeline by match ID.
    'timeline':                 URLS_BASE['match'] + '/timelines/by-match/{match_id}'
}

URLS_SPECTATOR = {
    # Get current game information for the given summoner ID.
    'active':                   URLS_BASE['spectator'] + '/active-games/by-summoner/{summoner_id}',

    # Get list of featured games.
    'featured':                 URLS_BASE['spectator'] + '/featured-games'
}

URLS_SUMMONER = {
    # Get a summoner by account ID.
    'by account':               URLS_BASE['summoner'] + '/summoners/by-account/{account_id}',

    # Get a summoner by summoner name.
    'by name':                  URLS_BASE['summoner'] + '/summoners/by-name/{summoner_name}',

    # Get a summoner by summoner ID.
    'by id':                    URLS_BASE['summoner'] + '/summoners/{summoner_id}'
}

URLS_THIRD_PARTY_CODE = {
    # Get third party code for a given summoner ID. (?)
    'by id':                    URLS_BASE['tpc'] + '/third-party-code/by-summoner/{summoner_id}'
}

# URLS_TOURNAMENT_STUB = {
#     # Create a mock tournament code for the give tournament.
#     'codes':                    URLS_BASE['tstub'] + '/codes',

#     # Gets a mock list of lobby events by tournament code.
#     'by tournament':            URLS_BASE['tstub'] + '/lobby-events/by-code/{tournament_code}',

#     # Creates a mock tournament provider and returns its ID.
#     'providers':                URLS_BASE['tstub'] + '/providers',

#     # Creates a mock tournament and returns its ID.
#     'tournaments':              URLS_BASE['tstub'] + '/tournaments'
# }

# URLS_TOURNAMENT = {
#     # Create tournament code for the given tournament.
#     'codes':                    URLS_BASE['tournament'] + '/codes',

#     # Update the pick type, map, spectator type, or allowed summoners for a code. / Returns the tournament code DTO associated with a tournament code string.
#     'by tournament':            URLS_BASE['tournament'] + '/codes/{tournament_code}',

#     # Gets a list of lobby events by tournament code.
#     'events by tournament':     URLS_BASE['tournament'] + '/lobby-events/by-code/{tournament_code}',

#     # Creates a tournament provider and returns its ID.
#     'providers':                URLS_BASE['tournament'] + '/providers',

#     # Creates a tournament and returns its ID.
#     'tournaments':              URLS_BASE['tournament'] + '/tournaments'
# }


























