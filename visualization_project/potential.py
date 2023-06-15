import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import pandas as pd
from mplsoccer import Pitch
import matplotlib.pyplot as plt
from collections import defaultdict

fifa17 = pd.read_csv('fifa17.csv')
fifa18 = pd.read_csv('fifa18.csv')
fifa19 = pd.read_csv('fifa19.csv')
fifa20 = pd.read_csv('fifa20.csv')
fifa21 = pd.read_csv('fifa21.csv')
fifa22 = pd.read_csv('fifa22.csv')

# FIFA 17
fifa17_defender = pd.read_csv('fifa17_defender.csv')
fifa17_midfielder = pd.read_csv('fifa17_midfielder.csv')
fifa17_forward = pd.read_csv('fifa17_forward.csv')
fifa17_goalkeeper = pd.read_csv('fifa17_goalkeeper.csv')

# FIFA 18
fifa18_defender = pd.read_csv('fifa18_defender.csv')
fifa18_midfielder = pd.read_csv('fifa18_midfielder.csv')
fifa18_forward = pd.read_csv('fifa18_forward.csv')
fifa18_goalkeeper = pd.read_csv('fifa18_goalkeeper.csv')

# FIFA 19
fifa19_defender = pd.read_csv('fifa19_defender.csv')
fifa19_midfielder = pd.read_csv('fifa19_midfielder.csv')
fifa19_forward = pd.read_csv('fifa19_forward.csv')
fifa19_goalkeeper = pd.read_csv('fifa19_goalkeeper.csv')

# FIFA 20
fifa20_defender = pd.read_csv('fifa20_defender.csv')
fifa20_midfielder = pd.read_csv('fifa20_midfielder.csv')
fifa20_forward = pd.read_csv('fifa20_forward.csv')
fifa20_goalkeeper = pd.read_csv('fifa20_goalkeeper.csv')

# FIFA 21
fifa21_defender = pd.read_csv('fifa21_defender.csv')
fifa21_midfielder = pd.read_csv('fifa21_midfielder.csv')
fifa21_forward = pd.read_csv('fifa21_forward.csv')
fifa21_goalkeeper = pd.read_csv('fifa21_goalkeeper.csv')

# FIFA 22
fifa22_defender = pd.read_csv('fifa22_defender.csv')
fifa22_midfielder = pd.read_csv('fifa22_midfielder.csv')
fifa22_forward = pd.read_csv('fifa22_forward.csv')
fifa22_goalkeeper = pd.read_csv('fifa22_goalkeeper.csv')

### highest difference

# Sorting the FIFA 17 dataset by the difference between Potential and Overall ratings in descending order and selecting top 20 players
top_50_players_fifa17_defender = fifa17_defender.assign(
    Difference=fifa17_defender['Potential'] - fifa17_defender['Overall']).nlargest(50, 'Difference')
top_50_players_fifa17_midfielder = fifa17_midfielder.assign(
    Difference=fifa17_midfielder['Potential'] - fifa17_midfielder['Overall']).nlargest(50, 'Difference')
top_50_players_fifa17_forward = fifa17_forward.assign(
    Difference=fifa17_forward['Potential'] - fifa17_forward['Overall']).nlargest(50, 'Difference')
top_50_players_fifa17_goalkeeper = fifa17_goalkeeper.assign(
    Difference=fifa17_goalkeeper['Potential'] - fifa17_goalkeeper['Overall']).nlargest(50, 'Difference')
# Create empty DataFrames for each position
result_df_defender = pd.DataFrame(columns=['ID', 'Name', 'Potential 17', 'Overall 17', 'Potential 18', 'Overall 18',
                                           'Potential 19', 'Overall 19', 'Potential 20', 'Overall 20',
                                           'Potential 21', 'Overall 21', 'Potential 22', 'Overall 22'])

result_df_midfielder = pd.DataFrame(columns=['ID', 'Name', 'Potential 17', 'Overall 17', 'Potential 18', 'Overall 18',
                                             'Potential 19', 'Overall 19', 'Potential 20', 'Overall 20',
                                             'Potential 21', 'Overall 21', 'Potential 22', 'Overall 22'])

result_df_forward = pd.DataFrame(columns=['ID', 'Name', 'Potential 17', 'Overall 17', 'Potential 18', 'Overall 18',
                                          'Potential 19', 'Overall 19', 'Potential 20', 'Overall 20',
                                          'Potential 21', 'Overall 21', 'Potential 22', 'Overall 22'])

