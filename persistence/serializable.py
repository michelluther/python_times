
class ProjectSerializable:
	"""docstring for ProjectJson"""
	def __init__(self, project):
		self.project = project

	def serialize(self):
		return {"id": self.project.getId(),
		"name": self.project.getName(),
		"positions": self._extractPositions()}	
		

	def _extractPositions(self):
		positions = []
		for position in self.project.getPositions():
			positions.append(self._extractPosition(position))
		return positions

	def _extractPosition(self, position):
		return {"id": position.getId(),
		"name": position.getName()
		}