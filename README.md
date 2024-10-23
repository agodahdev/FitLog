 # Fitlog

## About the app:
The fitness tracker app helps user monitor their workouts, track their health metrics (like weight, body fat percentage, and calories intake)m
and set fitness goals. It allowes users to log their workouts, update health information, and see their progress towards a goal like lose weight
or building muscle. The app is designed to give users an easy way to keep track of their fitness journey, view summeries, and generate progress reports. 

## Features:
1.**Log Workouts**: Record the type excercise, duration, intensity and calories burned.

2.**Track Health Metrics**: Update weight, body fat percentage, and daily calorie intake.

3.**Set Fitness Goals**: Set Goals like losing weight or building muscle and track your progress.

4.**View Summary**: See your logged workouts, health metrics, fitness goals in one place.

5.**Generate Progress Report**: Get a detailed report showing how much progress you've toward your goal.

6.**Save and Exit**: The app saves your data so that when you restart it, all your previous information will still be there.

## Instructions on How to use it:

1.**Menu Options**: When you start the app, you'll see that the main menu with the following options:
   1. Log Workout
   2. Track Health Metrics
   3. Set Fitness Goals
   4. View Summary
   5. Generate Progress Report
   6. Save and Exit.

### How to log Workouts:
- Choose option 1 to log workout.
- Enter the excercise type (e.g. running)
- Enter the duration (in minutes).
- Enter the intensity (low, medium, or high).
- Enter the number of calories burned.
- The workout will be logged, and you will see a success message.

### How to Track Health Metrics:
- Choose option 2 to track your health metrics.
- Enter your current weight (in kg).
- Enter your body fat percentage.
- Enter your daily calorie intake.
- The health metrics will be updated, and you will see a success message.

### How to Set Fitness Goals:
- Choose option 3 to set a fitness goal.
- Enter the goal type (e.g., Lose weight or Build muscle).
- Enter your target value (e.g., target weight).
- The app will set the goal, and you will see a success message.

### How to View Summary:
- Choose option 4 to view a summary.
- You’ll see a list of your logged workouts, current health metrics, and fitness goals.

### How to Generate Progress Report:
- Choose option 5 to generate a progress report.
- You’ll see your goal, the progress you’ve made, and the workouts contributing to your progress.

### How to Save and Exit:
- Choose option 6 to save your data and exit the app. When you restart the app, all your previous information will still be there.

## Testing
Here’s a list of errors I encountered and resolved during the development of the app:

1. **Indentation Errors**: Fixed incorrect indentation in several parts of the code, especially in try-except blocks.

2. **AttributeError ('dict' object has no attribute 'dict')**: Fixed by handling how Workout objects were converted for JSON saving.

3. **KeyError ('weight')**: Fixed by ensuring proper initialization of health metrics and using `.get()` methods for safe access.

4. **ValueError for Invalid Input in Log Workout**: Added input validation for negative durations, unrealistic calorie values, and invalid intensity levels.

5. **ValueError for Invalid Input in Track Health Metrics**: Added checks to ensure weight, body fat, and calories are within realistic ranges.

6. **ValueError for Invalid Input in Set Fitness Goals**: Added input validation for goal types and target values to ensure valid inputs.

7. **Progress Calculation Issue**: Fixed progress calculation to accurately reflect percentage toward the fitness goal.

8. **JSON File Not Found Error**: Handled missing `fitness_data.json` by initializing default values when the file isn’t present.

### App Testing
1. **Menu**:
   - When you start the app for the first time and there is no previous data, it will say: `File 'data/fitness_data.json' not found. Initializing with default values.`
   - If you enter a number outside the valid range (greater than 6 or less than 1) or letters, the app will return: `Invalid option, please try again.`

2. **Workout Logging**:
   - Test with negative or unrealistic numbers for all inputs (duration, intensity, calories burned). The app will return error messages like:
     - `Duration must be a positive number.`
     - `Calories burned must be a positive number and less than 10,000.`
   - With valid inputs, the workout is logged successfully.

3. **Tracking Health Metrics**:
   - Test with unrealistic values like 100000 kg for weight, 7000000% for body fat, or 1000000 for calories intake.
   - The app will return error messages like:
     - `Weight must be between 1 and 500 kg.`
     - `Body fat percentage must be between 0 and 100.`
   - With valid inputs, health metrics are updated successfully.

4. **Setting Fitness Goals**:
   - Test with invalid goal types (e.g., entering 100000) or unrealistic target weights (e.g., 100000 kg).
   - The app will return error messages like:
     - `Invalid goal type. Please choose 'Lose weight' or 'Build muscle'.`
     - `Target value must be between 1 and 500 kg.`
   - With valid inputs, the goal is set successfully.

5. **Viewing Summary**:
   - Test the summary after logging workouts, updating health metrics, and setting goals.
   - The app will display the workouts, updated health metrics, and fitness goals correctly.
   - Tested and works fine.

6. **Generating Progress Reports**:
   - Test the progress report after setting a goal and updating your weight.
   - The app will show accurate progress toward the goal (e.g., 60% progress if you reduce weight from 90 kg to 75 kg).
   - Tested and works fine.

7. **Save and Exit**:
   - After logging data, choose "Save and Exit" from the menu. The data is saved successfully, and when the app is restarted, all previous information is still there.
   - Tested and works fine.

### Validator Testing

  - **PEP8**: 
    -  No errors were returned from https://pep8ci.herokuapp.com/#

## Deployment:
 - **This project was deployed using github and Heroku**:

 - Fork or clone this repo
 - Create a new Heroku app
 - Set buildingblacks to Python and NodeJS 
 - Link the Heroku app to Github, searching repo
 - Deploy Branch

 - **Github deployment**:

  - Go to the Settings tab in your GitHub repo.
  - In the Source drop-down menu, select the main branch.
  - Save the changes under Branch settings.
  - Return to the Code tab, and under Deployments on the right, you will see the live page.

## Credits:

- Code institute Python Essentials Template

- Code institure deployment terminal

