# set base image (host OS)
FROM python:3.9-slim 

# set APP_CAR var to be used 
ENV CLIENTE_API /CLIENTE_API

# set the working directory in the container
WORKDIR $CLIENTE_API

# copy the dependencies file to the working directory
ADD . $CLIENTE_API

# install dependencies
RUN  python -m pip install --no-cache-dir -r ./requirements.txt

CMD uvicorn api:app --host 0.0.0.0 --port 9100 --reload