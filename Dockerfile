FROM python@sha256:1cb6108b64a4caf2a862499bf90dc65703a08101e8bfb346a18c9d12c0ed5b7e


WORKDIR /app

COPY main.py /app
COPY /audio /app
COPY /images /app
COPY Dockerfile /app
COPY horrorland.py /app
COPY player.py /app
COPY requirements_new.txt /app
COPY audio.py /app

RUN pip install -r requirements_new.txt

ENTRYPOINT ["python"] ["main.py"]
