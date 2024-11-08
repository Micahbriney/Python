DROP TABLE IF EXISTS Vocals;
DROP TABLE IF EXISTS Tracklists;
DROP TABLE IF EXISTS Instruments;
DROP TABLE IF EXISTS Performance;
DROP TABLE IF EXISTS Songs;
DROP TABLE IF EXISTS Band;
DROP TABLE IF EXISTS Albums;

-- ------------------------
--
--
-- NOTE: foreign key added to performance which references band
-- Order of create statements and drop table statements could be wrong
--
-- -----------------------


 -- Albums

       -- AId: unique identifier of the album
     -- Title: title of the album
      -- Year: year the album was released
     -- Label: label (record company) that released the album
      -- Type: type of recording (studio, live, etc.)

	-- -- ex: 
	-- AId	Title	Year	Label	 				Type
	-- 1	Le Pop	2008	Propeller Recordings	Studio

-- **************************************************************************

CREATE TABLE Albums (
	AId INTEGER,
	Title VARCHAR(50),
	Year INTEGER,
	Label VARCHAR(30),
	Type VARCHAR(30),
	PRIMARY KEY(AId)
);

  -- Band

         -- Id: unique id of each band member
  -- Firstname: first name of each band member
   -- Lastname: last name of each band member
   

-- **************************************************************************

CREATE TABLE Band (
	Id INTEGER,
	Firstname VARCHAR(30),
	Lastname VARCHAR(30),
	PRIMARY KEY(Id)
);

   -- Songs

       -- SongId: unique identifier of the song
        -- Title: song title

-- **************************************************************************

CREATE TABLE Songs (
	SongId INTEGER,
	Title VARCHAR(50),
	PRIMARY KEY(SongId)
);

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

CREATE TABLE Performance (
	SongId INTEGER,
	Bandmate INTEGER,
	StagePosition VARCHAR(30),
	FOREIGN KEY SongId_FK (SongId) REFERENCES Songs(SongId),
	FOREIGN KEY Bandmate_FK (Bandmate) REFERENCES Band(Id),
	PRIMARY KEY(SongId, Bandmate)
);

   -- Instruments

      -- SongId: id of the song (see Songs.SongId)
  -- BandmateId: id of the band member (see Band.Id)
  -- Instrument: name of the instrument played [1]  
    
  -- [1] On some songs, some members of Katzenjammer play multiple instruments.
      -- When this happens, Instruments contains one row per instrument
      -- played.

-- **************************************************************************

CREATE TABLE Instruments (
	SongId INTEGER,
	BandmateId INTEGER,
	Instrument VARCHAR(30),
	FOREIGN KEY BandmateId_instruments_FK (BandmateId) REFERENCES Band(Id),
	FOREIGN KEY SongId_instruments_FK (SongId) REFERENCES Songs(SongId),
	PRIMARY KEY(SongId, BandmateId, Instrument)
);

   -- Tracklists

      -- AlbumId:  id of the album (see Albums.Aid)
     -- Position:  position of the song on the album (first, second, etc...)
       -- SongId:  id of the song (see Songs.SongId)


-- **************************************************************************

CREATE TABLE Tracklists (
	AlbumId INTEGER,
	Position INTEGER,
	SongId INTEGER,
	FOREIGN KEY SongId_tracklists_FK (SongId) REFERENCES Songs(SongId),
	FOREIGN KEY AlbumId_tracklists_FK (AlbumId) REFERENCES Albums(AId),
	PRIMARY KEY(AlbumId, Position)
);

   -- Vocals

      -- SongId: id of the song (see Songs.SongId)
    -- Bandmate: id of the band member (see Band.Id)
        -- Type: type of vocal performance of the band member on the song [3]

-- [3] Types of vocal performance typically are "lead", "chorus" and "shared".
-- (there is also a single instance of "rap"). A band member can be listed
-- for more than one type of vocal performance for a given song.

-- **************************************************************************

CREATE TABLE Vocals (
	SongId INTEGER,
	Bandmate INTEGER,
	Type VARCHAR(30),
	FOREIGN KEY BandmateId_vocals_FK (Bandmate) REFERENCES Band (Id),
	FOREIGN KEY SongId_vocals_FK (SongId) REFERENCES Songs (SongId),
	PRIMARY KEY(SongId, Bandmate, Type)
);