result_df_goalkeeper = pd.DataFrame(columns=['ID', 'Name', 'Potential 17', 'Overall 17', 'Potential 18', 'Overall 18',
                                             'Potential 19', 'Overall 19', 'Potential 20', 'Overall 20',
                                             'Potential 21', 'Overall 21', 'Potential 22', 'Overall 22'])

lst = [(top_50_players_fifa17_defender, result_df_defender), (top_50_players_fifa17_midfielder, result_df_midfielder),
       (top_50_players_fifa17_forward, result_df_forward), (top_50_players_fifa17_goalkeeper, result_df_goalkeeper)]
for top_50, df in lst:
    # Looping through the top 20 players and extracting their data from the respective datasets
    for index, player in top_50.iterrows():
        player_id = player['ID']
        player_name = player['Name']
        potential_17 = player['Potential']
        overall_17 = player['Overall']
        player_data = [player_id, player_name, potential_17, overall_17]

        # Extracting potential and overall values from FIFA 18 to FIFA 22
        for year, dataset in zip(['18', '19', '20', '21', '22'], [fifa18, fifa19, fifa20, fifa21, fifa22]):
            try:
                player_row = dataset.loc[dataset['ID'] == player_id]
                potential = player_row['Potential'].values[0]
                overall = player_row['Overall'].values[0]
            except IndexError:
                potential = None
                overall = None

            # Add player data to the DataFrame only if Potential is higher than 75
            if potential is not None and potential > 75:
                player_data.extend([potential, overall])
            else:
                player_data.extend([None, None])

        # Add player data to the DataFrame only if Potential is higher than 75
        if player_data[2] is not None and player_data[2] > 75:
            df.loc[index] = player_data

# Deleting rows with None values and keeping 20 rows in each dataset

# Deleting rows with None values
result_df_defender = result_df_defender.dropna()
result_df_midfielder = result_df_midfielder.dropna()
result_df_forward = result_df_forward.dropna()
result_df_goalkeeper = result_df_goalkeeper.dropna()

# Keeping 20 rows in each dataset
result_df_defender = result_df_defender.head(30)
result_df_midfielder = result_df_midfielder.head(30)
result_df_forward = result_df_forward.head(30)
result_df_goalkeeper = result_df_goalkeeper.head(30)


def plot_summary(result_df, title):
    # Selecting the players from result_df
    players = result_df['Name'].tolist()

    # Creating subplots for all players
    num_players = len(players)
    num_cols = 3
    num_rows = (num_players + num_cols - 1) // num_cols

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))

    # Creating line plots for each player
    for i, player in enumerate(players):
        player_data = result_df[result_df['Name'] == player]

        # years = ['17', '18', '19', '20', '21', '22']
        years = ['FIFA 17', 'FIFA 18', 'FIFA 19', 'FIFA 20', 'FIFA 21', 'FIFA 22']
        potentials = player_data[
            ['Potential 17', 'Potential 18', 'Potential 19', 'Potential 20', 'Potential 21', 'Potential 22']].values[0]
        overalls = \
        player_data[['Overall 17', 'Overall 18', 'Overall 19', 'Overall 20', 'Overall 21', 'Overall 22']].values[0]

        row = i // num_cols
        col = i % num_cols

        ax = axes[row, col]
        ax.plot(years, potentials, marker='o', label='Potential')
        ax.plot(years, overalls, marker='o', label='Overall')

        ax.set_title(f"Player: {player}")
        ax.set_xlabel("Year")
        ax.set_ylabel("Rating")
        # ax.legend()

    # Adding main title
    fig.suptitle(title, fontsize=16, y=1.05)

    # Creating a single legend for all plots
    handles, labels = ax.get_legend_handles_labels()
    # fig.legend(handles, labels, loc='center', bbox_to_anchor=(0.5, -0.02), ncol=2)
    fig.legend(handles, labels, loc='upper left')

    # Adjusting the layout and spacing
    plt.tight_layout()

    # Displaying the figure
    plt.show()
    st.pyplot(plt)


position = st.selectbox("Select Position", ["Goalkeeper", "Defender", "Midfielder", "Forward"])

# Assign the appropriate list based on the selected position
if position == "Goalkeeper":
    plot_summary(result_df_goalkeeper, "Goalkeeper Position")
elif position == "Defender":
    plot_summary(result_df_defender, "Defender Position")
elif position == "Midfielder":
    plot_summary(result_df_midfielder, "Midfielder Position")
elif position == "Forward":
    plot_summary(result_df_forward, "Forward Position")
