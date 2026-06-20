# Use a lightweight Python base image
FROM python:3.11-slim

# Set up the working directory
WORKDIR /app

# Copy the project configuration and source code
COPY pyproject.toml .
COPY src/ ./src/

# Install the package directly from the pyproject.toml (no requirements.txt needed)
RUN pip install --no-cache-dir .

# Run the project with an unprivileged user for extra sandbox security
RUN useradd -m sandboxuser
USER sandboxuser

# Command to initiate the orchestrator and arm the canaries
CMD ["python", "src/main.py"]
