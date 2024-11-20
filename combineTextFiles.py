import os


def combineTextFiles(yolo_labels_dir, combined_label_dir, classes_list):
    os.makedirs(f'{combined_label_dir}', exist_ok=True)

    for folder in classes_list:
        directory = f'{yolo_labels_dir}/{folder.lower()}'
        for file_name in os.listdir(directory):
            file_dir = f'{directory}/{file_name}'
            if not file_name.endswith('.txt'):
                continue
            with open(file_dir, 'r') as file:
                file_content = file.read().strip()
                output_dir = f'{combined_label_dir}/{file_name}'
                if os.path.isfile(output_dir):
                    with open(output_dir, 'a') as output_file:
                        output_file.write(f'\n{file_content}')
                        output_file.close()
                else:
                    with open(output_dir, 'w') as output_file:
                        output_file.write(f'{file_content}')
                        output_file.close()
            file.close()



if __name__ == '__main__':
    classes = ['Person', 'Car', 'Dog', 'Cat', 'Bicycle', 'Bus', 'Truck', 'Weapon', 'Fish', 'Airplane']
    combineTextFiles(yolo_labels_dir='./yolo_labels/train',
                     combined_label_dir='./yolo_labels/combined/train',
                     classes_list=classes)
    combineTextFiles(yolo_labels_dir='./yolo_labels/val',
                     combined_label_dir='./yolo_labels/combined/val',
                     classes_list=classes)
    combineTextFiles(yolo_labels_dir='./yolo_labels/test',
                     combined_label_dir='./yolo_labels/combined/test',
                     classes_list=classes)