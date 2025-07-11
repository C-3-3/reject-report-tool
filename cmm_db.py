import sqlite3

def init_db():
    conn = sqlite3.connect("data/cmm_refs.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS cmm_refs (
            part_number TEXT,
            damage_type TEXT,
            cmm_reference TEXT,
            action_summary TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_cmm_reference(part_number, damage_type):
    conn = sqlite3.connect("data/cmm_refs.db")
    c = conn.cursor()
    c.execute("SELECT cmm_reference FROM cmm_refs WHERE part_number=? AND damage_type=?",
              (part_number, damage_type))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def add_cmm_entry(part_number, damage_type):
    cmm_ref = input("Enter CMM reference (Task/Table/Revision/etc.): ")
    action_summary = input("Enter action summary (e.g., Discard if beyond limits): ")
    conn = sqlite3.connect("data/cmm_refs.db")
    c = conn.cursor()
    c.execute("INSERT INTO cmm_refs VALUES (?, ?, ?, ?)",
              (part_number, damage_type, cmm_ref, action_summary))
    conn.commit()
    conn.close()
    print("✅ CMM reference added.")
