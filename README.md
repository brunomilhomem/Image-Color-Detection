# Image Color Detection
_The main idea of it, is to deliver a program which the user would be able to select a picture and upload it to the API (application programming interface), chose whatever pixel available in the image, and then the program would display the color name and RGB number._


# Methods

The project was built in three steps:

| Nr. | Steps |
| ------ | ------ |
| 1 | Backend development - The functionalities to upload the files and capture the mouse event clicks were created as REST API using FastApi() in the Backend. |
| 2 | Frontend development - Where Users will be able to interact with API’s created to upload an image and find out the colors selected in the image. |
| 3 | An Open cv algorithm to find the R, G, B value of the coordinates in the image and find the color name from a database. |


# Installation

```sh
python -m pip install -r backend/requirements.txt
python -m pip install -r frontend/requirements.txt
```