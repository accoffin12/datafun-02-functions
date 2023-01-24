"""
Alexandra Coffin
Data Analytics Fundementals
January 23, 2023
Domain: Formula 1
Task: Build a PyBuddy to answer questions about domain selected. Use object orientation programming, custom classes and custom functions.

Build a PyBuddy to extend a welcome.
"""
from pybuddy_oop import PyBuddy
import datetime
import statistics as stats


from enum import Enum

class positions(Enum):
        manager = 1
        engineer = 2
        stratagist = 3
        Data_Analyst = 4  
class PyBuddy:
        def __init__(self, name, positions, founded, team_age, wins, team, available):
                self.name=name
                self.positions = positions
                self.founded = founded
                self.team_age = team_age
                self.wins = wins
                self.team = team
                self.available = available
        
    
        def __str__(self):
                """Built-in method"""
                s0 = f"I'm {self.name}.\n"
                s1 = f"I'm a {self.positions.name}.\n"
                s2 = f"We currently have {self.wins}\n"
                sm1 = f"We currently have {self.compare_wins()} wins than average!\n"
                s3 = f"I've been with the team {self.get_age_string()}.\n"
                sm2 = f"My team got a total annual bonus of ${self.annual_bonus():.2f}!\n"

                if self.available:
                        s3 = "There's no race today, I can help.\n"
                else:
                        s3 = "I'm at the track today, maybe tomorrow.\n"

                return s0 + s1 + s2 + sm1 + s3 + sm2
                
        def get_age_string(self):
                start= self.founded
                end = datetime.datetime.now()
                duration = end.year - start
                ageString = str(duration)
                return ageString

        #Created to compare wins to age, allowing for calculation of team bonus.
        # List created from user input, uses stats.mean.
        def compare_wins(self): 
                """Compare wins to calculate average."""
                win_avg = stats.mean(win_list) 

                if self.wins < win_avg:
                        return "lower"
                if self.wins > win_avg:
                        return "higher"
                if self.win == win_avg:
                        return "average"

        def annual_bonus(self):
                if 0 < self.team_age < 15:
                        team_bonus = 1.3
                elif 15 < self.team_age <35:
                        team_bonus = 15.5
                elif 35 < self.team_age <55:
                        team_bonus = 25.2
                elif self.team_age > 75:
                        team_bonus = 30
                
                win_bonus = ((self.wins / 2) * 6)
                
                annual_bonus = win_bonus + team_bonus
                
                return annual_bonus

        def display_welcome(self):
                print()
                print("Welcome, I'm with the FIA.")
                print(self.__str__())

"""Calculating team bonus for teams based off years as a member of FIA."""
# -----------------------------------1---------------------------------
#Call Functions and Exicute Code

#Asking for five years of race wins.
win_list = []
list_lenght = 5

for test in range (list_lenght):
        win_list.append(int(input('Enter total wins for team: ')))

if __name__ == "__main__":

#create an instance ofa PyBuddy
        Toto = PyBuddy(
                name ="Toto",
                positions = positions.manager,
                founded = 1970,
                team_age = 53,
                wins = 125,
                team = f"Mercedes",
               available = False,
        )
#Call the buddy's welcome() method            
        Toto.display_welcome()

#create another instance of a PyBuddy
#using named arguments
Rex = PyBuddy(
        "Rex",
        positions.stratagist,
        1929,
        94,
        243,
        f"Ferrari",
        True,
        )
Rex.display_welcome()