import yfinance as yf
import pandas as pd

def fetch_financial_data():
    # Define the ticker symbol for Apple Inc.
    ticker_symbol = 'AAPL'

    # Fetch data for Apple Inc.
    apple = yf.Ticker(ticker_symbol)

    # Get financial statements
    income_statement = apple.financials
    balance_sheet = apple.balance_sheet
    cash_flow_statement = apple.cashflow

    # Transpose the data
    income_statement_transposed = income_statement.transpose()
    balance_sheet_transposed = balance_sheet.transpose()
    cash_flow_statement_transposed = cash_flow_statement.transpose()

    # Optionally, if you want to add a 'Date' column to make it explicit
    income_statement_transposed.reset_index(inplace=True)
    balance_sheet_transposed.reset_index(inplace=True)
    cash_flow_statement_transposed.reset_index(inplace=True)
    income_statement_transposed.rename(columns={'index': 'Date'}, inplace=True)
    balance_sheet_transposed.rename(columns={'index': 'Date'}, inplace=True)
    cash_flow_statement_transposed.rename(columns={'index': 'Date'}, inplace=True)

    # Save the transformed financial statements to CSV files
    income_statement_transposed.to_csv('income_statement_transposed.csv', index=False)
    balance_sheet_transposed.to_csv('balance_sheet_transposed.csv', index=False)
    cash_flow_statement_transposed.to_csv('cash_flow_statement_transposed.csv', index=False)

if __name__ == "__main__":
    fetch_financial_data()
