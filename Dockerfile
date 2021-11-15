FROM python:3

WORKDIR /usr/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

EXPOSE 5000
# CMD [ "ddtrace-run", "python", "./src/app.py" ]
CMD [ "python", "./src/app.py" ]
