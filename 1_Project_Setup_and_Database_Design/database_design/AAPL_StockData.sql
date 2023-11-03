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
