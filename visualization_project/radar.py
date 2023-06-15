import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



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


# Load the data for each position and year (replace with your own data)
goalkeeper_lst = [(fifa17_goalkeeper, "fifa 17 goalkeeper"), (fifa18_goalkeeper, "fifa 18 goalkeeper"), (fifa19_goalkeeper, "fifa 19 goalkeeper"), (fifa20_goalkeeper, "fifa 20 goalkeeper"), (fifa21_goalkeeper, "fifa 21 goalkeeper"), (fifa22_goalkeeper, "fifa 22 goalkeeper")]
defender_lst = [(fifa17_defender, "fifa 17 defender"), (fifa18_defender, "fifa 18 defender"), (fifa19_defender, "fifa 19 defender"), (fifa20_defender, "fifa 20 defender"), (fifa21_defender, "fifa 21 defender"), (fifa22_defender, "fifa 22 defender")]
midfielder_lst = [(fifa17_midfielder, "fifa 17 midfielder"), (fifa18_midfielder, "fifa 18 midfielder"), (fifa19_midfielder, "fifa 19 midfielder"), (fifa20_midfielder, "fifa 20 midfielder"), (fifa21_midfielder, "fifa 21 midfielder"), (fifa22_midfielder, "fifa 22 midfielder")]
forward_lst = [(fifa17_forward, "fifa 17 forward"), (fifa18_forward, "fifa 18 forward"), (fifa19_forward, "fifa 19 forward"), (fifa20_forward, "fifa 20 forward"), (fifa21_forward, "fifa 21 forward"), (fifa22_forward, "fifa 22 forward")]

# Define the function for plotting the radar chart
def plot_summary_radar_chart(lst, main_title):
    all_ability_ratings = []
    all_overall_ratings = []

    # Iterate over the datasets
    for dataset, title in lst:
        # Select personal ability ratings and overall ratings for each player
        ability_ratings = dataset[['Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                                   'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed',
                                   'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength',
                                   'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties',
                                   'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
                                   'GKKicking', 'GKPositioning', 'GKReflexes']]
        overall_ratings = dataset['Overall']

        # Append the ability ratings and overall ratings to the lists
        all_ability_ratings.append(ability_ratings)
        all_overall_ratings.append(overall_ratings)

    # Concatenate all the ability ratings and overall ratings
    all_ability_ratings = pd.concat(all_ability_ratings)
    all_overall_ratings = pd.concat(all_overall_ratings)

    # Calculate the average ratings for each ability
    average_ratings = all_ability_ratings.mean()
    average_overall = all_overall_ratings.mean()

    # Normalize the average ratings and overall rating
    normalized_ratings = average_ratings / average_overall

    # Set up the radar chart
    categories = normalized_ratings.index
    values = normalized_ratings.values

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_yticklabels([])
    ax.set_title(main_title)

    plt.show()

# Define the function for plotting the correlation charts
# Create the position selection dropdown
position = st.selectbox("Select Position", ["Goalkeeper", "Defender", "Midfielder", "Forward"])

# Assign the appropriate list based on the selected position
if position == "Goalkeeper":
    position_lst = goalkeeper_lst
elif position == "Defender":
    position_lst = defender_lst
elif position == "Midfielder":
    position_lst = midfielder_lst
elif position == "Forward":
    position_lst = forward_lst

# Plot the radar chart for the selected position
plot_summary_radar_chart(position_lst, f"{position} : Impact of Abilities on Overall Rating - Average of All Years")

# Display the radar chart using st.pyplot()
st.pyplot(plt)


