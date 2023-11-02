CREATE TABLE AAPL_StockData (
    Date DATE NOT NULL,
    OpenPrice DECIMAL(10, 2) NOT NULL,
    HighPrice DECIMAL(10, 2) NOT NULL,
    LowPrice DECIMAL(10, 2) NOT NULL,
    ClosePrice DECIMAL(10, 2) NOT NULL,
    Volume BIGINT NOT NULL,
    PRIMARY KEY (Date)
);

-- Index already created by primary key constraint

CREATE TABLE EconomicData (
    Country NVARCHAR(255) NOT NULL,
    Date DATE NOT NULL,
    GDP DECIMAL(20, 2),
    GDP_per_capita DECIMAL(20, 2),
    Unemployment DECIMAL(5, 2),
    Inflation DECIMAL(5, 2),
    Personal_remittances DECIMAL(20, 2),
    CO2_emissions DECIMAL(10, 2),
    Access_to_electricity DECIMAL(5, 2),
    PRIMARY KEY (Country, Date)
);
