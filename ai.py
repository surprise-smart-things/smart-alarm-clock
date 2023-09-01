import pickle
import numpy as np
import warnings
import tensorflow.keras
warnings.filterwarnings("ignore")

def giveSnooze(new_data, wake):
    # AI calculates and returns number of times user will snooze
    filename = 'model_v1.pkl'
    new_data = list(new_data)
    new_data[-1] = wake
    new_data = np.array(new_data).reshape(1, -1)
    loaded_model = pickle.load(open(filename, 'rb'))
    prediction = loaded_model.predict(new_data)
    return (np.where(prediction[0] >= 0.5)[0])

# print(giveSnooze())