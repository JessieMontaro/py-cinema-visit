class Customer:
    def __init__(self, name, food):
        self.food = food
        self.name = name

    def watch_movie(self, movie):
        print(f"{self.name} is watching \"{movie}\".")
