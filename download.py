from openimages import download

def downloadFiles(classes, dest_dir, csv_dir, annotation_format):


    # Download 'train' images and annotations for the specified classes
    download.download_dataset(class_labels=classes, dest_dir=dest_dir, csv_dir=csv_dir, annotation_format=annotation_format)

if __name__ == '__main__':
    downloadFiles(classes=['Person', 'Car', 'Dog', 'Cat', 'Bicycle', 'Bus', 'Truck', 'Weapon', 'Fish', 'Airplane'],
                  dest_dir='./openimages/train', csv_dir='./openimages/csv', annotation_format='pascal')