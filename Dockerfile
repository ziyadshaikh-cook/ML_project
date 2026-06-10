FROM python:3.11-slim

WORKDIR /app

# Copy EVERYTHING first (fixes the -e . bug: setup.py must exist before pip install)
COPY . .

# Install all dependencies (including the local package via -e .)
RUN pip install --no-cache-dir -r requirements.txt

# Tell EB's Nginx reverse proxy to forward port 80 → 5000
EXPOSE 5000

CMD ["python", "app.py"]