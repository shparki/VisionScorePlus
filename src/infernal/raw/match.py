from ..core import Session, RequestError, const
import traceback

import json
import pandas as pd


class Match(object):

	version = const.VERSIONS['match']

	# @classmethod
	# def get_matches_by_tournament(cls, session, tournament_code, params={}):
	# 	pass

	@classmethod
	def get_match(cls, session, match_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_MATCH['match'],
				url_params = {
					'version':			cls.version,
					'match_id':			match_id
				},
				params = params

			)
		except RequestError as req_err:
			print(req_err)
			# traceback.print_exc()
		except Exception as e:
			print(e)
			# traceback.print_exc()

		req_table = pd.io.json.json_normalize(r)
		return req_table

	# @classmethod
	# def get_match_by_tournament(cls, session, tournament_code, match_id, params={}):
	# 	pass

	@classmethod
	def get_matchlist(cls, session, account_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_MATCH['matchlist'],
				url_params = {
					'version':			cls.version,
					'account_id':		account_id
				},
				params = params

			)
		except RequestError as req_err:
			print(req_err)
			# traceback.print_exc()
		except Exception as e:
			print(e)
			# traceback.print_exc()

		req_table = pd.io.json.json_normalize(
			data=r,
			record_path=['matches'],
			meta=['startIndex', 'endIndex', 'totalGames']
		)
		return req_table

	@classmethod
	def get_timeline(cls, session, match_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_MATCH['timeline'],
				url_params = {
					'version':			cls.version,
					'match_id':			match_id
				},
				params = params

			)
		except RequestError as req_err:
			print(req_err)
			# traceback.print_exc()
		except Exception as e:
			print(e)
			# traceback.print_exc()

		req_table = pd.io.json.json_normalize(
			data=r
		)

		return req_table