FROM tensorflow/tensorflow
WORKDIR /code

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
ENTRYPOINT ["python"]

CMD ["app.py"]