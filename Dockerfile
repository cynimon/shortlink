FROM python:3.10-alpine

# Set the working directory to /opt/app
WORKDIR /opt/app
ENV PYTHONPATH="/opt/app/shortlink"
# Copy the requirements file into the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

EXPOSE 8000

# Start the application using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]