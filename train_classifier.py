import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

import pickle
import os
file_path = 'C:\\Users\\rjmka\\OneDrive\\Desktop\\Project_exhib\\data.pickle'
if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        data_dict = pickle.load(file)
else:
    print(f"File {file_path} not found.")

fixed_data = []
max_length = 84  
for element in data_dict['data']:
    if len(element) < max_length:
        element = element + [0] * (max_length - len(element)) 
    fixed_data.append(element[:max_length]) 

data = np.asarray(fixed_data)
labels = np.asarray(data_dict['labels'])


x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)


model = RandomForestClassifier()
model.fit(x_train, y_train)


y_predict = model.predict(x_test)


score = accuracy_score(y_predict, y_test)
print('{}% of samples were classified correctly!'.format(score * 100))


with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)
