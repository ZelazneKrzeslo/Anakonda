import matplotlib.pyplot as plt
import numpy as np

panstwa = np.array(["Niemcy", "Francja", "Włochy", "Anglia", "Hiszpania", "Holandia", "Belgia", "Szwecja", "Austria", "Dania", "Polska", "Grecja", "Finlandia", "Portugalia", "Irlandia", "Węgry", "Czechy", "Słowacja", "Luksemburg", "Litwa", "Cypr", "Łotwa", "Estonia", "Estonia", "Malta"])
PKB = np.array([22218438941, 17303107859, 14359479157, 13739900046, 8957286488, 5552933781, 4035286807, 2832862800, 2308432030, 2130860212, 2099087114, 1882611879, 1544832284, 1443049602, 1341281313, 1003119411, 932392859, 393148777, 299993572, 241439011, 221997405, 144556416, 115205431, 100756308, 57409269])

plt.bar(panstwa,PKB)
plt.show()