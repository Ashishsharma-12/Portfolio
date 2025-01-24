# Use a minimal Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /main

# Copy requirements file to the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire application to the container
COPY . .

# Use JSON array syntax for CMD
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]