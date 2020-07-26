FROM python:3.7-alpine

COPY botutils/ /bots/botutils/
COPY bot.py /bots/bot.py
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3" ,"bot.py"]
