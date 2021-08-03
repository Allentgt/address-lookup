FROM python:3.7
ADD source .
RUN pip install -r requirements.txt
CMD python main.py
