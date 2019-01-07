FROM python:3.6-alpine
WORKDIR /root
COPY aliddns.py send_email.py requirements.txt ./
COPY logs logs 
RUN pip install -r requirements.txt

CMD ["python", "/root/aliddns.py"]
