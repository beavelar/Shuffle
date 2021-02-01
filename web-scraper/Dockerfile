# Requirements
FROM python:3.8.3

# Working directory
WORKDIR /web-scraper

# Copy dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

EXPOSE 3010

# Start app
CMD ["python", "-u", "./server.py"]