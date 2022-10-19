FROM python:3.9
COPY . /App
WORKDIR /App
RUN pip install -r requirements.txt
CMD ["uvicorn","main:app", "--reload"]
EXPOSE 8000
