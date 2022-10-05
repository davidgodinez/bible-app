FROM python:3.9 
RUN addgroup app && useradd -r -g app appuser
# RUN apt-get update && apt install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0
RUN apt-get update && apt install -y libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 portaudio19-dev 
WORKDIR  /bible-app
COPY . .
RUN pip install -r requirements.txt
USER appuser
CMD ["python", "./bible/app2.py"]