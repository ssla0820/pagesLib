class basePage():
    def __init__(self, name):
        self.name = name
    def data(self):
        print(f'calling basePage.data() from {self.name}')
    def new(self):
        print(f'add new command in basePage.new() from {self.name}')
