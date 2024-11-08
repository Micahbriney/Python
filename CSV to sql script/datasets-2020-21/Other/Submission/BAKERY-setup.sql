DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS receipts;
DROP TABLE IF EXISTS goods;
DROP TABLE IF EXISTS customers;


 -- customers

       -- CId: unique identifier of the customer
  -- LastName: last name of the customer
 -- FirstName: first name of the customer
	-- EX: 
	-- (1,'LOGAN','JULIET')
-- **************************************************************************

CREATE TABLE customers (
	CId INTEGER,
	LastName VARCHAR(20),
	FirstName VARCHAR(20),
	PRIMARY KEY(CId)
);


 -- goods

     -- GId: unique identifier of the baked good
  -- Flavor: flavor/type of the good (e.g., "chocolate", "lemon")
    -- Food: category of the good (e.g., "cake", "tart")
   -- Price: price (in dollars) 
	-- ex:
	-- ('20-BC-C-10','Chocolate','Cake','8.95'),
-- **************************************************************************

CREATE TABLE goods (
	GId VARCHAR(30),
	Flavor VARCHAR(20),
	Food VARCHAR(15),
	Price FLOAT,
	PRIMARY KEY(GId),
	UNIQUE(Flavor, Food)
);


-- reciepts

      -- RNumber : unique identifier of the receiipt
     -- SaleDate : date of the purchase. 
     -- Customer : id of the customer (see customers.Id)
	-- Ex:
	-- 	(18129,'28-Oct-2007',15),
-- **************************************************************************

CREATE TABLE receipts (
	RNumber INTEGER,
	SaleDate DATE,
	Customer INTEGER,
	PRIMARY KEY(RNumber),
	FOREIGN KEY CustomerId_reciepts_FK (Customer) REFERENCES customers(CId)
);


-- items

    -- Receipt : receipt number 
    -- Ordinal : position of the purchased item on the
              -- receipts. (i.e., first purchased item,
              -- second purchased item, etc...)
    -- Item    : identifier of the item purchased (see goods.Id)
    -- Ex:
	-- 	(51991,1,'90-APIE-10'),
-- **************************************************************************

CREATE TABLE items (
	Receipt INTEGER,
	Ordinal INTEGER,
	Item VARCHAR(30) NOT NULL,
	PRIMARY KEY(Receipt, Ordinal),
	FOREIGN KEY Receipt_items_FK (Receipt) REFERENCES receipts(RNumber),
	FOREIGN KEY Item_items_FK (Item) REFERENCES goods(GId)
);