import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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


goalkeeper_lst = [(fifa17_goalkeeper, "fifa 17 goalkeeper"), (fifa18_goalkeeper, "fifa 18 goalkeeper"), (fifa19_goalkeeper, "fifa 19 goalkeeper"), (fifa20_goalkeeper, "fifa 20 goalkeeper"), (fifa21_goalkeeper, "fifa 21 goalkeeper"), (fifa22_goalkeeper, "fifa 22 goalkeeper")]
defender_lst = [(fifa17_defender, "fifa 17 defender"), (fifa18_defender, "fifa 18 defender"), (fifa19_defender, "fifa 19 defender"), (fifa20_defender, "fifa 20 defender"), (fifa21_defender, "fifa 21 defender"), (fifa22_defender, "fifa 22 defender")]
midfielder_lst = [(fifa17_midfielder, "fifa 17 midfielder"), (fifa18_midfielder, "fifa 18 midfielder"), (fifa19_midfielder, "fifa 19 midfielder"), (fifa20_midfielder, "fifa 20 midfielder"), (fifa21_midfielder, "fifa 21 midfielder"), (fifa22_midfielder, "fifa 22 midfielder")]
forward_lst = [(fifa17_forward, "fifa 17 forward"), (fifa18_forward, "fifa 18 forward"), (fifa19_forward, "fifa 19 forward"), (fifa20_forward, "fifa 20 forward"), (fifa21_forward, "fifa 21 forward"), (fifa22_forward, "fifa 22 forward")]



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

    st.pyplot(fig)

def plot_average_correlation(lst, title_pos):
    # Create an empty DataFrame to store the combined data
    combined_dataset = pd.DataFrame()

    # Combine the data from all the years into one DataFrame
    for dataset, title in lst:
        combined_dataset = pd.concat([combined_dataset, dataset])

    ability_ratings = combined_dataset[['Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                                        'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed',
                                        'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength',
                                        'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties',
                                        'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
                                        'GKKicking', 'GKPositioning', 'GKReflexes']]
    overall_ratings = combined_dataset['Overall']

    # Calculate correlation between personal abilities and overall rating
    correlation_matrix = ability_ratings.corrwith(overall_ratings)

    # Sort the correlations in descending order
    sorted_correlations = correlation_matrix.abs().sort_values(ascending=False)

    # Reverse the color order
    colors = sns.color_palette('coolwarm', len(sorted_correlations))[::-1]

    # Plot the sorted correlations with reversed colors
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sorted_correlations.values, y=sorted_correlations.index, palette=colors)
    plt.xlabel('Correlation')
    plt.ylabel('Personal Ability')
    plt.title(f'{title_pos} Average Correlation between Personal Abilities and Overall Rating')

    # Add numbers on the bars
    for i, correlation in enumerate(sorted_correlations.values):
        plt.text(correlation, i, f'{correlation:.2f}', ha='left', va='center')

    plt.show()
    st.pyplot(plt)


roles_lst = [(goalkeeper_lst, "GK"), (defender_lst, "Defenders"), (midfielder_lst, "Midfielders"),
             (forward_lst, "Forwards")]

# Create a selectbox to choose the position
position = st.selectbox("Choose a position:", ["GK", "Defenders", "Midfielders", "Forwards","Averages"])

if position == "Averages":
    plot_average_correlation(goalkeeper_lst, "GK")
    plot_average_correlation(defender_lst, "Defenders")
    plot_average_correlation(midfielder_lst, "Midfielders")
    plot_average_correlation(forward_lst, "Forwards")
else:
    # Find the corresponding list for the selected position
    lst = next((lst for lst, role in roles_lst if role == position), None)

    # If the list is found, plot the correlation
    if lst is not None:
        plot_correlation(lst, position)





