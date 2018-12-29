class Match(object):

	@classmethod
	def get_matches_by_tournament(cls, session, tournament_code, params={}):
		pass

	@classmethod
	def get_match(cls, session, match_id, params={}):
		pass

	@classmethod
	def get_match_by_tournament(cls, session, tournament_code, match_id, params={}):
		pass

	@classmethod
	def get_matchlist(cls, session, account_id, params={}):
		pass

	@classmethod
	def get_timeline(cls, session, match_id, params={}):
		pass