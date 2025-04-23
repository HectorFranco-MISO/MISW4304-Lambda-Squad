# Use a base image of Python 3.12
FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Upgrade pip and install the dependencies from requirements.txt
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the application source code to the container
COPY ./app /app/src

# Create a new user 'appuser' with user ID 5678, disable password, and change ownership of /app to appuser
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

# Switch to the new user 'appuser'
USER appuser

# Expose port 3000 for the application
EXPOSE 3000

# Command to run the application using Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3000"]