#health metrics class to track weight, body fat, and daily calories intake
class HealthMetrics:
    def__init__(self):
    self.data = {
        #Default weight
        "weight": 0.0,
        #Default body fat percentage
        "body_fat": 0.0,
        #Default daily calories intake
        "calories_intake": 0,
    }

    def update_metrics(self, weight, body_fat, calories_intake):
        # Updates metrics with new values provided by the user
        self.data["weight"] = weights
        self.data["body_fat"] = body_fat
        self.data["calories_intake"] = calories_intake

    def__str__(self):
        return f"weight: {self.data['weight']} kg, Body Fat: {self.data['body_fat']}%, Calories Intake: {self.data['calories_intake']} kcal"