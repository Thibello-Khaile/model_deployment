"""
    Simple file to create a sklearn model for deployment in our API

    Author: Explore Data Science Academy

    Description: This script is responsible for training a simple linear
    regression model which is used within the API for initial demonstration
    purposes.

"""

# Dependencies
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Fetch training data and preprocess for modeling
train = pd.read_csv('./data/df_cleaned.csv')

y_train = train[['load_shortfall_3h']]
X_train = train[['month', 'hour', 'dayofweek', 'quarter', 'weekofyear', 'dayofyear',
       'avg_wind_speed', 'avg_wind_deg', 'avg_rain_1h', 'avg_rain_3h',
       'avg_humidity', 'avg_clouds_all', 'avg_pressure', 'avg_snow_3h',
       'weather_id', 'avg_temp_max', 'avg_temp_min', 'avg_temp']]

# Fit model
lm_regression = LinearRegression(normalize=True)
print ("Training Model...")
lm_regression.fit(X_train, y_train)

# Pickle model for use within our API
save_path = '../assets/trained-models/model_.pkl'
print (f"Training completed. Saving model to: {save_path}")
pickle.dump(lm_regression, open(save_path,'wb'))
