# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port used by Streamlit
EXPOSE 8080

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.enableCORS=false"]
