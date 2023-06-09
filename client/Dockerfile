FROM python:3.8-slim-buster
ADD client ./code
ADD common ./code

ENV HOST 0.0.0.0
ENV AUTH_PORT 5051
ENV MAFIA_PORT 5052

RUN cd code && \
    pip install --upgrade pip && \
    pip3 install -r requirements.txt && \
    ./generate_protos.sh

CMD ["python3", "./code/main.py"]