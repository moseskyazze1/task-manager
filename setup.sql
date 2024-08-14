CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128),
    summary VARCHAR(256),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

INSERT INTO task (
    name,
    summary,
    description
) VALUES (
    "wash car",
    "the car needs to be washed",
    "make sure the car gets waxed after it is washed"
), (
    "walk the dog",
    "Rocky needs their exercise",
    "make sure to do at least 2 laps around the park"
), (
    "buy groceries",
    "go to the supermarket and buy groceries",
    "We need: Eggs, Milk, Cereal, and Coffee"
);
