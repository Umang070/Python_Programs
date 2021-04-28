# -----ducktyping--------------
class Codeblock:
                def execute(self):
                    print("Running")
class Own:
                def execute(self):
                    print("Checking")
                    print("Running")
class Try:
                def display(self,ide):
                    ide.execute()
ide = Own()                        # ide = Codeblock()......not fixed we can change it....
t = Try()
t.display(ide)