FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/start_page_app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /usr/src/start_page_app

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]