import pandas as pd 

# * Realizar una operacion merge

player = ['player1', 'player2', 'player3']

point = [8, 9, 6]
title = ['Game1', 'Game2', 'Game3']

df1 = pd.DataFrame({'Player': player, 'Points': point, 'Title': title})

print(df1)

player = ['player1', 'player5', 'player6']
power = ['punch', 'kick', 'elbow']
title = ['Game1', 'Game5', 'Game6']
df2 = pd.DataFrame({'Player': player, 'Power': power, 'Title': title})
print(df2)

#/// Inner Merge /// 


df3 = df1.merge(df2, on='Title', how='inner')
print(df3)

df4 = df1.merge(df2, on='Player', how='inner')
print(df4)

#/// Merge left /// 


df5 = df1.merge(df2, on='Player', how='left')
print(df5) 
# * Se obtienen todos los valores del DataFrame izq teniendo como referencia el atributo Player del primer DataFrame y 
# * los valores en comun que posee el segundo(df2)

#/// Merge right /// 

df6 = df1.merge(df2, on='Player', how='right')
print(df6) 
# * Se obtienen todos los valores del DataFrame der teniendo como referencia el atributo Player del segundo DataFrame y 
# * los valores en comun que posee el segundo(df2)

#/// Outer Merge /// 

df7 = df1.merge(df2, on='Player', how='outer')
print(df7) 
