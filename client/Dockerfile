FROM python:3.8-alpine
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "-m","pytest","--cov","main","-vv"]
