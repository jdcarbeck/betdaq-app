# Software Engineering Project Group 31 - Betdaq
This project was completed by Brian Barry, Cian Begley, Joeseph Carnec, Sharleen Bang, Jack Donal Collins, John Davis Carbeck, and David Zhang.

## Installation & Dependencies
This project needs either python3 with pip3 or Docker
All required and used packages are in the requirements.txt file

## Running the Project
**a config.py file should be included with the project this contains the login for the API**
### Docker
If docker is installed:
1. go into the home dir of project
2. run `docker build -t betdaq .` to build docker
3. run image `docker run -it betdaq`

### Python
python 3 must be installed on machine as well as pip3
* `./run.sh install` used for running the project for the first time to install packages
* `./run.sh` for subsequent running of the project

## Use Cases
This python wrapper is used for querying the betdaq API and the sample application demonstrate the use of the wrapper so that that the user can implement betting stratigeies