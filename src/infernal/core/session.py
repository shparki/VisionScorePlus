from . import contants as const
from .infernal_error  import RequestError, RateError
from .utils import default_dict

import requests
from requests.auth import AuthBase

import datetime
import os
import csv
import json

import pandas as pd



class RiotAuth(AuthBase):

	def __init__(self, api_key):
		self.api_key = api_key

	def __call__(self, r):
		r.headers['X-Riot_Token'] = self.api_key
		return r



class Session(object):

	def __init__(self, api_key, endpoint, name=None):
		self.api_key = api_key
		self.auth = RiotAuth(self.api_key)
		self.endpoint = 'na-old'
		if endpoint in const.ENDPOINTS.keys():
			self.endpoint = endpoint

		self.uid = datetime.datetime.today().strftime('%y%m%d_%H%M%S')
		self.name = name
		if self.name is None:
			self.name = self.uid

		cwd = str(os.getcwd())
		self.encl_dirpath = '{}/sessions'.format(cwd)
		if not os.path.exists(self.encl_dirpath):
			os.mkdir(self.encl_dirpath)

		self.parent_dirpath = '{}/{}'.format(self.encl_dirpath, self.name)
		if not os.path.exists(self.parent_dirpath):
			os.mkdir(self.parent_dirpath)

		self.data_dirpath = '{}/data'.format(self.parent_dirpath, self.name)
		if not os.path.exists(self.data_dirpath):
			os.mkdir(self.data_dirpath)

		self.logs_dirpath = '{}/logs'.format(self.parent_dirpath, self.name)
		if not os.path.exists(self.logs_dirpath):
			os.mkdir(self.logs_dirpath)

	def __str__(self):
		return 'session: {} | uid: {}'.format(self.name, self.uid)

	def request(self, url, url_paraps, params={}):
		args = {
			'endpoint': 		const.ENDPOINTS[self.endpoint],
			'url':				url
		}
		req_url = const.URLS_BASE['base'].format_map(
			default_dict(**args))
		req_url = req_url.format_map(
			default_dict(**url_params))
		req = requests.get(
			url = req_url,
			params = params,
			auth = self.auth
		)
		if str(req.status_code) in const.RESPONSE_CODES.keys():
			raise RequestError(str(req.status_code))

		return req.json()









