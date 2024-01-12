import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Set display format
pd.options.display.float_format = '{:,.2f}'.format

# Read the dataset
df_data = pd.read_csv('nobel_prize_data.csv')

# Group by year and count the number of Nobel Prizes
prize_per_year = df_data.groupby('year').size()

# Calculate a 5-year moving average
moving_average = prize_per_year.rolling(window=5).mean()

# Create an interactive plot using Plotly Express
fig = px.scatter(prize_per_year, x=prize_per_year.index, y=prize_per_year.values,
                 title='Number of Nobel Prizes Awarded per Year',
                 labels={'x': 'Year', 'y': 'Number of Prizes'},
                 template='plotly_dark',  # Dark theme for an advanced look
                 trendline='lowess',  # Smooth trendline
                 trendline_color_override='red',  # Trendline color
                 color_discrete_sequence=['dodgerblue'],  # Dot color
                 opacity=0.7,  # Dot opacity
                 size_max=100,  # Maximum dot size
                 size=np.ones_like(prize_per_year) * 10)  # Initial dot size

# Update the layout for advanced styling
fig.update_layout(
    title={'text': 'Number of Nobel Prizes Awarded per Year', 'x': 0.5, 'y': 0.92, 'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 18}},
    xaxis=dict(tickfont=dict(size=14), tickvals=np.arange(1900, 2021, step=5), tickangle=45, title='Year', title_font=dict(size=16)),
    yaxis=dict(tickfont=dict(size=14), title='Number of Prizes', title_font=dict(size=16)),
    showlegend=False,  # Hide legend for simplicity
    hovermode='closest',  # Display the hover information for the closest point
    annotations=[
        dict(x=1905, y=prize_per_year.loc[1905], xref="x", yref="y",
             text="Landsteiner discovers blood groups", showarrow=True, arrowhead=5, ax=0, ay=-40),
        dict(x=1911, y=prize_per_year.loc[1911], xref="x", yref="y",
             text="Marie Curie wins second Nobel Prize", showarrow=True, arrowhead=5, ax=0, ay=-40),
    ],
)

# Add a dynamic line annotation at the last year
fig.add_shape(type='line',
              x0=prize_per_year.index[-1], x1=prize_per_year.index[-1],
              y0=0, y1=prize_per_year.iloc[-1],
              line=dict(color='green', width=2, dash='dash'))

# Display the figure
fig.show()
