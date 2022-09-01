FROM python:3.7-slim

RUN apt-get update && apt-get install -y libgomp1 \
    libzbar-dev \
    g++

# Install the function's dependencies
COPY notebooks notebooks
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /notebooks/

EXPOSE 8888
ENTRYPOINT ["jupyter","lab","--ip=0.0.0.0","--allow-root","--no-browser"],

