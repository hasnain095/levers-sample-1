FROM python:3.10.6

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY . .

RUN python /app/app/backend_pre_start.py

CMD ["/start-reload.sh"]