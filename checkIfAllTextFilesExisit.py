import os


def textFileExists(image_file_path, text_file_path, classes_list):
    does_not_exist = {}
    for key in classes_list:
        does_not_exist[key] = []
    for class_name in does_not_exist.keys():
        directory = f'{image_file_path}/{class_name.lower()}/images'
        text_directory = f'{text_file_path}/{class_name.lower()}'
        text_file_list = os.listdir(text_directory)
        for i in range(len(text_file_list)):
            text_file_list[i] = text_file_list[i].removesuffix('.txt')
        for file_name in os.listdir(directory):
            file_name = file_name.removesuffix('.jpg')
            if file_name not in text_file_list:
                does_not_exist[class_name].append(file_name)

    print(f'missing text Files:\n{does_not_exist}')


def imageFileExists(image_file_path, text_file_path, classes_list):
    does_not_exist = {}
    for key in classes_list:
        does_not_exist[key] = []
    for class_name in does_not_exist.keys():
        text_directory = f'{text_file_path}/{class_name.lower()}'
        directory = f'{image_file_path}/{class_name.lower()}/images'
        image_file_list = os.listdir(directory)
        for i in range(len(image_file_list)):
            image_file_list[i] = image_file_list[i].removesuffix('.jpg')
        for file_name in os.listdir(text_directory):
            file_name = file_name.removesuffix('.txt')
            if file_name not in image_file_list:
                does_not_exist[class_name].append(file_name)

    print(f'missing image files:\n{does_not_exist}')


def withCombinedFiles(image_file_path, text_file_path, classes_list):
    does_not_exist = {}
    for key in classes_list:
        does_not_exist[key] = []
    text_directory = f'{text_file_path}'
    images = []
    class_name = None
    for class_name1 in does_not_exist.keys():
        class_name = class_name1
        directory = f'{image_file_path}/{class_name.lower()}/images'
        image_file_list = os.listdir(directory)
        for i in range(len(image_file_list)):
            image_file_list[i] = image_file_list[i].removesuffix('.jpg')
            images.append(image_file_list[i])
    for file_name in os.listdir(text_directory):
        file_name = file_name.removesuffix('.txt')
        if file_name not in images:
            does_not_exist[class_name].append(file_name)

    print(f'missing image files:\n{does_not_exist}')

    does_not_exist = {}
    for key in classes_list:
        does_not_exist[key] = []
    text_directory = f'{text_file_path}'
    text_file_list = os.listdir(text_directory)
    for class_name in does_not_exist.keys():
        directory = f'{image_file_path}/{class_name.lower()}/images'
        for i in range(len(text_file_list)):
            text_file_list[i] = text_file_list[i].removesuffix('.txt')
        for file_name in os.listdir(directory):
            file_name = file_name.removesuffix('.jpg')
            if file_name not in text_file_list:
                does_not_exist[class_name].append(file_name)

    print(f'missing text Files:\n{does_not_exist}')



if __name__ == '__main__':
    classes = ['Person', 'Car', 'Dog', 'Cat', 'Bicycle', 'Bus', 'Truck', 'Weapon', 'Fish', 'Airplane']
    # textFileExists(image_file_path='./openimages/train',
    #                text_file_path='./yolo_labels/train')
    #
    # imageFileExists(image_file_path='./openimages/train',
    #                text_file_path='./yolo_labels/train')

    # withCombinedFiles(image_file_path='./openimages/train',
    #                   text_file_path='./yolo_labels/combined/train')

    imageFileExists(image_file_path='./openimages/train',
                    text_file_path='./yolo_labels/train',
                    classes_list=classes)

    imageFileExists(image_file_path='./openimages/train',
                    text_file_path='./yolo_labels/val',
                    classes_list=classes)

    imageFileExists(image_file_path='./openimages/train',
                    text_file_path='./yolo_labels/test',
                    classes_list=classes)