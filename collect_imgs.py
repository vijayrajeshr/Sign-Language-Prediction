import os
import cv2

# Define the data directory
DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Define the number of classes and dataset size
number_of_classes = 26
dataset_size = 10,100,250,500,

# Define the class labels
class_labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Open the video capture
cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    class_label = class_labels[j]
    class_dir = os.path.join(DATA_DIR, class_label)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {class_label} ({j + 1}/{number_of_classes})')

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.putText(frame, f'Class: {class_label} ({j + 1}/{number_of_classes})', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.putText(frame, f'Class: {class_label} ({j + 1}/{number_of_classes}) - Image {counter + 1}/{dataset_size}', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_dir, f'{counter}kararaj.jpg'), frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()
