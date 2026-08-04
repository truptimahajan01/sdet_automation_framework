FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run API tests by default (no Chrome needed in this image)
CMD ["pytest", "-m", "api", "-v", "--html=reports/report.html", "--self-contained-html"]