#connect db
import sqlite3

#where is DB? 
dbfile = "./db/bujo.db"

#connect SQLITE db
def create_db():
	try: 
		con = sqlite3.connect(dbfile)
		cur = con.cursor()
		cur.execute('''CREATE TABLE IF NOT EXISTS tasks (task_id INTEGER PRIMARY KEY, task TEXT)''')
		con.commit()
	except Exception as e:
		print(f"Error: {e}")
	finally:	
		con.close()

# #return all users
# def all_users():
# 	try: 
# 		con = sqlite3.connect("./db/bujo.db")
# 		cur = con.cursor()

# 		res = cur.execute("SELECT * FROM users")
# 		return res.fetchall()
# 	except Exception as e: 
# 		print(f"Error: {e}")
# 	finally: 
# 		con.close()

# def add_user(username, email, password): 
# 	try: 
# 		con = sqlite3.connect("../db/bujo.db")
# 		cur = con.cursor()

# 		cur.execute("INSERT INTO users (username, email, password) VALUES (?,?,?)",(username,email,password))
# 		con.commit()
# 		return 
# 	except Exception as e:
# 		print(f"Error:{e}")
# 	finally: 
# 		con.close()

def add_task(task_id, task, done): 
	try: 
		con = sqlite3.connect(dbfile)
		cur = con.cursor()

		cur.execute("INSERT INTO tasks (task_id, task, done) VALUES (?,?,?)",(task_id,task,done))
		con.commit()
		return 
	except Exception as e:
		print(f"Error:{e}")
	finally: 
		con.close()

if __name__ == "__main__": 

	add_user('walter','thumb_life','coolcat')
	print(all_users())