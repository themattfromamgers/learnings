class public:
    def __init__(self):
        print("Public Giriş")

class student(public):
    def __init__(self):
        public.__init__(self)
        print("Student Yaratıldı.")

class teacher(public):
    def __init__(self):
        public.__init__(self)
        print("Teacher Yaratıldı")

x = student()



