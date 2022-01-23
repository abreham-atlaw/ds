class DBUtils:

	@staticmethod
	def deserialize(response, object_class):
		if response is None:
			return None
		if type(response) == list:
			return [object_class(*value) for value in response]
		return object_class(*response)
