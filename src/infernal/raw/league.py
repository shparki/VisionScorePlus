from ..core import Session, RequestError, const
import traceback

import json
import pandas as pd

class League(object):

	version = const.VERSIONS['league']

	@classmethod
	def get_challenger_league(cls, session, queue, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_LEAGUE['challenger league'],
				url_params = {
					'version':			cls.version,
					'queue':			queue
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
			record_path=['entries'],
			meta=['leagueId', 'tier']
		)
		return req_table

	@classmethod
	def get_master_league(cls, session, queue, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_LEAGUE['master league'],
				url_params = {
					'version':			cls.version,
					'queue':			queue
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
			record_path=['entries'],
			meta=['leagueId', 'tier']
		)
		return req_table

	@classmethod
	def get_grandmaster_league(cls, session, queue, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_LEAGUE['grandmaster league'],
				url_params = {
					'version':			cls.version,
					'queue':			queue
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
			record_path=['entries'],
			meta=['leagueId', 'tier']
		)
		return req_table

	@classmethod
	def get_league(cls, session, league_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_LEAGUE['league'],
				url_params = {
					'version':			cls.version,
					'league_id':		league_id
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
			record_path=['entries'],
			meta=['leagueId', 'tier']
		)
		return req_table

	@classmethod
	def get_league_positions(cls, session, summoner_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_LEAGUE['league positions'],
				url_params = {
					'version':			cls.version,
					'summoner_id':		summoner_id
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
			data=r#,
			# record_path=['entries'],
			# meta=['leagueId', 'tier']
		)
		return req_table

