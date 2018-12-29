from ..core import Session, RequestError, const
import traceback

class Summoner(object):
	version = const.VERSIONS['summoner']
	print('Version: ', version)

	@classmethod
	def get_summoner_by_account_id(cls, session, account_id, params={}):
		pass

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

		return r


	@classmethod
	def get_summoner_by_PUUID(cls, session, PUUID, params={}):
		pass

	@classmethod
	def get_summoner_by_summoner_id(cls, session, summoner_id, params={}):
		pass