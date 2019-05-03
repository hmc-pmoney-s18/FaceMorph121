# FaceMorph

This is a web app that allows users morph two faces into a new image of their combined face. This new face can be anywhere between the two faces, from 99% of one face to 99% of another. Users can currently upload images from their devices and select the morphed rate to morph.

## The link to Web app
http://facemorph121.herokuapp.com/

## Prerequisites

* Flask
* OpenCV
* Dlib
* Heroku

## Frontend

The frontend of the web app is made by `Index.html`, which is a one page html file located in template floder and constructs the wireframe of the web app.
All of the css, js, and fonts files help style the index.html are located in static directory. This is benefical for flask api to locate the applied files.

## Controller

`app.py` is the control center for this web app. `app.py` takes the dynamic request from the frontend to recieve the uploaded image and selected morphed rate from the user and save in the local server. Then `app.py` pass the request to backend to form the morphed image. Once controller recieves the feedback from the backend. It makes a post request to the frontend.

## Backend

* `facemorph.py` is the main backend file, which handles the Image pre-pcocessing to get 68 facial landmarks and handles morphing process.
* `predict.dat` contains the information about all of the weights we use for the CNN model to get 68 facial landmarks from the user input facial image.

## Running the tests

Uploading the vague facial images or the images which contains non-human or multiple human faces to the webapp, which are unappropriate behaviors. The web app should return a error message correspondingly to warm the user to give out a correct input.

### Some Invalid example
Since "FaceMorph" only recognize the single front human facial image, then the following side face image, the multiple face image, and the non-human face image are invalid input to the webapp.

<img src="https://github.com/hmc-elephant-s18/FaceMorph/blob/master/cat.jpg" width="300" height="300">
<img src="https://github.com/hmc-elephant-s18/FaceMorph/blob/master/strange.jpg" width="300" height="300">
<img src="https://github.com/hmc-elephant-s18/FaceMorph/blob/master/avenger.jpg" width="300" height="300">


## Built With

* [flask] - Mirco Web framework by Python
* [heroku] - Platform to deploy the application


## Authors

* **Shihao Lin** - *Frontend & controller work* - [hmc-fly-f18](https://github.com/hmc-fly-f18)
* **Pascal Habineza** - *Backend & controller work* -[hmc-elephant-s18](https://github.com/hmc-elephant-s18)

See also the list of [contributors](https://github.com/hmc-elephant-s18/FaceMorph/contributors) who participated in this project.


## Acknowledgments

* Example programs for using dlib to detect facial landmarks http://dlib.net/face_landmark_detection.py.html

* Facial landmarks with dlib OpenCV and Python https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/

* Flask App main page http://flask.pocoo.org

* Heroku App main page https://www.heroku.com

* Face Landmarks detection model https://ibug.doc.ic.ac.uk/media/uploads/documents/sagonas_2016_imavis.pdf

* How to build a web application using Flask and deploy it to the cloud https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492

* Depoly your Flask Application to Heroku https://medium.com/the-andela-way/deploying-your-flask-application-to-heroku-c99050bce8f9
