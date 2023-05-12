class public:
    def __init__(self, score):
        self.score = score
class score_add(public):
    def __init__(self, score):
        public.__init__(self, score)
        self.score = score
        print("Bir Skor eklendi.")
        score += +1
        print(f'Güncel Skorunuz: {score}')
        

class score_delete(public):
    def __init__(self, score):
        public.__init__(self, score)
        self.score = score
        score -= -1
        print("Bir Skor Silindi")
        print(f'Skor: {score}')

class score_status(public):
    def __init__(self, score):
        public.__init__(self, score)
        self.score = score
        print(f'Mevcut Skorunuz: {score}')


