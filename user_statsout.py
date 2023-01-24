"""Alexandra Coffin
Data Fundementals
2023 January 23
Side note: issues updating conda to allow for use of stat.linear_regression, it should work still.
"""
PS C:\Users\Tower\Documents\Data Analytics Sp 2023\Repositories\Reference Repo Sp 2023\datafun-02-functions> & C:/Users/Tower/AppData/Local/Programs/Python/Python311/python.exe "c:/Users/Tower/Documents/Data 
Analytics Sp 2023/Repositories/Reference Repo Sp 2023/datafun-02-functions/user_stats.py"
The mode of all the scores was, 111.
The mean score for the test was, 99.12.
The median score for the test was, 102.5.
The variance of the test secores was, 175.67.

Traceback (most recent call last):
  File "c:\Users\Tower\Documents\Data Analytics Sp 2023\Repositories\Reference Repo Sp 2023\datafun-02-functions\user_stats.py", line 101, in <module>
    slope, intercept = stat.linear_regression(x_times, y_temps)
                       ^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'stat' has no attribute 'linear_regression'