import json

#Function to load data from JSON file
def load_data(filename="data/fitness_data.json"):
    try:
        with open(filename, 'r') as f:
             data = json.load(f)

             health_metrics = data.get("health_metrics", {
                "weight": 0.0,
                "body_fat": 0.0,
                "calories_intake": 0
             })


             return data["workouts"], health_metrics, data["goals"]

        except FileNotFoundError:
            #If the file doesn't excist, return empty defaults
            return [], {"weight": 0.0, "body_fat":0.0, "calories_intake":0}, []

    # Function to save data to JSON file
    def save_data(workouts, health_metrics, goals, filename="data/fitness_data.json"):
        data = {
            "workouts": [workout.__dict__ for workout in workouts],
            "health_metrics": health_metrics
            "goals": goals
        }

        with open(filename, 'w') as f:
            json.dump(data, f)