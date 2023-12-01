# python 3.9 slim
FROM python:3.9-slim

COPY . /spotify_music_refresher
WORKDIR /spotify_music_refresher

RUN pip install -e .

CMD ["uvicorn", "spotify_music_refresher.main:app", "--host"]
