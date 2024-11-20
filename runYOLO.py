import ultralytics
from ultralytics import YOLO
import torch

def train_model():
    num = 0
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    modelDir = 'yolov8n.pt'
    model = YOLO(modelDir)

    print('---------------- Training ----------------')
    train_results = model.train(data='data.yaml',
                                epochs=100,
                                imgsz=640,
                                batch=7,
                                device=device)

    print('---------------- validating ----------------')
    # evaluate performance on the validation set
    metrics = model.val()

    predict = model.predict(source='./data/obj/train')
    file = open()

        # print('---------------- showing ----------------')
        # # perform obj detection on image
        # results = model('data/obj/test/2013_07_28_CHBRC_13_14_140_RH_VK.png')
        # for i in range(len(results)):
        #     results[i].show()
        #
        # results2 = model('data/obj/train/img8616.png')
        # for i in range(len(results2)):
        #     results2[i].show()

    print('---------------- exporting ----------------')
    # export format
    export_model = model.export(format='onnx')


if __name__ == '__main__':
    train_model()
