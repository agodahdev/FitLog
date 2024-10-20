#Import necessary libraries and modules
from datetime import datetime
from workout import Workout
from health_metrics import HealthMetrics
from goal_manager import GoalManager
from db_manager import load_data, save_data

# Main Fitness Tracker application class
class FitnessTracker:
    def__init__(self):
    #Initialize the application with empty or loaded data
    self.workouts = []
    #Health metrics class
    self.health_metrics = HealthMetrics()
    #Goal manager class 
    self.goal_manager = GoalManager()
    self.load_data()

    def load_data(self):
        #Load saved data from the JSON file or initialize with default values
        self.workouts, self.health_metrics.data, self.goal_manager.goals = load_data()

    def save_data(self):
        #Save current data (workouts, health metrics, and goals) to the JSON file 
        save_data(self.workouts, self.health_metrics.data, self.goal_manager.goals)

    def log_workouts(self):
        #Gets user to input workout details and log it
        excercise = input("Enter exercise type:")
        duration = int(input("Enter duration (in minutes): "))
        intensity = input("Enter intensity (low/medium/high): ")
        calories_burned = int(input("Enter calories burned: ")) 
        date = datetime.now().strftime("%Y-%m-%d $H:%M:%S")

    # Create a new workout and add it to the list
    workout = Workout(excercise, duration, intensity, calories_burned, date)
    self.workouts.append(workout)
    print("Workout logged successfully!")