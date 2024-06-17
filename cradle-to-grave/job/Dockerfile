FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8507
ENV PYTHONPATH=/app
CMD ["streamlit", "run", "job_selector.py", "--server.port=8507", "--server.address=0.0.0.0"]
