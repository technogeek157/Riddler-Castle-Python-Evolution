from __future__ import print_function
import itertools
import os
import csv
import pandas as pd
import pickle

def tourny():
    #Set current working directory to your directory
    directory=os.getcwd()
    os.chdir(directory)

    #Read in and view mocked up data
    df = pd.read_csv('CastleCompetition_Pre.csv')
    df.head()

    #subset data to eliminate player name column and just have player strategy
    a=df.iloc[:,1:11]

    #convert data set rows to a series of lists
    b=a.values.tolist()

    # Empty dictionary
    Team_Strategy = {}

    #Create a dictionary where the player name = key and the value is a list [[score],[tournament submission]]
    for i in range(len(df)):
        Team_Strategy[df['Player Name'][i]] = [[0],b[i]]

    for i in Team_Strategy:
        a = 1

    myPickle = open('fitness.pickle', 'r')

    f = pickle.load(myPickle)

    count = -1
    for i in f:
        count += 1
        Team_Strategy['evo' + str(count)] = [[0],i]

    #Creates a list of all players and then creates all the possible matchups
    Teams_Competing=Team_Strategy.keys()
    pairs = list(itertools.combinations(Teams_Competing, 2))

    #Runs the tournament
    for i in pairs:
        name1= i[0]
        name2= i[1]
        
        strat1 = Team_Strategy[name1][1] 
        strat2 = Team_Strategy[name2][1] 
        
        team1_score = 0
        team2_score = 0
        
        #Compares the knights sent to each castle and assigns points accordingly
        for i in range(len(strat1)):
            if strat1[i] > strat2[i]:
                team1_score += i
            elif strat1[i] < strat2[i]:
                team2_score +=i
            else:
                team1_score += i/2
                team2_score += i/2
        
        #Determines who won the match and updates the score in the players' dictionary accordingly
        if team1_score > team2_score:
            Team_Strategy[name1][0][0] += 1
        elif team1_score < team2_score:
            Team_Strategy[name2][0][0] += 1

        else:
            Team_Strategy[name1][0][0] += 0.5
            Team_Strategy[name2][0][0] += 0.5

    # Create a list of the final scores of all players in tournament
    final_score = list()
    for i in Teams_Competing:
        temp_score=Team_Strategy[i][0][0]
        final_score.append(temp_score)

    # Create a dataframe that includes player names and their final scores
    df_score=pd.DataFrame(
        {'Player Name': Teams_Competing,
         'Final Score':final_score,
        })

    fitnessList = []

    for i in Team_Strategy:
        if i[:3] == 'evo':
            fitnessList.append(Team_Strategy[i])

    for i in fitnessList:
        print(i)

    returnFitness = open('returnFitness.pickle', 'w')
    pickle.dump(fitnessList, returnFitness)
        
        
    # Join the initial dataframe (player names and their strategies) with the df_score dataframe
    df_final=pd.merge(df, df_score, on='Player Name')

    # View final data set
    df_final.head()

    # Save final dataframe as a csv file for later analysis
    df_final.to_csv('CastleCompetition_Post.csv')
