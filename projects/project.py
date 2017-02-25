from projects.position import Position 

class Project:
	"""docstring for Project"""
	def __init__(self, id, name):
		self._name = name
		self._id = id
		self._positions = []

	def getName(self):
		return self._name

	def getId(self):
		return self._id

	def addPosition(self, id, name):
		self._positions.append(Position(id, name, 100))
		print('position added')

	def getPositions(self):
		return self._positions

