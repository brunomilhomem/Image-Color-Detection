FROM python:3.10.1-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]