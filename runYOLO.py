import ultralytics
from ultralytics import YOLO
import torch

def train_model():
    num = 0
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    modelDir = './runs/detect/train4/weights/best.pt'
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

    # run prediction on the test dataset
    predict = model.predict(source='./data/obj/test')
    file = open('./runs/detect/train5/predictStuff.csv', 'w')
    file.write(f'{predict}')
    file.close()

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

