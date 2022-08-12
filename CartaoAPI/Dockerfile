# set base image (host OS)
FROM python:3.9-slim 

# set APP_CAR var to be used 
ENV CARTAO_API /CARTAO_API

# set the working directory in the container
WORKDIR $CARTAO_API

# copy the dependencies file to the working directory
ADD . $CARTAO_API

# install dependencies
RUN  python -m pip install --no-cache-dir -r ./requirements.txt

CMD uvicorn api:app --host 0.0.0.0 --port 8001 --reload