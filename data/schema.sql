CREATE TABLE exercises (
    id INTEGER PRIMARY KEY,
    muscle TEXT NOT NULL,
    exercise TEXT NOT NULL,
    multiplier REAL NOT NULL
);

INSERT INTO exercises VALUES
    (NULL, 'chest', 'bench press', 1),
    (NULL, 'glutes', 'hip thrust', 1),
    (NULL, 'lats', 'pull ups', 1),
    (NULL, 'biceps', 'pull ups', 0.7),
    (NULL, 'back', 'pull ups', 0.7),
    (NULL, 'lats', 'chin ups', 1),
    (NULL, 'back', 'chin ups', 1),
    (NULL, 'biceps', 'chin ups', 1),
    (NULL, 'hamstrings', 'hip thrust', 1),
    (NULL, 'triceps', 'bench press', 0.5),
    (NULL, 'back', 'bend over row', 1),
    (NULL, 'biceps', 'bend over row', 0.5),
    (NULL, 'deltoids', 'military press', 1),
    (NULL, 'triceps', 'military press', 0.3),
    (NULL, 'quads', 'squat', 1),
    (NULL, 'quads', 'zercher squat', 1),
    (NULL, 'calves', 'calf raise', 1),
    (NULL, 'calves', 'seated calf raise', 1),
    (NULL, 'hamstrings', 'squat', 0.3),
    (NULL, 'hamstrings', 'good mornings', 1),
    (NULL, 'triceps', 'french press', 1),
    (NULL, 'biceps', 'biceps curls', 1);