from ..core import Session, RequestError, const
import traceback

import json
import pandas as pd

class ThirdPartyCode(object):

	version = const.VERSIONS['third_party_code']

	@classmethod
	def get_third_party_code(cls, session, summoner_id, params={}):
		r = None

		try:
			r = session.request(
				url = const.URLS_THIRD_PARTY_CODE['third party code'],
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

		return r