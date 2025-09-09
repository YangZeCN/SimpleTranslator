FROM python:3.13-slim


RUN apt-get update && apt-get install -y curl gnupg sqlite3 && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs vim telnet && \
    apt-get clean

RUN python3 --version && npm --version && sqlite3 --version

WORKDIR /app

COPY start_web.sh .
RUN chmod +x start_web.sh
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY vite-project/package*.json .
RUN npm install

COPY backend/ backend
COPY vite-project/ vite-project

EXPOSE 5000 5173

CMD ["./start_web.sh"]
