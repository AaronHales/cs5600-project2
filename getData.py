from download import downloadFiles
from  convertToYOLO import getInfofromCSVFile
from  combineTextFiles import combineTextFiles
from checkIfAllTextFilesExisit import imageFileExists
from moveImageFiles import moveImagesFromClass


def getData_fun():
    classes = ['Person', 'Car', 'Dog', 'Cat', 'Bicycle', 'Bus', 'Truck', 'Weapon', 'Fish', 'Airplane']
    dest_dir = './openimages/train'
    csv_dir = './openimages/csv'
    annotation_format = 'pascal'
    labels_dir = './yolo_labels'
    final_dir = './data/obj'

    downloadFiles(classes=classes, dest_dir=dest_dir, csv_dir=csv_dir, annotation_format=annotation_format)
    if annotation_format != 'darknet':
        getInfofromCSVFile(classes=classes, csv_dir=csv_dir, images_dir=dest_dir, labels_dir=labels_dir)
    imageFileExists(image_file_path=dest_dir, text_file_path=f'{labels_dir}/train', classes_list=classes)
    imageFileExists(image_file_path=dest_dir, text_file_path=f'{labels_dir}/val', classes_list=classes)
    imageFileExists(image_file_path=dest_dir, text_file_path=f'{labels_dir}/test', classes_list=classes)

    combineTextFiles(yolo_labels_dir=f'{labels_dir}/train', combined_label_dir=f'{final_dir}/train',
                     classes_list=classes)
    combineTextFiles(yolo_labels_dir=f'{labels_dir}/val', combined_label_dir=f'{final_dir}/vali',
                     classes_list=classes)
    combineTextFiles(yolo_labels_dir=f'{labels_dir}/test', combined_label_dir=f'{final_dir}/test',
                     classes_list=classes)

    imageFileExists(image_file_path=dest_dir, text_file_path=f'{final_dir}/train', classes_list=classes)
    imageFileExists(image_file_path=dest_dir, text_file_path=f'{final_dir}/val', classes_list=classes)
    imageFileExists(image_file_path=dest_dir, text_file_path=f'{final_dir}/test', classes_list=classes)

    moveImagesFromClass(source=dest_dir, destination=f'{final_dir}/train', classes_list=classes,
                        text_dir=f'{final_dir}/train')
    moveImagesFromClass(source=dest_dir, destination=f'{final_dir}/val', classes_list=classes,
                        text_dir=f'{final_dir}/val')
    moveImagesFromClass(source=dest_dir, destination=f'{final_dir}/test', classes_list=classes,
                        text_dir=f'{final_dir}/test')


if __name__ == '__main__':
    getData_fun()