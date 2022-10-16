class Worker:
    def __init__(self, name, project, status):
        self.name = name
        self.project = project
        self.status = status
        print("-- Developper létrehozva --")

    def getName(self):
        return self.name
    def getProject(self):
        return self.project
    def getStatus(self):
        return self.status

workers = []

for i in range(4):
    name = input("Enter worker name: ")
    project = input("Enter project name: ")
    status = input("Enter status: ")
    workers.append(Worker(name, project, status))

seen = []
for i in workers:
    for j in workers:
        if i.getProject() == j.getProject() and i.getName() != j.getName() and str(i.getName() + ":" + j.getName()) not in seen:
            print(i.getName() + " és " + j.getName() + " együtt dolgoznak")
            seen.append(i.getName() + ":" + j.getName())
            seen.append(j.getName() + ":" + i.getName())
