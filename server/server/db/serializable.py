
class Serializable:

	__serialized_fields__ = None

	def serialize(self) -> dict:
		return {
			key: self.__dict__[key]
			for key in self.__class__.__serialized_fields__
		}
