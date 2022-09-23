FROM python:3.9 
# Or any preferred Python version.
RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN pip install pyaudio
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY . bible-app/
WORKDIR  /bible-app
RUN pip install -r ./requirements3.txt
CMD [“python”, “./app.py”] 
# Or enter the name of your unique directory and parameter set.