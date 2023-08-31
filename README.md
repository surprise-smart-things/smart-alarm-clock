# Ai-Smart-Clock
## Project Description
This project is centered around developing a smart alarm system that leverages machine learning to predict the optimal time to ring the alarm based on the user's sleep patterns and snooze behavior.
### Features
<ul>
  <li><h3>Snooze-Count Prediction</h3>Using the Google Fitness API, the project retrieves sleep data from smart wearables. By analyzing this data, including bedtime, sleep cycles(N1,N2,N3,REM), and waking time, an ML model is trained to predict the user's snooze behavior. The model estimates the potential number of snoozes the user might take after the initial alarm rings.
</li>
  <li><h3>Alarm Time Calculation</h3>Leveraging the predicted snooze count and considering the user's desired wake-up time, the system calculates the optimal time to initially set the alarm. This calculation takes into account the snooze duration, ensuring that the user can still get the desired amount of sleep despite potential snoozes.
  </li>
</ul>

## How to run the project
1. **Download the dataset** : Save the dataset 'kk.csv' locally
2. **Train the ML model** : Open the file 'aitrain.ipynb' and run the script to train the machine learning model using the dataset
3. **Prepare the pickle model** : Open the file 'model_vi.pkl




