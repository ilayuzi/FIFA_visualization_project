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


def find_dream_team(dataset, formation):
    # Remove rows with null values in the 'Position' column
    dataset = dataset.dropna(subset=['Position'])
    if formation == "433":
        # Define the core positions
        core_positions = ['GK', 'CB', 'RB', 'LB', 'CM', 'CDM', 'RW', 'LW', 'CF']
        double = ['CB', 'CM']
    elif formation == "442":
        core_positions = ['GK', 'CB', 'RB', 'LB', 'CM', 'RM', 'LM', 'ST']
        double = ['CB', 'CM', 'ST']
    elif formation == "4231":
        core_positions = ['GK', 'CB', 'RB', 'LB', 'CM', 'CDM', 'CAM', 'RW', 'LW', 'ST']
        double = ['CB']
    else:
        return {}

    # Initialize an empty dictionary to store the dream team
    dream_team = defaultdict(list)

    # Find the top player for each core position
    for position in core_positions:
        if position in double:
            top_players = dataset.loc[dataset['Best Position'].str.strip() == position].nlargest(2, 'Overall')
        else:
            top_players = dataset.loc[dataset['Best Position'].str.strip() == position].nlargest(1, 'Overall')
        if not top_players.empty:
            for i in range(len(top_players)):
                player_name = top_players.iloc[i]['Name']
                dream_team[position].append(player_name)

    return dream_team


def plot_dream_team(dream_team, year, formation):
    pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
    fig, ax = pitch.draw()

    # Define the positions on the pitch for the dream team
    positions = {
        'GK': [(5, 40)],
        'CB': [(25, 30), (25, 50)],
        'RB': [(25, 70)],
        'LB': [(25, 5)],
        'CM': [(65, 30), (65, 50)],
        'CDM': [(40, 40)],
        'CAM': [(85, 40)],
        'RM': [(70, 70)],
        'LM': [(70, 5)],
        'RW': [(90, 70)],
        'LW': [(90, 5)],
        'CF': [(100, 40)],
        'ST': [(105, 35), (105, 45)]
    }

    # Plot the dream team players on the pitch
    for position, players in dream_team.items():
        for i, player_name in enumerate(players):
            coords = positions[position][i]
            ax.text(coords[0], coords[1], player_name, color='black', ha='center', va='center', fontsize=12,
                    fontweight='bold')

    plt.title(f"{year} Dream Team with Formation: {formation}")
    plt.show()
    st.pyplot(plt)


games = ["FIFA20", "FIFA21", "FIFA22"]
formations = ["433", "4231", "442"]

# Create selectboxes to choose the game and formation
selected_game = st.selectbox("Choose a game:", games)
selected_formation = st.selectbox("Choose a formation:", formations)

# Find the corresponding dataset for the selected game
if selected_game == "FIFA20":
    dataset = fifa20
elif selected_game == "FIFA21":
    dataset = fifa21
elif selected_game == "FIFA22":
    dataset = fifa22

# If the dataset is not empty, find the dream team and plot it
if not dataset.empty:
    dream_team = find_dream_team(dataset, selected_formation)
    plot_dream_team(dream_team, selected_game, selected_formation)
else:
    st.write("No dataset available for the selected game.")

