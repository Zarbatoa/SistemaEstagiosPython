FROM python:3
WORKDIR code
COPY . /code
RUN pip install -r requirements.txt
EXPOSE 8000
# RUN python3 manage.py migrate
CMD python3 manage.py runserver