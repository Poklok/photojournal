FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY Pipfile Pipfile.lock ./

RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /code
COPY . /code

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /code
CMD ["python", "main.py"]


