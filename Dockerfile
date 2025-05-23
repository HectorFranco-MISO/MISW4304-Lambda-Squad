# Use a base image of Python 3.12
FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Upgrade pip and install the dependencies from requirements.txt
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt \
    && pip install newrelic

# Copy the application source code to the container
COPY ./app /app/app

# Set environment variables
ENV RDS_USERNAME=postgres \
    RDS_PASSWORD=entrega-4 \
    RDS_HOSTNAME=database-entrega-4.crkgma2w6ksq.us-east-2.rds.amazonaws.com \
    RDS_PORT=5432 \
    RDS_DB_NAME=postgres \
    SECRET_TOKEN=bGFtYmRhX3NxdWFk \
    NEW_RELIC_APP_NAME="Entrega-4-Fargate" \
    NEW_RELIC_LOG=stdout \
    NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true \
    NEW_RELIC_LICENSE_KEY=ceb74435514c94fd53399597ee9eb6f6FFFFNRAL \
    NEW_RELIC_LOG_LEVEL=info

# Create a new user 'appuser' with user ID 5678, disable password, and change ownership of /app to appuser
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

# Switch to the new user 'appuser'
USER appuser

# Expose port 3000 for the application
EXPOSE 3000

ENTRYPOINT [ "newrelic-admin", "run-program" ]

# Command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]