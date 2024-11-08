 -- customers

       -- CId: unique identifier of the customer
  -- LastName: last name of the customer
 -- FirstName: first name of the customer
-- **************************************************************************

	INSERT INTO customers (CId, LastName, FirstName)
VALUES
	(1,'LOGAN','JULIET'),
	(2,'ARZT','TERRELL'),
	(3,'ESPOSITA','TRAVIS'),
	(4,'ENGLEY','SIXTA'),
	(5,'DUNLOW','OSVALDO'),
	(6,'SLINGLAND','JOSETTE'),
	(7,'TOUSSAND','SHARRON'),
	(8,'HELING','RUPERT'),
	(9,'HAFFERKAMP','CUC'),
	(10,'DUKELOW','CORETTA'),
	(11,'STADICK','MIGDALIA'),
	(12,'MCMAHAN','MELLIE'),
	(13,'ARNN','KIP'),
	(14,'S\'OPKO','RAYFORD'),
	(15,'CALLENDAR','DAVID'),
	(16,'CRUZEN','ARIANE'),
	(17,'MESDAQ','CHARLENE'),
	(18,'DOMKOWSKI','ALMETA'),
	(19,'STENZ','NATACHA'),
	(20,'ZEME','STEPHEN');


 -- goods

     -- GId: unique identifier of the baked good
  -- Flavor: flavor/type of the good (e.g., "chocolate", "lemon")
    -- Food: category of the good (e.g., "cake", "tart")
   -- Price: price (in dollars) 
-- **************************************************************************

	INSERT INTO goods (GId,Flavor,Food,Price)
VALUES
	('20-BC-C-10','Chocolate','Cake','8.95'),
	('20-BC-L-10','Lemon','Cake','8.95'),
	('20-CA-7.5','Casino','Cake','15.95'),
	('24-8x10','Opera','Cake','15.95'),
	('25-STR-9','Strawberry','Cake','11.95'),
	('26-8x10','Truffle','Cake','15.95'),
	('45-CH','Chocolate','Eclair','3.25'),
	('45-CO','Coffee','Eclair','3.5'),
	('45-VA','Vanilla','Eclair','3.25'),
	('46-11','Napoleon','Cake','13.49'),
	('90-ALM-I','Almond','Tart','3.75'),
	('90-APIE-10','Apple','Pie','5.25'),
	('90-APP-11','Apple','Tart','3.25'),
	('90-APR-PF','Apricot','Tart','3.25'),
	('90-BER-11','Berry','Tart','3.25'),
	('90-BLK-PF','Blackberry','Tart','3.25'),
	('90-BLU-11','Blueberry','Tart','3.25'),
	('90-CH-PF','Chocolate','Tart','3.75'),
	('90-CHR-11','Cherry','Tart','3.25'),
	('90-LEM-11','Lemon','Tart','3.25'),
	('90-PEC-11','Pecan','Tart','3.75'),
	('70-GA','Ganache','Cookie','1.15'),
	('70-GON','Gongolais','Cookie','1.15'),
	('70-R','Raspberry','Cookie','1.09'),
	('70-LEM','Lemon','Cookie','0.79'),
	('70-M-CH-DZ','Chocolate','Meringue','1.25'),
	('70-M-VA-SM-DZ','Vanilla','Meringue','1.15'),
	('70-MAR','Marzipan','Cookie','1.25'),
	('70-TU','Tuile','Cookie','1.25'),
	('70-W','Walnut','Cookie','0.79'),
	('50-ALM','Almond','Croissant','1.45'),
	('50-APP','Apple','Croissant','1.45'),
	('50-APR','Apricot','Croissant','1.45'),
	('50-CHS','Cheese','Croissant','1.75'),
	('50-CH','Chocolate','Croissant','1.75'),
	('51-APR','Apricot','Danish','1.15'),
	('51-APP','Apple','Danish','1.15'),
	('51-ATW','Almond','Twist','1.15'),
	('51-BC','Almond','Bear Claw','1.95'),
	('51-BLU','Blueberry','Danish','1.15');


-- reciepts

      -- RNumber : unique identifier of the receiipt
     -- SaleDate : date of the purchase. 
     -- Customer : id of the customer (see customers.Id)
-- **************************************************************************

	INSERT INTO receipts (RNumber, SaleDate, Customer)
VALUES
	(18129,STR_TO_DATE("28-Oct-2007", "%d-%b-%Y"),15),
	(51991,STR_TO_DATE("17-Oct-2007", "%d-%b-%Y"),14),
	(83085,STR_TO_DATE("12-Oct-2007", "%d-%b-%Y"),7),
	(70723,STR_TO_DATE("28-Oct-2007", "%d-%b-%Y"),20),
	(13355,STR_TO_DATE("12-Oct-2007", "%d-%b-%Y"),7),
	(52761,STR_TO_DATE("27-Oct-2007", "%d-%b-%Y"),8),
	(99002,STR_TO_DATE("13-Oct-2007", "%d-%b-%Y"),20),
	(58770,STR_TO_DATE("22-Oct-2007", "%d-%b-%Y"),18),
	(84665,STR_TO_DATE("10-Oct-2007", "%d-%b-%Y"),6);


-- items

    -- Receipt : receipt number 
    -- Ordinal : position of the purchased item on the
              -- receipts. (i.e., first purchased item,
              -- second purchased item, etc...)
    -- Item    : identifier of the item purchased (see goods.Id)
-- **************************************************************************

	INSERT INTO items (Receipt, Ordinal, Item)
VALUES
	(18129,1,'70-TU'),
	(51991,1,'90-APIE-10'),
	(51991,2,'90-CH-PF'),
	(51991,3,'90-APP-11'),
	(51991,4,'26-8x10'),
	(83085,1,'25-STR-9'),
	(83085,2,'24-8x10'),
	(83085,3,'90-APR-PF'),
	(83085,4,'51-ATW'),
	(83085,5,'26-8x10'),
	(70723,1,'45-CO'),
	(13355,1,'24-8x10'),
	(13355,2,'70-LEM'),
	(13355,3,'46-11'),
	(52761,1,'90-ALM-I'),
	(52761,2,'26-8x10'),
	(52761,3,'50-CHS'),
	(52761,4,'90-BLK-PF'),
	(52761,5,'90-ALM-I'),
	(99002,1,'50-CHS'),
	(99002,2,'45-VA'),
	(58770,1,'50-CHS'),
	(58770,2,'46-11'),
	(58770,3,'45-CH'),
	(58770,4,'20-CA-7.5'),
	(84665,1,'90-BER-11');

