FROM python:3.10.6

RUN mkdir /levers

WORKDIR /levers

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./ /levers

ENV PYTHONPATH=/levers

#RUN python /levers/app/backend_pre_start.py

#CMD ["/start-reload.sh"]