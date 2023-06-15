import streamlit as st
import pandas as pd
import plotly.express as px

# Define the function to plot player distribution on a world map
def plot_player_distribution(dataset, n):
    # Load the dataset
    df = pd.read_csv(dataset)

    # Select the top n players by "Overall" attribute
    top_players = df.nlargest(n, "Overall")

    # Count the number of players with each nationality
    country_counts = top_players['Nationality'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']

    # Plot the world map with colored countries
    fig = px.choropleth(country_counts, locations='Country', locationmode='country names',
                        color='Count', title='Distribution of Top Players by Country',
                        hover_name='Country', color_continuous_scale='thermal')

    # Set the map projection to 'natural earth'
    fig.update_geos(projection_type="natural earth")

    # Display the plot
    st.plotly_chart(fig)


# Set the title of the app
st.title('Top Players Distribution')

# Define the dataset dictionary
datasets = {
    'fifa17': {
        'Goalkeeper': 'fifa17_goalkeeper.csv',
        'Defender': 'fifa17_defender.csv',
        'Midfielder': 'fifa17_midfielder.csv',
        'Forward': 'fifa17_forward.csv',
        'All Positions': 'fifa17.csv'
    },
    'fifa18': {
        'Goalkeeper': 'fifa18_goalkeeper.csv',
        'Defender': 'fifa18_defender.csv',
        'Midfielder': 'fifa18_midfielder.csv',
        'Forward': 'fifa18_forward.csv',
        'All Positions': 'fifa18.csv'
    },
    'fifa19': {
        'Goalkeeper': 'fifa19_goalkeeper.csv',
        'Defender': 'fifa19_defender.csv',
        'Midfielder': 'fifa19_midfielder.csv',
        'Forward': 'fifa19_forward.csv',
        'All Positions': 'fifa19.csv'
    },
    'fifa20': {
        'Goalkeeper': 'fifa20_goalkeeper.csv',
        'Defender': 'fifa20_defender.csv',
        'Midfielder': 'fifa20_midfielder.csv',
        'Forward': 'fifa20_forward.csv',
        'All Positions': 'fifa20.csv'
    },
    'fifa21': {
        'Goalkeeper': 'fifa21_goalkeeper.csv',
        'Defender': 'fifa21_defender.csv',
        'Midfielder': 'fifa21_midfielder.csv',
        'Forward': 'fifa21_forward.csv',
        'All Positions': 'fifa21.csv'
    },
    'fifa22': {
        'Goalkeeper': 'fifa22_goalkeeper.csv',
        'Defender': 'fifa22_defender.csv',
        'Midfielder': 'fifa22_midfielder.csv',
        'Forward': 'fifa22_forward.csv',
        'All Positions': 'fifa22.csv'
    }
}

# Dataset selection
selected_dataset = st.selectbox('Select a dataset', options=list(datasets.keys()))

# Position selection
positions = list(datasets[selected_dataset].keys())
selected_position = st.selectbox('Select a position', options=positions)

n_players = st.slider('Select the number of top players', min_value=10, max_value=500, value=100, step=10)

# Get the dataset filename based on the selected dataset and position
dataset_file = datasets[selected_dataset][selected_position]

# Plot the player distribution on a world map
plot_player_distribution(dataset_file, n_players)

