class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name= str(name)
        self.age= int(age)
        self.tracks= str(tracks)
        self.score= float(score)

    def change_name(self, change_name):
        self.change_name = change_name
        print("Student's new name is", change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        print("Student's new age is", change_age)

    def add_track(self, add_track):
        self.add_track = add_track
        print("Student's new track is", add_track)

    def get_score(self, get_score):
        self.get_score = get_score
        print("Student's new score is", get_score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(20.9)
