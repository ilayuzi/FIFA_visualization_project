import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
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


# Load the data for each position and year (replace with your own data)
goalkeeper_lst = [(fifa17_goalkeeper, "fifa 17 goalkeeper"), (fifa18_goalkeeper, "fifa 18 goalkeeper"), (fifa19_goalkeeper, "fifa 19 goalkeeper"), (fifa20_goalkeeper, "fifa 20 goalkeeper"), (fifa21_goalkeeper, "fifa 21 goalkeeper"), (fifa22_goalkeeper, "fifa 22 goalkeeper")]
defender_lst = [(fifa17_defender, "fifa 17 defender"), (fifa18_defender, "fifa 18 defender"), (fifa19_defender, "fifa 19 defender"), (fifa20_defender, "fifa 20 defender"), (fifa21_defender, "fifa 21 defender"), (fifa22_defender, "fifa 22 defender")]
midfielder_lst = [(fifa17_midfielder, "fifa 17 midfielder"), (fifa18_midfielder, "fifa 18 midfielder"), (fifa19_midfielder, "fifa 19 midfielder"), (fifa20_midfielder, "fifa 20 midfielder"), (fifa21_midfielder, "fifa 21 midfielder"), (fifa22_midfielder, "fifa 22 midfielder")]
forward_lst = [(fifa17_forward, "fifa 17 forward"), (fifa18_forward, "fifa 18 forward"), (fifa19_forward, "fifa 19 forward"), (fifa20_forward, "fifa 20 forward"), (fifa21_forward, "fifa 21 forward"), (fifa22_forward, "fifa 22 forward")]


fifa22.loc[fifa22['ID'] == 20801, 'Name'] = ' Cristiano Ronaldo'
fifa22.loc[fifa22['ID'] == 158023, 'Name'] = ' L. Messi'

def calculate_average_correlation(lst):
    all_sorted_correlations = []

    for dataset, title in lst:
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

        return sorted_correlations


abilities_to_check = calculate_average_correlation(forward_lst).to_dict()
top_abilities = list(abilities_to_check.keys())[:11]
top_abilities.insert(0,"Overall")



# Initialize empty lists for each player's ratings
messi_ratings = ronaldo_ratings = defaultdict(list)
ronaldo_ratings = {ability: [] for ability in top_abilities}
messi_ratings = {ability: [] for ability in top_abilities}



# Check if Messi and Ronaldo exist in each dataset and extract their ratings for each feature
datasets = [fifa17, fifa18, fifa19, fifa20, fifa21, fifa22]
features = top_abilities

for dataset in datasets:
    for feature in features:
            messi_ratings[feature].append(dataset.loc[dataset['Name'] == ' L. Messi', feature].values[0])
            ronaldo_ratings[feature].append(dataset.loc[dataset['Name'] == ' Cristiano Ronaldo', feature].values[0])

years = ['FIFA 17', 'FIFA 18', 'FIFA 19', 'FIFA 20', 'FIFA 21', 'FIFA 22']

# Create subplots for each feature
fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(14, 12))
plt.suptitle('Lionel Messi vs Cristiano Ronaldo - Ratings Comparison')

# Plot each feature on a separate subplot
for i, ax in enumerate(axes.flat):
    feature = features[i]
    ax.plot(years, messi_ratings[feature], marker='o', label='Messi')
    ax.plot(years, ronaldo_ratings[feature], marker='o', label='Ronaldo')
    ax.set_title(feature)
    ax.set_xlabel('FIFA Edition')
    ax.set_ylabel('Rating')
    ax.legend()

    # Set y-axis limits and ticks
    ax.set_ylim(70, 100)
    ax.set_yticks(range(70, 101, 2))

# Adjust the layout and spacing
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
st.pyplot(plt)

# # Plot the radar chart for the selected position
# plot_summary_radar_chart(position_lst, f"{position} : Impact of Abilities on Overall Rating - Average of All Years")
#
# # Display the radar chart using st.pyplot()
# st.pyplot(plt)
