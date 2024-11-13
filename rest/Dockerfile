FROM mcr.microsoft.com/azure-functions/python:4-python3.11

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true \
    GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git


# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    libssl-dev git libc-ares2 \
    && apt-get clean

# Set the working directory
WORKDIR /home/site/wwwroot

ADD .deps/ .

COPY requirements.txt .

RUN pip install --upgrade pip && pip install grpcio && pip install --no-cache-dir -r requirements.txt --user

ENV FUNCTIONS_WORKER_RUNTIME python

ENV PYTHONPATH="${PYTHONPATH}:/root/.local/lib/python3.11/site-packages"

EXPOSE 80
