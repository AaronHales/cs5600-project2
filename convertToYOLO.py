import os
import cv2


# Function to convert Open Images annotations to YOLO format
def convertAnnotationsToYoloFormat(csv_file, images_dir, labels_dir, class_mapping, class_descriptions):
    # Read CSV file containing annotations
    df = open(csv_file, 'r')
    headers = df.readline().strip().split(',')
    image_id_index = headers.index('ImageID')
    class_index = headers.index('LabelName')
    x_min_index = headers.index('XMin')
    x_max_index = headers.index('XMax')
    y_min_index = headers.index('YMin')
    y_max_index = headers.index('YMax')

    for line in df:
        # Prepare a list of YOLO annotations
        yolo_annotations = []
        class_descript = ''

        line_data = line.strip().split(',')
        class_name = line_data[class_index]
        if class_name not in class_descriptions:
            continue
        image_id = line_data[image_id_index]
        class_descript = class_descriptions[class_name].lower()
        class_id = class_mapping[class_descriptions[class_name]]

        # Get the image dimensions (height, width)
        image_path = f'{images_dir}/{class_descriptions[class_name].lower()}/images/{image_id}.jpg'
        image = cv2.imread(image_path)
        if image is None:
            continue
        height, width, _ = image.shape

        # Get bounding box coordinates (normalized)
        xmin = float(line_data[x_min_index]) * width
        ymin = float(line_data[y_min_index]) * height
        xmax = float(line_data[x_max_index]) * width
        ymax = float(line_data[y_max_index]) * height

        # Calculate YOLO normalized values
        x_center = (xmin + xmax) / 2 / width
        y_center = (ymin + ymax) / 2 / height
        bbox_width = (xmax - xmin) / width
        bbox_height = (ymax - ymin) / height

        # Add YOLO formatted annotation
        yolo_annotations.append(f"{class_id} {x_center} {y_center} {bbox_width} {bbox_height}")

        # Save YOLO annotations in a text file
        if yolo_annotations:
            os.makedirs(f'{labels_dir}/{class_descript}', exist_ok=True)
            label_file = f'{labels_dir}/{class_descript}/{image_id}.txt'
            if os.path.isfile(label_file):
                with open(label_file, 'a') as f:
                    f.write(f'\n{"".join(yolo_annotations)}')
                    f.close()
            else:
                with open(label_file, 'w') as f:
                    f.write("".join(yolo_annotations))
                    f.close()
    df.close()


def getInfofromCSVFile(classes, csv_dir, images_dir, labels_dir):
    print('getting the needed class data')
    descriptionFile = open(f'{csv_dir}/class-descriptions-boxable.csv', 'r')
    class_descriptions = {}
    class_mapping = {}
    for line in descriptionFile:
        data = line.strip().split(',', 1)
        if data[1] not in classes:
            continue
        class_descriptions[data[0]] = [data[1]]
        class_mapping[data[1]] = (len(class_mapping.keys()) - 1)

    descriptionFile.close()
    print('converting the data to YOLO')
    convertAnnotationsToYoloFormat(
        csv_file=f'{csv_dir}/train-annotations-bbox.csv',
        images_dir=f'{images_dir}',
        labels_dir=f'{labels_dir}/train',
        class_mapping=class_mapping,
        class_descriptions=class_descriptions
    )
    # Convert annotations for validation dataset
    convertAnnotationsToYoloFormat(
        csv_file=f'{csv_dir}/validation-annotations-bbox.csv',
        images_dir=f'{images_dir}',
        labels_dir=f'{labels_dir}/val',
        class_mapping = class_mapping,
        class_descriptions = class_descriptions
    )
    # Convert annotations for test dataset
    convertAnnotationsToYoloFormat(
        csv_file=f'{csv_dir}/test-annotations-bbox.csv',
        images_dir=f'{images_dir}',
        labels_dir=f'{labels_dir}/test',
        class_mapping=class_mapping,
        class_descriptions=class_descriptions
    )


if __name__ == '__main__':
    # Mapping of Open Images class names to YOLO class IDs (from 0 to 9)
    class_mapping = {
        'Person': 0,
        'Car': 1,
        'Dog': 2,
        'Cat': 3,
        'Bicycle': 4,
        'Bus': 5,
        'Truck': 6,
        'Weapon': 7,
        'Fish': 8,
        'Airplane': 9,
    }

    class_descriptions = {
        '/m/01g317': 'Person',
        '/m/0k4j': 'Car',
        '/m/0bt9lr': 'Dog',
        '/m/01yrx': 'Cat',
        '/m/0199g': 'Bicycle',
        '/m/01bjv': 'Bus',
        '/m/07r04': 'Truck',
        '/m/083kb': 'Weapon',
        '/m/0ch_cf': 'Fish',
        '/m/0cmf2': 'Airplane',
    }
    # Convert annotations for training dataset
    convertAnnotationsToYoloFormat(
        csv_file='./openimages/csv/train-annotations-bbox.csv',
        images_dir='./openimages/train',
        labels_dir='./yolo_labels/train',
        class_mapping=class_mapping,
        class_descriptions=class_descriptions
    )
    # Convert annotations for validation dataset
    convertAnnotationsToYoloFormat(
        csv_file='./openimages/csv/validation-annotations-bbox.csv',
        images_dir='./openimages/train',
        labels_dir='./yolo_labels/val',
        class_mapping=class_mapping,
        class_descriptions=class_descriptions
    )
    # Convert annotations for test dataset
    convertAnnotationsToYoloFormat(
        csv_file='./openimages/csv/test-annotations-bbox.csv',
        images_dir='./openimages/train',
        labels_dir='./yolo_labels/test',
        class_mapping=class_mapping,
        class_descriptions=class_descriptions
    )
