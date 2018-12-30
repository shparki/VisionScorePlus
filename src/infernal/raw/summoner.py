from ..core import Session, RequestError, const
import traceback

import json
import pandas as pd

class Summoner(object):
	version = const.VERSIONS['summoner']


	@classmethod
	def get_summoner_by_account_id(cls, session, account_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_SUMMONER['summoner by account id'],
				url_params = {
					'version':			cls.version,
					'account_id':		account_id
				},
				params = params
			)
		except RequestError as req_err:
			print(req_err)
			traceback.print_exc()
		except Exception as e:
			print(e)
			traceback.print_exc()

		req_table = pd.io.json.json_normalize(r)
		return req_table


	@classmethod
	def get_summoner_by_name(cls, session, summoner_name, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_SUMMONER['summoner by name'],
				url_params = {
					'version':			cls.version,
					'summoner_name':	summoner_name
				},
				params = params

			)
		except RequestError as req_err:
			print(req_err)
			traceback.print_exc()
		except Exception as e:
			print(e)
			traceback.print_exc()

		req_table = pd.io.json.json_normalize(r)
		return req_table


	@classmethod
	def get_summoner_by_puuid(cls, session, puuid, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_SUMMONER['summoner by puuid'],
				url_params = {
					'version':			cls.version,
					'puuid':			puuid
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
	def get_summoner_by_summoner_id(cls, session, summoner_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_SUMMONER['summoner by summoner id'],
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