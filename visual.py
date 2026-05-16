import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2, 2, figsize=(18, 14))
fig.suptitle('IPL Analysis Dashboard 🏏', 
             fontsize=24, fontweight='bold', y=1.02)

win_counts = matches[matches['winner'] != 'No Result']['winner']\
             .value_counts().head(10)

colors1 = ['gold' if i < 3 else 'steelblue' 
           for i in range(len(win_counts))]

axes[0,0].barh(win_counts.index, win_counts.values, color=colors1)
axes[0,0].set_title('Most Successful Teams 🏆', fontweight='bold')
axes[0,0].set_xlabel('Total Wins')

matches['toss_match_winner'] = matches['toss_winner'] == matches['winner']
toss_effect = matches['toss_match_winner'].value_counts()

axes[0,1].pie(toss_effect.values,
              labels=['Toss Jeet ke Haara', 'Toss Jeet ke Jeeta'],
              colors=['steelblue', 'gold'],
              autopct='%1.1f%%',
              startangle=90)
axes[0,1].set_title('Toss = Match Win?', fontweight='bold')

season_matches = matches.groupby('season').size()

axes[1,0].plot(season_matches.index, season_matches.values,
               marker='o', linewidth=2, 
               color='steelblue', markersize=8)
axes[1,0].set_title('Matches Per Season 📈', fontweight='bold')
axes[1,0].set_xlabel('Season')
axes[1,0].set_ylabel('Total Matches')
axes[1,0].grid(True, alpha=0.3)
axes[1,0].tick_params(axis='x', rotation=45)

top_players = matches[matches['player_of_match'] != 'No Result']\
              .groupby('player_of_match').size()\
              .sort_values(ascending=False).head(10)

colors4 = ['gold' if val >= 20 else 'steelblue' 
           for val in top_players.values]

axes[1,1].barh(top_players.index, top_players.values, color=colors4)
axes[1,1].set_title('Top 10 Player of Match 🌟', fontweight='bold')
axes[1,1].set_xlabel('Times Won')

plt.tight_layout()
plt.savefig('../ipl_dashboard.png', dpi=150, bbox_inches='tight')
plt.show()

print("✅ Dashboard saved!")