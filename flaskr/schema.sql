DROP TABLE IF EXISTS user_play;

CREATE TABLE user_play (
  username TEXT UNIQUE NOT NULL,
  round_number INTEGER NOT NULL,
  millis INTEGER NOT NULL,
  score REAL NOT NULL
);
