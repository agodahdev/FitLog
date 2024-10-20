#Goal manager class to manage fitness goal and generate progress reports
class GoalManager:
    def__init__(self):
        self.goal = []


    def set_goal(self, goal_type, target_value):
        #create a new fitness goal and add it to the list
        goal = {"goal_type": goal_type, "target_value": target_value, "progress": 0.0}
        self.goals.append(goal)


    
    def generate_report(self, workouts, health_metrics):
        #Generates a report on the user's progress toward fitness goals
        for goal in self.goals:
            print(f"Goal: {goal['goal_type']}, Target: {goal['target_value']}")
            print(f"Current Weight: {health_metrics.data['weight']} kg")
            #Basic progress calculation
            print(f"Progress: {goal['progress']}%")
            print("Workouts contributing to progress:")
            for workout in workouts:
                print(f" - {workout}")