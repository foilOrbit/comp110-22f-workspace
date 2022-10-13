"""Dictionary related utility functions."""

__author__ = ""

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Read that file as a CSV instead of just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file when we're done, to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(row_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a column-based table with only the first N rows of data per column."""
    result: dict[str, list[str]] = {}
    for column in row_table:
        n_list: list[str] = []
        i: int = 0
        for entry in row_table[column]:
            if i < n:
                n_list.append(entry)
            i += 1
        result[column] = n_list
    return result


def select(table: dict[str, list[str]], input_list: list[str]) -> dict[str, list[str]]:
    """This function will return a new table with only the desired columns."""
    result: dict[str, list[str]] = {}
    for i in input_list:
        result[i] = table[i]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """This function will concatenate two tables."""
    result: dict[str, list[str]] = {}
    for key in table1:
        result[key] = table1[key]
    for key in table2:
        if key in result:
            result[key] += table2[key]
        else:
            result[key] = table2[key]
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """This function will produce a dict that shows the number of times a value appeared in a list."""
    result: dict[str, int] = {}
    for i in input_list:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
