import matplotlib.pyplot as plt
import numpy as np

wyniki = np.array([24.1, 25.7, 14.8, 11.5,10.3,4.9,8.6])
partie = ["CDU/CSU", "SPD", "GREENS", "FDP", "AID", "LEFT PARTY","INNE"]

plt.pie(wyniki, labels=partie, autopct='%1.1f%%')
plt.show()
plt.legend()
plt.axis('equal')
