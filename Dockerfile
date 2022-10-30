FROM python:3.10.6

WORKDIR /Procfile
COPY . /Procfile

RUN pip3 install -U pip
COPY requirments.txt .
RUN pip3 install -r requirments.txt

CMD ["python3", "-m", "app"]
