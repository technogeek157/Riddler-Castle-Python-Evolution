from evolve import evolve
from pandas import DataFrame, read_csv
import pandas as pd

teamsUnaltered = []
teams = []

evolvedDict = evolve(1000)

for i in evolvedDict:
    teams.append(i[1])
print teams
