from . import constants as constants


class default_dict(dict):
	def __missing__(self, key):
		return '{' + key + '}'