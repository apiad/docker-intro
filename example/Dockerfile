FROM python:3.6
RUN pip install --no-cache-dir Flask pymongo
COPY ./app /app
EXPOSE 5000
CMD [ "python", "/app/app.py" ]