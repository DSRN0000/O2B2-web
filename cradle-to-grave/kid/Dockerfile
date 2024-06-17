FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8502

CMD ["streamlit", "run", "kid_gamification.py", "--server.port=8502", "--server.address=0.0.0.0"]
ENV PYTHONPATH=/app