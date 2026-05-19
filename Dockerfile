# ── Base image ──────────────────────────────────────────────────────
FROM python:3.11-slim

# ── Set working directory ───────────────────────────────────────────
WORKDIR /app

# ── Copy requirements first (better layer caching) ──────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Copy the rest of the application ────────────────────────────────
COPY . .

# ── Train the model inside the container ────────────────────────────
RUN python train_model.py

# ── Expose the FastAPI port ─────────────────────────────────────────
EXPOSE 8000

# ── Start the application ──────────────────────────────────────────
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
