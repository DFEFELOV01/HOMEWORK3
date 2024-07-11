#используй питон такой-то версии
FROM python:3.12.2-bookworm


WORKDIR /

COPY /pyproject.toml poetry.lock ./

RUN pip install fastapi==0.111.0 #установка нужных пакетов
RUN pip install uvicorn
RUN pip install --upgrade pip poetry==1.8.3
RUN poetry config virtualenvs.create false --local

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]