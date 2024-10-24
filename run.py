# Import necessary libraries and modules
from datetime import datetime
from workout import Workout
from health_metrics import HealthMetrics
from goal_manager import GoalManager
from db_manager import load_data, save_data


# Main Fitness Tracker application class
class FitnessTracker:
    def __init__(self):
        # Initialize the application with empty or loaded data
        self.workouts = []
        self.health_metrics = HealthMetrics()  # Health metrics class instance
        self.goal_manager = GoalManager()      # Goal manager class instance
        self.load_data()

    def load_data(self):
        # Load saved data from the JSON file or initialize with default values
        self.workouts, self.health_metrics.data, self.goal_manager.goals = \
            load_data()

    def save_data(self):
        # Save current data (workouts, health metrics, and goals)
        # to the JSON file
        save_data(
            self.workouts, self.health_metrics.data, self.goal_manager.goals
        )

    def log_workout(self):
        try:
            # Get user input for workout details and log it
            exercise = input("Enter exercise type: ")
            duration = int(input("Enter duration (in minutes): "))
            if duration <= 0 or duration > 1440:
                raise ValueError(
                    "Duration must be between 1 and 1440 minutes."
                )
            intensity = input("Enter intensity (low/medium/high): ").lower()
            if intensity not in ['low', 'medium', 'high']:
                raise ValueError(
                    "Invalid intensity. Please choose 'low', 'medium', "
                    "or 'high'."
                )
            calories_burned = int(input("Enter calories burned: "))
            if calories_burned <= 0 or calories_burned >= 10000:
                raise ValueError(
                    "Calories burned must be a positive number"
                     " and less than 10,000."
                )
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            workout = Workout(
                exercise, duration, intensity, calories_burned, date
            )
            self.workouts.append(workout)
            print("Workout logged successfully!")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    def track_health_metrics(self):
        # User inputs for health metrics and update the health_metrics
        try:
            weight = float(input("Enter current weight (kg): "))
            if weight <= 0 or weight > 500:
                raise ValueError("Weight must be between 1 and 500 kg.")
            body_fat = float(input("Enter body fat percentage: "))
            if body_fat < 0 or body_fat > 100:
                raise ValueError(
                    "Body fat percentage must be between 0 and 100."
                )
            calories_intake = int(input("Enter daily calories intake: "))
            if calories_intake <= 0 or calories_intake > 10000:
                raise ValueError("Calories intake must be a positive number and less" 
                                 " than 10,000.")
            self.health_metrics.update_metrics(
                weight, body_fat, calories_intake
            )
            print("Health metrics updated successfully!")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    def set_fitness_goals(self):
        # Get goal type and target weight from user
        goal_type = input("Enter goal type (e.g., 'Lose weight'): ").lower()
        if goal_type not in ['lose weight', 'build muscle']:
            print(
                "Invalid goal type. Please choose 'Lose weight' "
                "or 'Build muscle'."
            )
            return
        try:
            target_value = float(
                input("Enter target value (e.g., target weight): ")
            )
            if target_value <= 0 or target_value > 500:
                raise ValueError(
                    "Target value must be between 1 and 500 kg."
                )

            # Use current weight as the starting point for progress tracking
            initial_weight = self.health_metrics.data['weight']

            # Set the goal with the current weight as the starting point
            self.goal_manager.set_goal(goal_type, target_value, initial_weight)
            print("Goal set successfully!")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    def view_summary(self):
        # Displays a summary of workouts, health metrics, and fitness goals
        print("\n--- Workouts ---")
        for workout in self.workouts:
            print(workout)

        print("\n--- Health Metrics ---")
        print(self.health_metrics)

        print("\n--- Fitness Goals ---")
        for goal in self.goal_manager.goals:
            print(goal)

    def generate_progress_report(self):
        # Generate a fitness progress report based on goals and health metrics
        print("\n--- Progress Report ---")
        self.goal_manager.generate_report(self.workouts, self.health_metrics)

    def menu(self):
        # Main Menu loop for the application
        while True:
            print("\nFitness Tracker Menu:")
            print("1. Log Workout")
            print("2. Track Health Metrics")
            print("3. Set Fitness Goals")
            print("4. View Summary")
            print("5. Generate Progress Report")
            print("6. Save and Exit")

            choice = input("Choose an option (1-6): ")

            if choice == '1':
                self.log_workout()
            elif choice == '2':
                self.track_health_metrics()
            elif choice == '3':
                self.set_fitness_goals()
            elif choice == '4':
                self.view_summary()
            elif choice == '5':
                self.generate_progress_report()
            elif choice == '6':
                self.save_data()
                print("Data saved. Exiting the application.")
                break
            else:
                print("Invalid option, please try again.")


# Entry point of the application
if __name__ == "__main__":
    tracker = FitnessTracker()  # Create an instance of the application
    tracker.menu()  # Start the menu loop
