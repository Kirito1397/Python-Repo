# Specify the base image
FROM alpine:3.5

# Install Python along with any required dependencies
RUN apk add --update py2-pip

# Install all Python requirements for our app to run
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy the files you have created earlier into our image by using COPY command.
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# Specify the port number which needs to be exposed. 
# Since our flask app is running on 5000 that's what we'll expose.
EXPOSE 5000

# Provide command for running the application - python ./app.py
CMD ["python", "/usr/src/app/app.py"]