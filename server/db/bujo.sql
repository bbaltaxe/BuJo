-- CREATE TABLE users 
-- (
-- 	id INTEGER PRIMARY KEY, 
-- 	username TEXT NOT NULL UNIQUE, 
-- 	email TEXT NOT NULL UNIQUE, 
-- 	password TEXT NOT NULL
-- );

-- CREATE TABLE tasks
-- (
-- 	id INTEGER PRIMARY KEY, 
-- 	user_id INTEGER REFERENCES users(id), --foreign key
-- 	status TEXT, 
-- 	content TEXT
-- );