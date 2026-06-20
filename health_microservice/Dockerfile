# go pull a pre-built image from Docker Hub that already has Python 3.11 installed inside it
# Docker reads FROM python:3.11-slim, sees it doesn't have that image locally, and downloads it from Docker Hub automatically.
FROM python:3.11-slim 

# making the working directory (/health_microservice will be the ROOT directory)
WORKDIR /health_microservice

# Install dependencies first (better layer caching)
# copy requirements.txt to the working directory (which is /health_microservice) and then install the dependencies using pip. This way, if you change your application code but not your dependencies, Docker can cache the layer with the installed dependencies and speed up subsequent builds.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the content from source <local system files> to destination <docker_app directory>
COPY . .

# Since you already set WORKDIR /health_microservice, you don't need to repeat the full path. This works fine, but it's inconsistent with your COPY requirements.txt . line above it (which correctly uses the shorthand .). For consistency:

EXPOSE 8000

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
