# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /Controller

# Copy all project files into the container
COPY . /Controller

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port FastAPI will run on
EXPOSE 8000

# Run the app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
