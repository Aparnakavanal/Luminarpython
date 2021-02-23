class pycharm:
    def create_file(self):
        print("pycharm create file")
    def execute_program(self):
        print("pycharm execute program")


class vscode:
    def create_file(self):
        print("vscode create file")

    def execute_program(self):
        print("vscode execute program")

class Programmer:
    def coding(self,ide):
        ide.create_file()
        ide.execute_program()

cd=vscode()
p=Programmer()
p.coding(cd)

