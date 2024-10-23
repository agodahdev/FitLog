# Health metrics class to track weight, body fat, and daily calories intake
class HealthMetrics:
    def __init__(self, weight=0.0, body_fat=0.0, calories_intake=0):
        # Health metrics attributes
        self.weight = weight  # User's current weight
        self.body_fat = body_fat  # Body fat percentage
        self.calories_intake = calories_intake  # Daily calorie intake

    def update_metrics(self, weight, body_fat, calories_intake):
        # Update health metrics
        self.weight = weight
        self.body_fat = body_fat
        self.calories_intake = calories_intake

    def __str__(self):
        # String representation for displaying metrics
        return (
            f"Weight: {self.weight} kg, Body Fat: {self.body_fat}%, "
            f"Calories Intake: {self.calories_intake} kcal"
        )
