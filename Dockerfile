FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python", "product_list_app.py"]
