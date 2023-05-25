import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def giveSnooze(new_data, wake):
    # AI calculates and returns number of times user will snooze
    filename = 'finalized_model.sav'
    new_data = list(new_data)
    new_data[-1] = wake
    new_data = np.array(new_data).reshape(1, -1)
    loaded_model = pickle.load(open(filename, 'rb'))
    prediction = loaded_model.predict(new_data)
    return (prediction[0])
