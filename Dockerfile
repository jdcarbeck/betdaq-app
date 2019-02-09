# Python version for enviorment
FROM python:3.5-slim
#Set worrking directory to /app
WORKDIR /betdaq-app
#Copy contents from current directory to the worrking directory
COPY . /betdaq-app
#Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
#Run app when the container launches
CMD ["python", "betdaq.py"]
