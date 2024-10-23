# Goal manager class to manage fitness goal and generate progress reports
class GoalManager:
    def __init__(self):
        # List to store fitness goals
        self.goals = []

    def set_goal(self, goal_type, target_value, initial_weight):
        # Set a goal with goal type, target value, and starting weight
        goal = {
            "goal_type": goal_type,
            "target_value": target_value,
            "initial_weight": initial_weight,  # Starting weight for progress tracking
            "progress": 0.0  # Start progress at 0%
        }
        # Add the goal to the list
        self.goals.append(goal)

    def generate_report(self, workouts, health_metrics):
        # Loop through all goals
        for goal in self.goals:
           print(f"Goal: {goal['goal_type']}, Target: {goal['target_value']}")

        # Check if the goal is 'Lose weight'
        if goal['goal_type'] == "lose weight":
            # Access health metrics as object attributes
            current_weight = health_metrics.weight  # Accessing current weight
            target_weight = goal['target_value']  # Target weight for the goal
            initial_weight = goal['initial_weight']  # Initial weight when goal was set

            # Calculate progress based on weight loss, ensure progress doesn't exceed 100%
            if current_weight > target_weight:
                progress = ((initial_weight - current_weight) / (initial_weight - target_weight)) * 100
                progress = min(progress, 100)  # Cap progress at 100%
                goal['progress'] = progress
                print(f"Current Weight: {current_weight} kg")
                print(f"Progress: {goal['progress']}%")
            else:
                print(f"Goal achieved! Current weight: {current_weight} kg")

        # List workouts contributing to progress
        print("Workouts contributing to progress:")
        for workout in workouts:
            print(f"  - {workout}")