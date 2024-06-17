FROM python:3.9-slim

WORKDIR /home

COPY requirements.txt ./
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
ENV PYTHONPATH=/app

CMD ["streamlit", "run", "home_before_login.py", "--server.port=8501", "--server.address=0.0.0.0"]
