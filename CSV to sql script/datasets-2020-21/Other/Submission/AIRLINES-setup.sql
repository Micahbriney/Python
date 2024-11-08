DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS airports;
DROP TABLE IF EXISTS airlines;


-- airlines table
--           Id   : unique identifier of the airline
--        Airline : full name of the airline
--   Abbreviation : abbreviated name of the airline
--        Country : country of the airline
-- ex.
-- Id	Airline	        Abbreviation	Country
-- 1	United Airlines	UAL	            USA

CREATE TABLE airlines(
    Id INTEGER,
    Airline VARCHAR(70),
    Abbreviation VARCHAR(30), 
    Country VARCHAR(30),
    PRIMARY KEY (Id),
    UNIQUE (Abbreviation)
);

-- INSERT INTO airlines(Id, Airline, Abbreviation, Country)
-- VALUES (101, 'Southwestern', 'Southwest', 'USA')

-- airports table
--         City  : location of the airport
--   AirportCode : unique three-letter airport code
--   AirportName : name of the airport
--       Country : country of the airport
-- CountryAbbrev : abbreviation of the country
-- ex. 
-- City	    AirportCode	AirportName	  Country	    CountryAbbrev  
-- Aberdeen	APG	        Phillips AAF  United States	US 

CREATE TABLE airports(
    City VARCHAR(30),
    AirportCode CHAR(3),
    AirportName VARCHAR(60),
    Country VARCHAR(60),
    CountryAbbrev VARCHAR(10),
    PRIMARY KEY (AirportCode)
);


-- flights table

--       Airline : airline that manages the flight
--      FlightNo : flight number (unique for each airline, may repeat
--                 for different airlines)
-- SourceAirport : Code for the airport from which the flight originates
--   DestAirport : Code for the airport at which the flight terminates
-- ex: 
-- Airline	 FlightNo	 SourceAirport	 DestAirport
-- 1	     28          APG	         ABR

CREATE TABLE flights(
    Airline INTEGER,
    FlightNo INTEGER,
    SourceAirport CHAR(3),
    DestAirport CHAR(3) NOT NULL,
    PRIMARY KEY (Airline, FlightNo),
    FOREIGN KEY flights_Source_FK (SourceAirport) REFERENCES airports (AirportCode),
    FOREIGN KEY flights_Dest_FK (DestAirport) REFERENCES airports (AirportCode),
    FOREIGN KEY flights_Airline_FK (AirLine) REFERENCES airlines (Id)
);

	INSERT INTO airlines (Id,Airline,Abbreviation,Country)
VALUES
	(1,'United Airlines','UAL','USA'),
	(2,'US Airways','USAir','USA'),
	(3,'Delta Airlines','Delta','USA'),
	(4,'Southwest Airlines','Southwest','USA'),
	(5,'American Airlines','American','USA'),
	(6,'Northwest Airlines','Northwest','USA'),
	(7,'Continental Airlines','Continental','USA'),
	(8,'JetBlue Airways','JetBlue','USA'),
	(9,'Frontier Airlines','Frontier','USA'),
	(10,'AirTran Airways','AirTran','USA'),
	(11,'Allegiant Air','Allegiant','USA'),
	(12,'Virgin America','Virgin','USA');

	INSERT INTO airports (City,AirportCode,AirportName,Country,CountryAbbrev  )
VALUES
	('Aberdeen','APG','Phillips AAF','United States','US'),
	('Aberdeen','ABR','Municipal','United States','US'),
	('Abilene','DYS','Dyess AFB','United States','US'),
	('Abilene','ABI','Municipal','United States','US'),
	('Abingdon','VJI','Virginia Highlands','United States','US'),
	('Ada','ADT','Ada','United States','US'),
	('Adak Island','ADK','Adak Island Ns','United States','US'),
	('Adrian','ADG','Lenawee County','United States','US'),
	('Afton','AFO','Municipal','United States','US'),
	('Aiken','AIK','Municipal','United States','US'),
	('Ainsworth','ANW','Ainsworth','United States','US'),
	('Akhiok','AKK','Akhiok SPB','United States','US'),
	('Akiachak','KKI','Spb','United States','US'),
	('Akiak','AKI','Akiak','United States','US'),
	('Akron CO','AKO','Colorado Plains Regional Airport','United States','US'),
	('Akron/Canton OH','CAK','Akron/canton Regional','United States','US'),
	('Akron/Canton','AKC','Fulton International','United States','US');

	INSERT INTO flights (Airline, FlightNo, SourceAirport, DestAirport)
VALUES
	(1,28,'APG','ABR'),
	(1,29,'AIK','ADT'),
	(1,44,'AKO','AKI'),
	(1,45,'CAK','APG'),
	(1,54,'AFO','AKO'),
	(3,2,'AIK','ADT'),
	(3,3,'DYS','ABI'),
	(3,26,'AKK','VJI'),
	(9,1260,'AKO','AKC'),
	(9,1261,'APG','ABR'),
	(9,1286,'ABR','APG'),
	(9,1287,'DYS','ANW'),
	(10,6,'KKI','AKC'),
	(10,7,'VJI','APG'),
	(10,54,'ADT','APG'),
	(6,4,'AIK','AKO'),
	(6,5,'CAK','APG'),
	(6,28,'AKO','ABI'),
	(6,29,'ABR','ABI');