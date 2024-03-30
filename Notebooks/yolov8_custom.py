import os
from ultralytics import YOLO

model = YOLO('best.pt')  # Load mode

image_path = './pic.png'

# Run inference on the source
results = model(source = image_path, show = True, conf = 0.4, save = True, project = './output', name = 'result')  
# results = model.predict('pic.png')  # Save results to project/output
