FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8503

CMD ["streamlit", "run", "public_organization.py", "--server.port=8503", "--server.address=0.0.0.0"]
ENV PYTHONPATH=/app