FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only necessary files
COPY core/ core/
COPY task1/ task1/
COPY manage.py .
COPY requirements .
COPY README.md .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements

EXPOSE 8080

# Run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
