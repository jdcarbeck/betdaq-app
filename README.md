# betdaq-app
A application exemplifying the use of the betdaq API. Created for the Software
Engineering Project at Trinity College Dublin

## Setting up
The requirements for the project are listed in `requirements.txt` but it is suggested
that docker be installed and used as it will ensure the best environment for running the project

**RECOMENED:** read the *brief* documentation of zeep [here](https://python-zeep.readthedocs.io/en/master/index.html) 

### Running without Docker
1. Make sure that you have Python 3.6.2 installed using `python3 --version`
2. Using `pip install` install all that is listed in `requirements.txt`
3. in the root directory run `python3 run.py`

### Using Docker
1. Build the image in the root directory using `docker build -t betdaq .`
2. Run the image using `docker run betdaq`

##Project Plan
1. build python app that stores information for the current events 
