import pandas as pd
import numpy as np
import JMP_Stats as jmp

# --- CREATION D' UN DATAFRAME - - - -
observations = pd.DataFrame({'NOTES': np.array([3, 19, 10, 15, 14, 12, 9, 8, 11, 12, 11, 12, 13, 11, 14, 16])})

# --- ANALYSE D' UNE FEATURE - - -
stats = jmp.JMPStatistiques(observations['NOTES'])
stats.analyseFeature()
