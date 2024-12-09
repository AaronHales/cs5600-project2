import ultralytics
from ultralytics import YOLO
import torch

def train_model():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Will be using {device}')
    modelDir = 'yolov8n.pt'
    model = YOLO(modelDir)
    imageSize = 640

    print('---------------- Training ----------------')
    train_results = model.train(data='data.yaml',
                                epochs=50,
                                imgsz=imageSize,
                                # batch=,
                                device=device,
                                val=True,)

    print('---------------- validating ----------------')
    # evaluate performance on the test set
    metrics = model.val(data='data.yaml',
                        split='test',
                        save_json=True,)

    print('---------------- exporting ----------------')
    # export format
    export_model = model.export(format='onnx')


if __name__ == '__main__':
    train_model()

