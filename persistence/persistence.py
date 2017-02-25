from persistence.serializable import ProjectSerializable 
import sys
import json


f = open("projects.json", "w")

def createPersistenceFile():
	pass

def findPersistenceFile():
	pass

def saveProjects(projects):
	serializedProjects = []

	for project in projects:
		serializedProjects.append(ProjectSerializable(project).serialize())

	json.dump(serializedProjects, f)
	# print(jsonString)

