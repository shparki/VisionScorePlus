from ..core import Session, RequestError, const
import traceback

import json
import pandas as pd

class ChampionMastery(object):

	version = const.VERSIONS['champion_mastery']

	@classmethod
	def get_all_masteries(cls, session, summoner_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_CHAMPION_MASTERY['all masteries'],
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

		req_table = pd.io.json.json_normalize(r)
		return req_table

	@classmethod
	def get_champion_mastery(cls, session, summoner_id, champion_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_CHAMPION_MASTERY['champion mastery'],
				url_params = {
					'version':			cls.version,
					'summoner_id':		summoner_id,
					'champion_id':		champion_id
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

	@classmethod
	def get_total_mastery(cls, session, summoner_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_CHAMPION_MASTERY['total mastery'],
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

		return pd.Series({'totalMastery': r})


