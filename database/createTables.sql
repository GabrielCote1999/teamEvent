--User table
--we will add the fk adress after the creation of the adress table

CREATE TABLE IF NOT EXISTS user(
    userId integer PRIMARY KEY,
    firstName text NOT NULL,
    lastName text NOT NULL,
    userPassword text NOT NULL,
    email text NOT NULL,
    creationDate date NOT NULL,
    dateOfBirth date NOT NULL
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
--We will add the adress FK and category FK after their creation
CREATE TABLE IF NOT EXISTS events(
    eventId integer PRIMARY KEY,
    eventName text NOT NULL,
    startDate date NOT NULL,
    endDate date NOT NULL,
    creationDate date NOT NULL,
    eventStatus text NOT NULL,
    vote integer
);

--We will add the categoryType FK after the table creation
CREATE TABLE IF NOT EXISTS category(
    categoryId integer PRIMARY KEY,
    categoryName text NOT NULL,
    categoryType text
);

CREATE TABLE IF NOT EXISTS categoryTypes(
    categoryTypeId int NOT NULL,
    categoryType text NOT NULL
);