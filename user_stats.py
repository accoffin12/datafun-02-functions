"""

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import stat
import statistics


# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

#Calculate measures of central tendancy for Agility Scores
score_mode = statistics.mode(scores)
score_mean = statistics.mean(scores)
score_median = statistics.median(scores)
score_variance = statistics.pvariance(scores)
score_st_dev = statistics.pstdev(scores)

print(f"The mode of all the scores was, {score_mode}.")
print(f"The mean score for the test was, {score_mean}.")
print(f"The median score for the test was, {score_median}.")
print(f"The variance of the test secores was, {round(score_variance, 2)}.")
print(f"The standard deviation of the test scores was {round(score_st_dev, 2)}.")
print()

#Calculate the slope and intercept for regression line.
y_future = 13

slope, intercept = stat.linear_regression(x_times, y_temps)
print(f"The linear regression for the data has a slope of {round(slope,2)} and an intercept of {round(intercept, 2)}")

x_future = 13
y_future = slope * x_future + intercept
print(f"Based on the temperatures over the past 12 hours, the temp will be {round(y_future,0)} degrees in a few hours.")







    



