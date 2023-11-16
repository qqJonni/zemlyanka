import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect('new_db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PTIMARY KEY, name TEXT, phone_number TEXT, address TEXT)")
    db.commit()


async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?)", (user_id, '', '', ''))


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile SET name = '{}', phone_number = '{}', address = '{}' WHERE user_id == '{}'".format(
            data['name'], data['phone_number'], data['address'], user_id))
        db.commit()
