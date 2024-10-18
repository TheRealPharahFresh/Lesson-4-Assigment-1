# Task 1: Your Mood Tracker 
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week.
#  Use nested loops to implement this: 
# the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.

import random

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]
time_of_day = ["Morning", "Afternoon", "Evening"]

for day_index in range(7):
    day = weekdays[day_index]
    mood = random.choice(moods)
    for time_index in range(3):
        tod = time_of_day[time_index]
        print(f'On {day} {tod} you were {mood}')

