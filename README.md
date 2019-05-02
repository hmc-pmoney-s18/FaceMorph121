# FaceMorph

The web app allows users morph two faces into a new image of their combined face. This new face can be anywhere between the two faces, from 99% of one face to 99% of another. Users can currently upload images from their devices and select the morphed rate to morph.

## The link to Web app
http://facemorph121.herokuapp.com/

## Prerequisites

* Flask
* OpenCV
* Dlib
* Heroku

## Frontend

The frontend of the web app is made by `Index.html`, which is a one page html file located in template floder and constructs the wireframe of the web app.
All of the css, js, and font files help to implement the index.html are located in static directory. This is benefical for flask api to locate the applied files.

## Controllor

`app.py` is the control center for this web app. `app.py` takes the dynamic request from the frontend to recieve the uploaded image and selected morphed rate from the user and save in the local server. Then `app.py` pass the request to backend to form the morphed image. Once controller recieves the feedback from the backend. It makes a post request to the frontend.

## Backend

* `facemorph.py` is the main backend file, which handles the Image pre-pcocessing to get 68 facial landmarks and handles morphing process.
* `predict.dat` contains the information about all of the weights we use for the CNN model to get 68 facial landmarks from the user input facial image.

## Running the tests

Uploading the vague facial images or the images which contains non-human or multiple human faces to the webapp, which are unappropriate behaviors. The web app should return a error message correspondingly to warm the user to give out a correct input.

### Some Invalid example


### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


## Acknowledgments

* Example programs for using dlib to detect facial landmarks http://dlib.net/face_landmark_detection.py.html

* Facial landmarks with dlib OpenCV and Python https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/

* Flask App main page http://flask.pocoo.org

* Heroku App main page https://www.heroku.com

* How to build a web application using Flask and deploy it to the cloud https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492

* Depoly your Flask Application to Heroku https://medium.com/the-andela-way/deploying-your-flask-application-to-heroku-c99050bce8f9
