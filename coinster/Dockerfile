#Use the official Python image as the base image
FROM ubuntu


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Python and other dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN mkdir /usr/bin/crontab
#RUN chmod +rxw /usr/bin/crontab

# Copy the source code of the Django application
COPY . .

# Expose port 8000 for the web server
EXPOSE 8000

# Run the Django application using gunicorn
CMD ["gunicorn", "coinster.wsgi", "--bind", "0.0.0.0:8000"]‏

