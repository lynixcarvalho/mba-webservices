# set base image (host OS)
FROM python:3.9-slim 

# set APP_CAR var to be used 
ENV WEBSITE /WEBSITE

# set the working directory in the container
WORKDIR $WEBSITE

# copy the dependencies file to the working directory
ADD . $WEBSITE

# install dependencies
RUN  python -m pip install --no-cache-dir -r ./requirements.txt

CMD python3 manage.py runserver 0.0.0.0:9000