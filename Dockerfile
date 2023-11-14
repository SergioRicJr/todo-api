FROM python:3.11.5-alpine3.17
ENV PYTHONUBUFFERED 1
COPY . .
RUN pip install -r requirements.txt
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]