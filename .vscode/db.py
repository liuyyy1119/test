import sqlite3

def init_db():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    # 创建用户表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # 插入一个默认账号（防止没数据）
    cursor.execute("SELECT * FROM users WHERE username=?", ("admin",))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "123456"))

    conn.commit()
    conn.close()