DROP DATABASE IF EXISTS soap-cat-db;

CREATE DATABASE soap-cat-db;

USE soap-cat-db;

CREATE TABLE
    donors (
        name VARCHAR(255) PRIMARY KEY,
        json_data VARCHAR(1536), -- a json without the titles section is always 1488 (movable without CMAC), 1536 is the next round number above 1488
        last_transferred INT UNSIGNED,
        uploader VARCHAR(18),
        note VARCHAR(128) DEFAULT "None"
    );

/* 0-10 in last_transferred mean special things
0 means it needs to be prepared before it can be used
1 means it was manually disabled by someone and will need to be re-enabled manually
2 means the last_transferred time should be refreshed
3 means it was automatically disabled due to some error and needs to be adressed by someone
4-10 are reserved for future use
 */