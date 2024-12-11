# How to use
## starting
### ? `getData.py` will do everything for starting out
first you will need to download the dataset
* run `download.py`
  * enter the desired classes into `classes` variable
  * this will go through and download all the files for those classes
* run `convertToYOLO.py`
  * this will go through and convert the dataset into a format that YOLO can use
  * set `label_dir` to the place where you want to label files to be saved
    * keep in mind that each label file with be in a folder for each class
* run `checkIfAllTextFilesExist.py` (not needed)
  * this will check to see if there is a text file for each image and an image for each text file
* run `combineTextFiles.py`
  * this will go through each classes text files and combine text files that are for the same image
  * set `yolo_label_dir` to the path to the classes label files
  * set `combined_label_dir` to the path that you want to combined file to be at
  * set `classes` to the list of the classes you downloaded
* run `moveImageFiles.py`
  * this is to move the image files to a different place based on mode used, which is found by the `annotation-bbox.csv` files
  * set `source` to the location of the image files downloaded
  * set `destination` to the location of to copy image files to
  * set `text_dir` to the location of the text files that were created
  * set `classes` to the list of classes used
  
### if you want to use `getData.py`
* set `classes` to the desired classes
* set `dest_dir` to the location you want the images to be location you want the images to be placed
* set `csv_dir` to the location you want the csv files to be downloaded to
* set `annotation_format` to the annotation format you want (either pascal or darknet)
* set `label_dir` to be the location you want the initial label files to be placed
* set `final_dir` to the location you want everything to end up

you will need to clean up the leftover files a bit, but now you should be all set

it will take a while for everything to finish, for me, it took a few hours to download classes I wanted, then 3-4 for 
getting the needed data from the csv files, then about 30-60 minutes of getting everything else done

now you are ready to train the model

## training
I have created a file named: `runYOLO.py` which I used to train my model. Refer to the documentation for YOLO for how to train the model, but I had it validate using the val split while it was training and then predict with the test split, but you can change that.
