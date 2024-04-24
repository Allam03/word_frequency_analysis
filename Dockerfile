FROM python:3.9

RUN pip install nltk

WORKDIR /app

COPY script.py /app/
COPY paragraphs.txt /app/

CMD ["python", "script.py"]