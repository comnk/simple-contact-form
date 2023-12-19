CREATE TABLE form_data (
  id INTEGER,
  user_name TEXT NOT NULL,
  email TEXT NOT NULL,
  txt TEXT NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT),
  UNIQUE (user_name, email)
);