import pandas as pd

player = ['player1', 'player2', 'player3']
point = [8, 9, 6]
title = ['Game1', 'Game2', 'Game3']
df1 = pd.DataFrame({'Player': player, 'Points': point,
                    'Title': title}, index=['L2', 'L3', 'L4'])

player = ['player1', 'player5', 'player6']
power = ['punch', 'kick', 'elbow']
title = ['Game1', 'Game5', 'Game6']
df2 = pd.DataFrame({'Players': player, 'Power': power,
                    'Titles': title}, index=['L1', 'L2', 'L3'])

df3 = pd.concat([df1, df2])
print(df3)