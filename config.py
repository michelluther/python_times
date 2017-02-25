import os
import json

# Read config from file
# 1. read default ...

print("trying to read a file")
f = open("conf.json", "r")
baseConfig = json.load(f)


class AppConfiguration:
	"""docstring for Config"""

	def __init__(self):
		self._appName = baseConfig["applicationName"]
		self._storageFolder = baseConfig["persistence"]["path"]

	def getAppName(self):
		return self._appName
		
		


