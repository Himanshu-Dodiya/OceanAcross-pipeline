FROM python:3.11-slim
WORKDIR /app
COPY src/ .
RUN pip install flask        # install dependencies at build time
EXPOSE 5000
CMD ["python", "main.py"]