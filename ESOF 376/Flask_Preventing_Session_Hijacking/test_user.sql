-- SQLite-Compatible SQL Dump

-- Table structure for table `users`
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user TEXT NOT NULL UNIQUE, -- Ensures usernames are unique
  password TEXT NOT NULL
);

-- Insert initial data only if it does not already exist
INSERT INTO users (user, password) VALUES('ahmad', 'a53a33601b8dd9d06ae9e50f1f30fbe957aba866'),
('aslam', 'c848d7cfaea8f10d19fb007d90e7711754080c79');