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
1. Finish python api implementation
2. Build a database that can be dynamically refreshed from run.py
3. Build a react front end that displays stored data
3. Connect react front end to python backend run in docker instance
4. Build a shell script for running the project.
