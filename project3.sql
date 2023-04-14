DROP TABLE IF EXISTS attend;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS trips;

CREATE TABLE trips (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(50),
    start_date DATE,
    length INT(1),
    cost INT(4),
    location VARCHAR(50),
    level VARCHAR(50),
    leader VARCHAR(50),
    description TEXT
) ENGINE = innodb;

CREATE TABLE members (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(50),
    dob DATE,
    email VARCHAR(50),
    address VARCHAR(50),
    phone VARCHAR(20)
) ENGINE = innodb;

CREATE TABLE attend (
    member_id INT NOT NULL,
    trip_id INT NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (trip_id) REFERENCES trips(id)
) ENGINE = innodb;

INSERT INTO trips (id,name,start_date,length,cost,location,level,leader,description) VALUES
(1,'Operation: French Clover','2023-01-04',7,5000,'White House (Allegedly)','Intense','REDACTED','Haha just a silly trip to the US capital with a lot of digging supplies and a tunnel bore nothing suspicious'),
(2,'Randy\'s Redwood Escapade','2023-02-18',5,200,'Redwood National Park CA','Easy','Randy Murphy','5 days of exploring the natural redwoods in California!'),
(3,'Yellowstone Old Faithful Eruption Dive','2023-03-21',1,80,'Yellowstone National Park WY','Certain Death','Neo-Messiah','We will be diving into Old Faithful as it is erupting.'),
(4,'Great Smokey Mountains Adventure','2023-04-15',3,2200,'Great Smokey Mountains National Park TN','Intermediate','Fredd','This 4-day adventure brings you face to face with the many facets and hidden wonders of the Great Smoky Mountains.'),
(5,'Grand Teton Kayaking','2023-06-06',9,1600,'Grand Teton National Park WY','Easy','Lilly Normalname','The Grand Tetons are renowned for breathtaking beauty. This incredible 2-day trip takes us through some of the best sights.');

INSERT INTO members (id,name,dob,email,address,phone) VALUES 
(1,'Blunder Whoopsmore','1998-07-19','bloopsmore@hotmail.com','4716 Hogging St Billings MT','406-318-7926'),
(2,'Grimble Simpleton','2002-03-14','arceus519@gmail.com','1150 S Clarizz Bloomington IN','317-317-4892'),
(3,'Andrew Turnner','1996-12-08','bessattackingme28@gmail.com','925 Strand Rd Houstan TX','558-439-0021'),
(4,'Danial Latinovik','2001-04-22','dlatinov@gmail.com','6203 E Verdant Dr Lafayette IN','317-430-1345'),
(5,'Haley Millings','2001-08-13','iloverawmeat@gmail.com','7307 Indiana Ave Bloomington IN','317-998-0305'),
(6,'Bethanial Borken','1979-07-13','planteater@gmail.com','448 Stunt Ave Gary IN','202-657-7007');

INSERT INTO attend VALUES 
(1,2),
(1,5),
(2,1),
(2,3),
(3,5),
(4,2),
(5,4),
(5,5),
(6,2);
