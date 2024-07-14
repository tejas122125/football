from ultralytics import YOLO 
import torch

model = YOLO("models/finetuned.pt")

results = model.predict('test1.mp4',save=True)
print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)