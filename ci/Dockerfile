FROM python:3.12


RUN apt-get update && apt-get install -y \
    curl unzip gnupg ca-certificates fonts-liberation \
    && curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


ENV CHROME_BIN=/usr/bin/google-chrome


WORKDIR /tests
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .


CMD ["pytest", "tests", "--alluredir=allure-results"]
