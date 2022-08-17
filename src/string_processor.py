class StringProcessor:
    def __init__(self, string) -> None:
        self.string = string

    def append(self, string):
        self.string += string

    def remove(self, substring):
        self.string = self.string.replace(substring, '')

    def mirror(self):
        self.string = self.string[::-1]

    def save(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.string)

    def load(self, file_path):
        with open(file_path, 'r') as file:
            self.string = file.read()






