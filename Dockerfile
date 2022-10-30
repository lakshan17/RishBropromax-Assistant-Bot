FROM python:3.10.6

WORKDIR /Assistant
COPY . /Assistant
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "bot"]
