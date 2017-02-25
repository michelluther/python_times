#!/usr/bin/env python3.4

from config import AppConfiguration
from persistence import persistence

from projects.project import Project

from ui.appWindow import AppWindow

projects = []

configuration = AppConfiguration()
print(configuration._storageFolder)

appWindow = AppWindow(configuration);


# projects.append(Project(123, 'marjory'))
# projects.append(Project(456, 'hagebau'))

# for project in projects:
# 	project.addPosition(123, 'Projektleiter')

# persistence.saveProjects(projects)

