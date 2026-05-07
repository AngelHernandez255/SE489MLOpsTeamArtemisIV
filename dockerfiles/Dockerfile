
# Multi-stage build for Artemis Movie Recomender

# Stage 1: Builder
FROM python:3.13-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.13-slim

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Set environment variables
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Copy project code
COPY . .

# Install the package
RUN pip install --no-cache-dir -e .

EXPOSE 8000

ENTRYPOINT ["python", "-m", "SE489MLOpsTeamArtemisIV.train_model"]
