import pickle
import numpy as np
import warnings
import keras
warnings.filterwarnings("ignore")

def giveSnooze(new_data, step, wake ):
    # AI calculates and returns number of times user will snooze
    filename = 'model_v3.keras'
    new_data = list(new_data)
    new_data.append(step)
    print(new_data)
    new_data[-2] = wake
    new_data = np.array(new_data).reshape(1, -1)
    loaded_model = keras.models.load_model(filename)
    prediction = loaded_model.predict(new_data)
    return (np.where(prediction[0] >= 0.5)[0])

# print(giveSnooze())