
import json

# Function to load data from JSON file


def load_data(filename="data/fitness_data.json"):
    try:
        # Try opening the file for reading
        with open(filename, 'r') as f:
            data = json.load(f)  # Load the JSON data
            # set default health metrics if not in file
            health_metrics = data.get("health_metrics", {
                "weight": 0.0,       # Default weight
                "body_fat": 0.0,     # Default body fat percentage
                "calories_intake": 0  # Default daily calorie intake
            })
            # Use .get() for workouts and goals to avoid KeyError
            workouts = data.get("workouts", [])
            goals = data.get("goals", [])

            # Return the loaded data with safe fallback values
            return workouts, health_metrics, goals
    except FileNotFoundError:
        # If the file is not found, initialize empty defaults
        print(
            f"File '{filename}' not found. Initializing with default values."
        )
        return [], {"weight": 0.0, "body_fat": 0.0, "calories_intake": 0}, []
    except json.JSONDecodeError:
        # Handle the case where the JSON file is corrupted or malformed
        print(f"Error reading '{filename}'. Initializing with default values.")
        return [], {"weight": 0.0, "body_fat": 0.0, "calories_intake": 0}, []


# Function to save data to JSON file
def save_data(
    workouts, health_metrics, goals, filename="data/fitness_data.json"
      ):
    # Prepare the data dictionary for saving
    data = {
        # Convert Workout objects to dict if they have a __dict__ attribute
        "workouts": [
            workout.__dict__ if hasattr(workout, '__dict__') else workout
            for workout in workouts
            ],
        "health_metrics": health_metrics,  # Save updated health metrics
        "goals": goals
    }

    # Try writing the data to the JSON file
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)  # Use indent for better readability
    except IOError as e:
        # Handle file write errors (e.g., permission issues, disk space)
        print(f"Error saving data to {filename}: {e}")
