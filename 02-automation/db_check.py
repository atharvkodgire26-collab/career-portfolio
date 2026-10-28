import sqlite3

# 1. Connect to the database
conn = sqlite3.connect("watch_history.db")
cursor = conn.cursor()

# 2. Get the last 5 logs, ordered by newest first
cursor.execute("SELECT url, status, checked_at FROM logs ORDER BY id DESC LIMIT 5")
logs = cursor.fetchall()

# 3. Print them nicely
print("Recent Watch Logs:")
print("-" * 60)
for log in logs:
    print(f"URL:    {log[0]}")
    print(f"Status: {log[1]}")
    print(f"Time:   {log[2]}")
    print("-" * 60)

conn.close()