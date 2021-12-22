
--categoryType table
CREATE TABLE IF NOT EXISTS categoryTypes(
    categoryTypeId int NOT NULL,
    categoryType text NOT NULL
);
--Category table
CREATE TABLE IF NOT EXISTS category(
    categoryId integer PRIMARY KEY,
    categoryName text NOT NULL,
    categoryType text
    FOREIGN KEY (categoryTypeId) REFERENCES categoryType (categoryTypeId)
);

CREATE TABLE IF NOT EXISTS adress(
    adressId integer PRIMARY KEY,
    streetNumber integer NOT NULL,
    appNumber text,
    roadName text NOT NULL,
    zipCode text NOT NULL,
    country text NOT NULL,
    province text NOT NULL
);
--Events table
CREATE TABLE IF NOT EXISTS events(
    eventId integer PRIMARY KEY,
    eventName text NOT NULL,
    startDate date NOT NULL,
    endDate date NOT NULL,
    creationDate date NOT NULL,
    eventStatus text NOT NULL,
    vote integer
    FOREIGN KEY (adressId) REFERENCES adress (adressId)
    FOREIGN KEY (categoryId) REFERENCES category (categoryId)
);
--User table
CREATE TABLE IF NOT EXISTS user(
    userId integer PRIMARY KEY,
    firstName text NOT NULL,
    lastName text NOT NULL,
    userPassword text NOT NULL,
    email text NOT NULL,
    creationDate date NOT NULL,
    dateOfBirth date NOT NULL,
    FOREIGN KEY (adressId) REFERENCES adress (adressId)
);


