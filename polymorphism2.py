class pycharm:
    def execute(self):
        print("pycharm")
        print("executing")

class Intellij:
    def execute(self):
        print("Intellij")
        print("executing")

class laptop:
    def code(self, ide):
        ide.execute()

l = laptop()
ide = pycharm()
l.code(ide)
