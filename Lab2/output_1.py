class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

class Scores:
    def __init__(self, scores):
        self.scores = scores

    def total(self):
        return sum(self.scores)

def calculate_score(person, scores):
    total_score = scores.total()
    is_adult = person.age >= 18
    
    print("Name:", person.name)
    print("Age:", person.age)
    print("Gender:", person.gender)
    print("Height:", person.height)
    print("Weight:", person.weight)
    print("Total Score:", total_score)
    print("Adult:", is_adult)

# Приклад виклику функції
person = Person("John", 25, "Male", 175, 70)
scores = Scores([85, 90, 75, 88, 92])
calculate_score(person, scores)
