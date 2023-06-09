FROM python:latest
ADD server ./code
ADD common ./code
WORKDIR /code

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    ./generate_protos.sh