import pandas as pd

player = ['player1', 'player2', 'player3']
point = [8, 9, 6]
title = ['Game1', 'Game2', 'Game3']
df1 = pd.DataFrame({'Player': player, 'Points': point, 'Title': title}, index=['L2', 'L3', 'L4'])

player = ['player1', 'player5', 'player6']
power = ['punch', 'kick', 'elbow']
title = ['Game1', 'Game5', 'Game6']
df2 = pd.DataFrame({'Players': player, 'Power': power, 'Titles': title}, index=['L1', 'L2', 'L3'])
    

def main(df1):

    #/// Inner Join ///
    # * Se enlazan a partir del index
    print(df1)
    print(df2)

    df3 = df1.join(df2, how='inner')
    print(df3)

    #/// Left Join ///
    df3 = df1.join(df2, how='left')
    print(df3)

    #/// Right Join ///
    df3 = df1.join(df2, how='right')
    print(df3)

    #/// Outer Join ///
    # * Se obtienen todos los indices en total de los dos df
    df3 = df1.join(df2, how='outer')
    print(df3)

    return df1

if __name__ == '__main__':
    main(df1)
