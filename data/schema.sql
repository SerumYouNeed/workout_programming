CREATE TABLE exercises (
    id INTEGER PRIMARY KEY,
    muscle TEXT NOT NULL,
    exercise TEXT NOT NULL,
    multiplier REAL NOT NULL
);

INSERT INTO exercises VALUES
    (NULL, 'chest', 'bench press', 1),
    (NULL, 'biceps', 'bench press', 0.5),
    (NULL, 'back', 'bend over row', 1),
    (NULL, 'biceps', 'bend over row', 0.5),
    (NULL, 'deltoids', 'military press', 1),
    (NULL, 'triceps', 'military press', 0.3),
    (NULL, 'quads', 'squat', 1),
    (NULL, 'hamstring', 'squat', 0.3),
    (NULL, 'hamstring', 'good mornings', 1),
    (NULL, 'triceps', 'french press', 1),
    (NULL, 'biceps', 'biceps curls', 1);