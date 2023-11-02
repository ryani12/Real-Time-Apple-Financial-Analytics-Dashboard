# Real-Time-Apple-Financial-Analytics-Dashboard


---

## Project Documentation

### Phase 1: Project Setup and Database Design

#### 1. Version Control:
   - **GitHub Repository Setup**:
     - Created a GitHub repository to manage version control for the project.
     - The repository will hold all project files including code, data schemas, and documentation.

   - **Commit Strategy**:
     - Committing changes at the end of each significant task or milestone.
     - Meaningful commit messages to describe the changes made.

   - **Branching Strategy**:
     - Utilizing feature branching for working on new features or tasks.
     - Merging branches back into the main branch upon completion and review.

#### 2. Market Data Schema Design:
   - **Azure SQL Database Setup**:
     - Setup Azure SQL Database for structured data storage.
     - Database Name: AppleFinancialDB

   - **Market Data Table Creation**:
     - Created a table named `AAPL_StockData` to store the stock market data of Apple Inc.
     - SQL Script: In "1_Project_Setup_and_Database_Design\database_design\market_data"

   - **Indexing**:
     - An index is created on the `Date` column by default due to the primary key constraint, which will speed up queries against this column.

   - **Constraints**:
     - The `Date` column is set as the primary key to ensure each day's data is unique.
     - The `NOT NULL` constraint is used to ensure that all data columns are filled.

   - **Data Types**:
     - Utilized `DECIMAL(10,2)` for price columns to accommodate prices up to 10 digits with 2 decimal places.
     - Utilized `BIGINT` for Volume to accommodate large numbers.
     - Utilized `DATE` for the Date column to store date values.

   - **Data Import**:
     - Imported the CSV file generated from Alpha Vantage into the `AAPL_StockData` table to populate it with market data.

---
