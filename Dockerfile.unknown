FROM python:alpine3.7
ADD script.py . 
WORKDIR /script
COPY  . /script
RUN pip install --upgrade pip setuptools
RUN pip install nltk
EXPOSE 4000
CMD python ./script.py 