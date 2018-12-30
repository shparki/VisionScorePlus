from ..core import Session, RequestError, const
import traceback

import json
import pandas as pd

class Spectator(object):

	version = const.VERSIONS['spectator']

	@classmethod
	def get_active_match(cls, session, summoner_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_SPECTATOR['active match'],
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
	def get_featured_games(cls, session, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_SPECTATOR['featured games'],
				url_params = {
					'version':			cls.version
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
			record_path=['gameList'],
			meta=['clientRefreshInterval']
		)
		return req_table