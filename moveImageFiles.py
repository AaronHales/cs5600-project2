import shutil
import os

def moveImage(source, destination):
    shutil.copy(source, destination)


def moveImagesFromClass(source, destination, classes_list, text_dir):
    text_files = os.listdir(text_dir)
    for i in range(len(text_files)):
        text_files[i] = text_files[i].removesuffix('.txt')
    for class1 in classes_list:
        dir = f'{source}/{class1.lower()}/images'
        for file in os.listdir(dir):
            # print(os.path.isfile(f'{dir}/{file}'))
            if os.path.isfile(f'{dir}/{file}'):
                file_name = file.removesuffix('.jpg')
                if file_name in text_files:
                    moveImage(f'{dir}/{file}', destination)
        print(f'done with class: {class1}')


if __name__ == '__main__':
    classes = ['Person', 'Car', 'Dog', 'Cat', 'Bicycle', 'Bus', 'Truck', 'Weapon', 'Fish', 'Airplane']
    source = './openimages/train'
    destination = './data/obj'
    text_dir = './yolo_labels/combined'
    moveImagesFromClass(source=source, destination=f'{destination}/train', classes_list=classes,
                        text_dir=f'{text_dir}/train')
    moveImagesFromClass(source=source, destination=f'{destination}/val', classes_list=classes,
                        text_dir=f'{text_dir}/val')
    moveImagesFromClass(source=source, destination=f'{destination}/test', classes_list=classes,
                        text_dir=f'{text_dir}/test')