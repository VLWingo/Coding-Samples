# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:27:42 2021

@author: Victoria Wingo

DataCamp unguided project 
"Investigating Netflix Movies and Guest Stars in The Office"
Purpose: returns one guest star from The Office episode with 
the highest viewership and displays plots comparing the popularity and quality 
of episodes with and without guest appearances across the life of the series

"""

#All the packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mplc

# Import data from datasets/office_episodes.csv
location = "office_episodes.csv"
office_df = pd.read_csv(
                        location
                        )
office_df['HasGuests'] = ~office_df['GuestStars'].isnull()
max_rating = office_df['Ratings'].max()
office_df['ScaledRatings'] = office_df['Ratings'] / max_rating
print(office_df['ScaledRatings'])

stars_df = office_df[office_df['HasGuests'] == True]
nostars_df = office_df[office_df['HasGuests'] == False]

fig, ax = plt.subplots()
cmap, norm = mplc.from_levels_and_colors([0, 0.25, 0.5, 0.75, 1.1],
                                         ['red',
                                          'orange',
                                          'lightgreen',
                                          'darkgreen'])

plt.scatter(x = stars_df['Episode'],
            y = stars_df['Viewership'],
            c = stars_df['ScaledRatings'],
            cmap = cmap,
            norm = norm,
            s = 250,
            marker = '*',
            alpha = 0.75)
plt.scatter(x = nostars_df['Episode'],
            y = nostars_df['Viewership'],
            c = nostars_df['ScaledRatings'],
            cmap = cmap,
            norm = norm,
            s = 25,
            marker = 'o',
            alpha = 0.5)

ax.set_title("Popularity, Quality, and Guest Appearances on the Office")
ax.set_xlabel("Episode Number")
ax.set_ylabel("Viewership (Millions)")
plt.show()

top_star = office_df['GuestStars'].iloc[office_df['Viewership'].argmax()].split(", ")[1]
print(top_star)