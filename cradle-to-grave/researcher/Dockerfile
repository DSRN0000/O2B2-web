FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8504

CMD ["streamlit", "run", "researcher.py", "--server.port=8504", "--server.address=0.0.0.0"]
ENV PYTHONPATH=/app