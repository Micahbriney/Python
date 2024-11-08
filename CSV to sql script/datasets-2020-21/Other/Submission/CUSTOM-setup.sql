DROP TABLE IF EXISTS inventory_parts;
DROP TABLE IF EXISTS inventory_sets;
DROP TABLE IF EXISTS inventories;
DROP TABLE IF EXISTS sets;
DROP TABLE IF EXISTS parts;
DROP TABLE IF EXISTS themes;
DROP TABLE IF EXISTS part_categories;
DROP TABLE IF EXISTS colors;

-- ------------------------------------------------------
-- part_categories
-- contains information on the part category (what type of part it is)
-- and a unique ID for that part category
-- ------------------------------------------------------
-- ------------------------------------------------------

CREATE TABLE part_categories (
	id INTEGER,
	name VARCHAR(50),
	PRIMARY KEY(id)
);

-- ---------------------------------------------------------
-- ---------------------------------------------------------
-- themes
-- includes information on lego themes. Each theme is given 
-- a unique ID number, a name, and 
-- (if it's part of a bigger theme) which theme it's part of.
-- ---------------------------------------------------------
-- ---------------------------------------------------------

CREATE TABLE themes (
	id INTEGER,
	name VARCHAR(35),
	parent_id INTEGER DEFAULT NULL,
	PRIMARY KEY(id)
);

-- --------------------------------------------------------
-- --------------------------------------------------------
-- colors
-- Contains information on LEGO colors, including a unique ID 
-- for each color, its name, and approximate RGB value, and 
-- whether it's transparent
-- --------------------------------------------------------
-- --------------------------------------------------------


CREATE TABLE colors (
	id INTEGER,
	name VARCHAR(30),
	rgb VARCHAR(10),
	is_trans CHAR(1),
	PRIMARY KEY(id)
);

-- ------------------------------------------------------------
-- parts
-- includes information on lego parts, including a unique ID 
-- number, the name of the part, and what part category it's from
-- ------------------------------------------------------------
-- ------------------------------------------------------------

CREATE TABLE parts (
	part_num VARCHAR(20),
	name VARCHAR(240),
	part_cat_id INTEGER,
	PRIMARY KEY(part_num),
	FOREIGN KEY part_cat_id_parts_FK (part_cat_id) REFERENCES part_categories(id)
);

-- --------------------------------------------------------
-- --------------------------------------------------------
-- sets
-- contains information on LEGO sets, including a unique 
-- ID number, the name of the set, the year it was 
-- released, its theme and how many parts it includes.
-- --------------------------------------------------------
-- --------------------------------------------------------

CREATE TABLE sets (
	set_num VARCHAR(20),
	name VARCHAR(100),
	year INTEGER,
	theme_id INTEGER,
	num_parts INTEGER,
	PRIMARY KEY(set_num),
	FOREIGN KEY theme_id_sets_FK (theme_id) REFERENCES themes(id)
);

-- --------------------------------------------------------------------------
-- --------------------------------------------------------------------------
-- inventories
-- contains information on inventories, including a unique ID, it's 
-- version and the set number
-- --------------------------------------------------------------------------
-- --------------------------------------------------------------------------

CREATE TABLE inventories (
	id INTEGER,
	version INTEGER,
	set_num VARCHAR(20),
	PRIMARY KEY(id),
	FOREIGN KEY id_inventories_FK (set_num) REFERENCES sets(set_num)
);

-- -----------------------------------------------
-- inventory_sets
-- contains information on what inventory is 
-- included in which sets, including the inventory 
-- ID, the set number and the quantity of that 
-- inventory that are included
-- -----------------------------------------------
-- -----------------------------------------------

CREATE TABLE inventory_sets (
	inventory_id INTEGER,
	set_num VARCHAR(30),
	quantity INTEGER,
	PRIMARY KEY(inventory_id, set_num),
	FOREIGN KEY inventory_id_inventory_sets_to_inventories_FK (inventory_id) REFERENCES inventories(id)
);


-- ------------------------------------------------
-- inventory_parts
-- contains information part inventories, including 
-- a unique ID number, the part number, the color 
-- of the part, how many are included and 
-- whether it's a spare.
-- ------------------------------------------------
-- ------------------------------------------------

CREATE TABLE inventory_parts (
	inventory_id INTEGER,
	part_num VARCHAR(20),
	color_id INTEGER,
	quantity INTEGER,
	is_spare CHAR(1),
	PRIMARY KEY(inventory_id, part_num, color_id),
	FOREIGN KEY inventory_id_inventory_parts_to_inventories_FK (inventory_id) REFERENCES inventories(id),
	FOREIGN KEY part_num_inventory_parts_to_parts_FK (part_num) REFERENCES parts(part_num),
	FOREIGN KEY color_id_inventory_parts_to_colors_FK (color_id) REFERENCES colors(id)

);


	