from . import constants as constants

class InfernalError(Exception):

	def __init__(self):
		pass

	def __str__(self):
		pass



class RequestError(InfernalError):

	def __init__(self, code):
		InfernalError.__init__(self)
		self.code = code
		self.message = const.REPSONSE_CODES[code]

	def __str__(self):
		return 'Request Error({}): {}'.format(self.code, self.message)



class RateError(InfernalError):

	def __init__(self):
		pass

	def __str__(self):
		pass