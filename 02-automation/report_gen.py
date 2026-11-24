import sqlite3
from datetime import datetime

# 1. Connect to the existing database
conn = sqlite3.connect("watch_history.db")
cursor = conn.cursor()

# 2. Query 1: Get total number of checks logged
cursor.execute("SELECT COUNT(*) FROM logs")
total_checks = cursor.fetchone()[0]

# 3. Query 2: Get total number of times a site actually CHANGED
cursor.execute("SELECT COUNT(*) FROM logs WHERE status = 'CHANGED'")
total_changes = cursor.fetchone()[0]

# 4. Query 3: Get the last 5 activities for the detailed report
cursor.execute("""
    SELECT url, status, checked_at 
    FROM logs 
    ORDER BY id DESC 
    LIMIT 5
""")
recent_logs = cursor.fetchall()

# 5. Format and print the report
print("=" * 50)
print("📊 WEEKLY WATCHER ACTIVITY REPORT")
print("=" * 50)
print(f"Total Checks Logged: {total_checks}")
print(f"Total Changes Detected: {total_changes}")
print("-" * 50)
print("RECENT ACTIVITY (Last 5):")

for log in recent_logs:
    url = log[0]
    status = log[1]
    # Format the timestamp to be more readable
    try:
        dt = datetime.fromisoformat(log[2])
        time_str = dt.strftime("%b %d, %Y - %I:%M %p")
    except:
        time_str = log[2]
    
    print(f"• [{status}] {url}")
    print(f"  Time: {time_str}")

print("=" * 50)

# 6. Close the connection
conn.close()