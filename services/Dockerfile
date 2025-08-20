FROM python:3.11-slim

WORKDIR /app

# העתקת קבצי requirements
COPY requirements.txt .
# התקנת התלויות
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל הקבצים של הפרויקט
COPY . .

# פתיחת הפורט 8000
EXPOSE 8000

# פקודת הרצה
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
