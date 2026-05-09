import time
import sqlite3
from datetime import datetime

print("\n🚀 BlackVision Aenya OS v8.0 - DEMO MODE\n")

time.sleep(1)
print("🔐 Initializing Sandbox Environment...")
time.sleep(1)

print("🧠 Loading Hybrid Intelligence Core...")
time.sleep(1)

print("🌐 Simulating Chrome Fusion...")
time.sleep(1)

print("📡 Agent Hive Online")
time.sleep(1)

# Criar memória simulada
conn = sqlite3.connect("aenya_memory.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs(
    time TEXT, 
    event TEXT
)
""")

def log(event):
    now = datetime.now().strftime("%H:%M:%S")
    cursor.execute("INSERT INTO logs VALUES (?,?)", (now, event))
    conn.commit()
    print(f"[{now}] {event}")

print("\n🤖 Spawning Soldier Agent...\n")
time.sleep(2)

log("Agent created")
time.sleep(1)
log("Opening Gmail (simulated)")
time.sleep(1)
log("Reading command email")
time.sleep(1)
log("Generating automation script")
time.sleep(1)
log("Executing web task (simulated)")
time.sleep(1)
log("Screenshot captured")
time.sleep(1)
log("Knowledge stored in memory")

print("\n✅ Demo completed.")
print("System ready for Full Fusion mode.\n")

conn.close()
