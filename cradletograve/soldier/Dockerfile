FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8506

CMD ["streamlit", "run", "welfare.py", "--server.port=8506", "--server.address=0.0.0.0"]
ENV PYTHONPATH=/app