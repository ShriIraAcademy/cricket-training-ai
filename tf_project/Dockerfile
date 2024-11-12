# Start from the official Python image with version 3.9 (or another compatible version)
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # Prevents Python from writing .pyc files to disk
ENV PYTHONUNBUFFERED 1         # Ensures stdout and stderr are printed to the console

# Set up the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose the port the Django app will run on
EXPOSE 8000

# Run database migrations and start the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
