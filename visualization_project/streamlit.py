import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# fifa17 = pd.read_csv('FIFA17_official_data.csv')
# fifa18 = pd.read_csv('FIFA18_official_data.csv')
# fifa19 = pd.read_csv('FIFA19_official_data.csv')
# fifa20 = pd.read_csv('FIFA20_official_data.csv')
# fifa21 = pd.read_csv('FIFA21_official_data.csv')
# fifa22 = pd.read_csv('FIFA22_official_data.csv')

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


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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

def plot_correlation(lst, position):
    fig, axes = plt.subplots(3, 2, figsize=(12, 16))
    axes = axes.flatten()

    for i, (dataset, title) in enumerate(lst):
        ability_ratings = dataset[['Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                                   'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed',
                                   'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength',
                                   'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties',
                                   'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
                                   'GKKicking', 'GKPositioning', 'GKReflexes']]
        overall_ratings = dataset['Overall']

        # Calculate correlation between personal abilities and overall rating
        correlation_matrix = ability_ratings.corrwith(overall_ratings)

        # Sort the correlations in descending order
        sorted_correlations = correlation_matrix.abs().sort_values(ascending=False)

        # Reverse the color order
        colors = sns.color_palette('coolwarm', len(sorted_correlations))[::-1]

        # Plot the sorted correlations with reversed colors
        ax = axes[i]
        sns.barplot(x=sorted_correlations.values, y=sorted_correlations.index, palette=colors, ax=ax)
        ax.set_xlabel('Correlation')
        ax.set_ylabel('Personal Ability')
        ax.set_title(title)

        # Add numbers on the bars
        for j, correlation in enumerate(sorted_correlations.values):
            ax.text(correlation, j, f'{correlation:.2f}', ha='left', va='center')
    plt.suptitle(f'{position}: Correlation between Personal Abilities and Overall Rating\n', fontsize=16,
                 fontweight='bold')
    plt.tight_layout()
    plt.show()


# Define the data for each position and year
goalkeeper_lst = [(fifa17_goalkeeper, "fifa 17 goalkeeper"), (fifa18_goalkeeper, "fifa 18 goalkeeper"), (fifa19_goalkeeper, "fifa 19 goalkeeper"), (fifa20_goalkeeper, "fifa 20 goalkeeper"), (fifa21_goalkeeper, "fifa 21 goalkeeper"), (fifa22_goalkeeper, "fifa 22 goalkeeper")]
defender_lst = [(fifa17_defender, "fifa 17 defender"), (fifa18_defender, "fifa 18 defender"), (fifa19_defender, "fifa 19 defender"), (fifa20_defender, "fifa 20 defender"), (fifa21_defender, "fifa 21 defender"), (fifa22_defender, "fifa 22 defender")]
midfielder_lst = [(fifa17_midfielder, "fifa 17 midfielder"), (fifa18_midfielder, "fifa 18 midfielder"), (fifa19_midfielder, "fifa 19 midfielder"), (fifa20_midfielder, "fifa 20 midfielder"), (fifa21_midfielder, "fifa 21 midfielder"), (fifa22_midfielder, "fifa 22 midfielder")]
forward_lst = [(fifa17_forward, "fifa 17 forward"), (fifa18_forward, "fifa 18 forward"), (fifa19_forward, "fifa 19 forward"), (fifa20_forward, "fifa 20 forward"), (fifa21_forward, "fifa 21 forward"), (fifa22_forward, "fifa 22 forward")]

# Create the position and year selection dropdowns
position = st.selectbox("Select Position", ["Goalkeeper", "Defender", "Midfielder", "Forward"])
# year = st.selectbox("Select Year", ["fifa17", "fifa18", "fifa19", "fifa20", "fifa21", "fifa22"])

# # Get the corresponding list based on the selected position and year
# if position == "Goalkeeper":
#     if year == "fifa17":
#         data_lst = [(fifa17_goalkeeper, "fifa 17 goalkeeper")]
#     elif year == "fifa18":
#         data_lst = [(fifa18_goalkeeper, "fifa 18 goalkeeper")]
#     elif year == "fifa19":
#         data_lst = [(fifa19_goalkeeper, "fifa 19 goalkeeper")]
#     elif year == "fifa20":
#         data_lst = [(fifa20_goalkeeper, "fifa 20 goalkeeper")]
#     elif year == "fifa21":
#         data_lst = [(fifa21_goalkeeper, "fifa 21 goalkeeper")]
#     elif year == "fifa22":
#         data_lst = [(fifa22_goalkeeper, "fifa 22 goalkeeper")]
# elif position == "Defender":
#     if year == "fifa17":
#         data_lst = [(fifa17_defender, "fifa 17 defender")]
#     elif year == "fifa18":
#         data_lst = [(fifa18_defender, "fifa 18 defender")]
#     elif year == "fifa19":
#         data_lst = [(fifa19_defender, "fifa 19 defender")]
#     elif year == "fifa20":
#         data_lst = [(fifa20_defender, "fifa 20 defender")]
#     elif year == "fifa21":
#         data_lst = [(fifa21_defender, "fifa 21 defender")]
#     elif year == "fifa22":
#         data_lst = [(fifa22_defender, "fifa 22 defender")]
# elif position == "Midfielder":
#     if year == "fifa17":
#         data_lst = [(fifa17_midfielder, "fifa 17 midfielder")]
#     elif year == "fifa18":
#         data_lst = [(fifa18_midfielder, "fifa 18 midfielder")]
#     elif year == "fifa19":
#         data_lst = [(fifa19_midfielder, "fifa 19 midfielder")]
#     elif year == "fifa20":
#         data_lst = [(fifa20_midfielder, "fifa 20 midfielder")]
#     elif year == "fifa21":
#         data_lst = [(fifa21_midfielder, "fifa 21 midfielder")]
#     elif year == "fifa22":
#         data_lst = [(fifa22_midfielder, "fifa 22 midfielder")]
# elif position == "Forward":
#     if year == "fifa17":
#         data_lst = [(fifa17_forward, "fifa 17 forward")]
#     elif year == "fifa18":
#         data_lst = [(fifa18_forward, "fifa 18 forward")]
#     elif year == "fifa19":
#         data_lst = [(fifa19_forward, "fifa 19 forward")]
#     elif year == "fifa20":
#         data_lst = [(fifa20_forward, "fifa 20 forward")]
#     elif year == "fifa21":
#         data_lst = [(fifa21_forward, "fifa 21 forward")]
#     elif year == "fifa22":
#         data_lst = [(fifa22_forward, "fifa 22 forward")]


# # Plot the correlation chart for the selected position and year
# plot_correlation(data_lst, f"{position}: Correlation between Personal Abilities and Overall Rating")
#
# # Display the correlation chart using st.pyplot()
# st.pyplot(plt)

# Plot the radar chart for the selected position
plot_summary_radar_chart(data_lst, f"{position}: Impact of Abilities on Overall Rating - Average of All Years")

# Display the radar chart using st.pyplot()
st.pyplot(plt)

