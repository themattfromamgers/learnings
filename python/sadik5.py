class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

        print("oluşturuldu")

        
    def __str__(self):
     return f"{self.title}"

    def __len__(self):
     return self.duration

m = Movie('Star Wars', 'George', 'xd')

print(str(m))
