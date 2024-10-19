class Workout:
    def__init__(self, exercise, duration, intensity, calories_burned, date):
    self.exercise = exercise
    self.duration = duration
    self.intensity = intensity
    self.calories_burned = calories_burned
    self.date = date

    # string for printing the workout 
    def__str__(self):
       return f"{self.date}: {self.excercise} for {self.duration} mins ({self.intensity} intensity) - {self.calories_burned} kcal"