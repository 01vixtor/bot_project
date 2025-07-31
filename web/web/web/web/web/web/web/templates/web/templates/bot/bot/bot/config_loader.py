import sqlite3

def get_config():
    conn = sqlite3.connect('web/site.db')
    cursor = conn.cursor()
    cursor.execute("SELECT message_text, interval_minutes, valid_time_minutes, random_min, random_max FROM bot_config LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "message_text": row[0],
            "interval": row[1],
            "valid_time": row[2],
            "min": row[3],
            "max": row[4],
        }
    return None
