
import random



class Exercise:
    exercises = {}
    def __init__(self, exercise: str, type, level: float):
        self.exercise = exercise
        self.level = level
        self.type = type
        if self.level not in Exercise.exercises:
            Exercise.exercises[self.level] = [self]
        else:
            Exercise.exercises[self.level].append(self)
        
   
    def __repr__(self) -> str:
        return str(self.__dict__)

beginner_lift = Exercise("lift 5", "strength", 1)
beginner_run = Exercise("run 5", "speed", 1)
intermediate_lift = Exercise("lift 10", "strength", 3.5)
intermediate_run = Exercise("run 10", "speed", 3.8)
advanced_lift = Exercise("lift 15", "strength", 7.3)
advanced_run = Exercise("run 15", "speed", 9)




class Workout:
    available_exercises = Exercise.exercises
    def __init__(self, goal, type):
        self.goal = goal
        self.type = type
    def sort_bytype(self, available_exercises = available_exercises):
        for exercise in available_exercises:
            if self.type in available_exercises.level:
                pass

    def create_workout(self, available_exercises = available_exercises):
        
        chosen_exercices = []
        while self.goal >= sorted(available_exercises)[0]:

            level = random.choice(list(available_exercises.keys()))

            if level > self.goal:
                continue
    
            chosen_exercices.append(random.choice(available_exercises[level]).exercise)
    
            self.goal -= level
        print("workout:", chosen_exercices)

my_goal = int(input("what level workout would you like"))

my_workout = Workout(my_goal, "speed")
my_workout.create_workout()

