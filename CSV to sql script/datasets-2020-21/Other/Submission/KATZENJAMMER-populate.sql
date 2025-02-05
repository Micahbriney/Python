 -- Albums

       -- AId: unique identifier of the album
     -- Title: title of the album
      -- Year: year the album was released
     -- Label: label (record company) that released the album
      -- Type: type of recording (studio, live, etc.)
-- **************************************************************************
	
	INSERT INTO Albums (AId,Title,Year,Label,Type)
VALUES
	(1,'Le Pop',2008,'Propeller Recordings','Studio'),
	(2,'A Kiss Before You Go',2011,'Propeller Recordings','Studio'),
	(3,'A Kiss Before You Go: Live in Hamburg',2012,'Universal Music Group','Live'),
	(4,'Rockland',2015,'Propeller Recordings','Studio');


  -- Band

         -- Id: unique id of each band member
  -- Firstname: first name of each band member
   -- Lastname: last name of each band member
 -- **************************************************************************

INSERT INTO Band (Id,Firstname,Lastname)
VALUES
	(1,'Solveig','Heilo'),
	(2,'Marianne','Sveen'),
	(3,'Anne-Marit','Bergheim'),
	(4,'Turid','Jorgensen');


   -- Songs

       -- SongId: unique identifier of the song
        -- Title: song title
-- **************************************************************************

	INSERT INTO Songs (SongId,Title)
VALUES
	(1,'Overture'),
	(2,'A Bar In Amsterdam'),
	(3,'Demon Kitty Rag'),
	(4,'Tea With Cinnamon'),
	(5,'Hey Ho on the Devil\'s Back'),
	(6,'Wading in Deeper'),
	(7,'Le Pop'),
	(8,'Der Kapitan'),
	(9,'Virginia Clemm'),
	(10,'Play My Darling, Play'),
	(11,'To the Sea'),
	(12,'Mother Superior'),
	(13,'Aint no Thang'),
	(14,'A Kiss Before You Go'),
	(15,'I Will Dance (When I Walk Away)'),
	(16,'Cherry Pie'),
	(17,'Land of Confusion'),
	(18,'Lady Marlene'),
	(19,'Rock-Paper-Scissors'),
	(20,'Cocktails and Ruby Slippers'),
	(21,'Soviet Trumpeter'),
	(22,'Loathsome M'),
	(23,'Shepherds Song'),
	(24,'Gypsy Flee'),
	(25,'Gods Great Dust Storm'),
	(26,'Ouch'),
	(27,'Listening to the World'),
	(28,'Johnny Blowtorch'),
	(29,'Flash'),
	(30,'Driving After You'),
	(31,'My Own Tune'),
	(32,'Badlands'),
	(33,'Old De Spain'),
	(34,'Oh My God'),
	(35,'Lady Gray'),
	(36,'Shine Like Neon Rays'),
	(37,'Flash in the Dark'),
	(38,'My Dear'),
	(39,'Bad Girl'),
	(40,'Rockland'),
	(41,'Curvaceous Needs'),
	(42,'Borka'),
	(43,'Let it Snow');


   -- Performance
        -- SongId: id of the song (see Songs.SongId)
      -- Bandmate: id of the band member (see Band.Id)
 -- StagePosition: stage position of the band member during the live 
                -- performances of the song [2]
      
 -- [2] due to positioning of the instruments the band members play, no band
     -- member ever changes her position during a single song. All position
     -- changes are between songs. Also, some band members can share the same
     -- position (usually 'center') during the same song.
-- **************************************************************************

    INSERT INTO Performance (SongId,Bandmate,StagePosition)
VALUES
	(1,1,'back'),
	(1,2,'left'),
	(1,3,'center'),
	(1,4,'right'),
	(2,1,'center'),
	(2,2,'back'),
	(2,3,'left'),
	(2,4,'right'),
	(3,1,'back'),
	(3,2,'right'),
	(3,3,'center'),
	(3,4,'left'),
	(4,1,'back'),
	(4,2,'center'),
	(4,3,'left'),
	(4,4,'right');


   -- Instruments

      -- SongId: id of the song (see Songs.SongId)
  -- BandmateId: id of the band member (see Band.Id)
  -- Instrument: name of the instrument played [1]  
    
  -- [1] On some songs, some members of Katzenjammer play multiple instruments.
      -- When this happens, Instruments contains one row per instrument
      -- played.
-- **************************************************************************

	INSERT INTO Instruments (SongId,BandmateId,Instrument)
VALUES
	(1,1,'trumpet'),
	(1,2,'keyboard'),
	(1,3,'accordion'),
	(1,4,'bass balalaika'),
	(2,1,'trumpet'),
	(2,2,'drums'),
	(2,3,'guitar'),
	(2,4,'bass balalaika'),
	(3,1,'drums'),
	(3,1,'ukalele'),
	(3,2,'banjo'),
	(3,3,'bass balalaika'),
	(3,4,'keyboards'),
	(4,1,'drums'),
	(4,2,'ukalele'),
	(4,3,'accordion'),
	(4,4,'bass balalaika');


   -- Tracklists

      -- AlbumId:  id of the album (see Albums.Aid)
     -- Position:  position of the song on the album (first, second, etc...)
       -- SongId:  id of the song (see Songs.SongId)
-- **************************************************************************

	INSERT INTO Tracklists (AlbumId,Position,SongId)
VALUES
	(1,1,1),
	(1,2,2),
	(1,3,3),
	(1,4,4),
	(1,5,5),
	(1,6,6),
	(1,7,7),
	(1,8,8),
	(1,9,9),
	(1,10,10),
	(1,11,11),
	(1,12,12),
	(1,13,13),
	(2,1,14),
	(2,2,15),
	(2,3,16),
	(2,4,17),
	(2,5,18),
	(2,6,19),
	(2,7,20),
	(2,8,21),
	(2,9,22),
	(2,10,23),
	(2,11,24),
	(2,12,25),
	(3,1,14),
	(3,2,26),
	(3,3,3),
	(3,4,15),
	(3,5,11),
	(3,6,19),
	(3,7,18),
	(3,8,16),
	(3,9,12),
	(3,10,17),
	(3,11,22),
	(3,12,20),
	(3,13,2),
	(3,14,5),
	(3,15,8),
	(3,16,7),
	(3,17,25),
	(3,18,13),
	(3,19,24),
	(4,1,33),
	(4,2,41),
	(4,3,34),
	(4,4,35),
	(4,5,31),
	(4,6,36),
	(4,7,30),
	(4,8,37),
	(4,9,38),
	(4,10,39),
	(4,11,40);


   -- Vocals

      -- SongId: id of the song (see Songs.SongId)
    -- Bandmate: id of the band member (see Band.Id)
        -- Type: type of vocal performance of the band member on the song [3]

-- [3] Types of vocal performance typically are "lead", "chorus" and "shared".
-- (there is also a single instance of "rap"). A band member can be listed
-- for more than one type of vocal performance for a given song.
-- **************************************************************************

	INSERT INTO Vocals (SongId,Bandmate,Type)
VALUES
	(2,1,'lead'),
	(2,3,'chorus'),
	(2,4,'chorus'),
	(3,2,'lead'),
	(4,1,'chorus'),
	(4,2,'lead'),
	(4,3,'chorus'),
	(4,4,'chorus');	
