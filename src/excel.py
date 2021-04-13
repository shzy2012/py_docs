from __future__ import print_function
from os.path import join, dirname, abspath, isfile
from collections import Counter
import xlrd
from xlrd.sheet import ctype_text   


def get_excel_sheet_object(fname, idx=0):
    if not isfile(fname):
        print ('File doesn't exist: ', fname)

    # Open the workbook and 1st sheet
    xl_workbook = xlrd.open_workbook(fname)
    xl_sheet = xl_workbook.sheet_by_index(0)
    print (40 * '-' + 'nRetrieved worksheet: %s' % xl_sheet.name)

    return xl_sheet

def show_column_names(xl_sheet):
    row = xl_sheet.row(0)  # 1st row
    print(60*'-' + 'n(Column #) value [type]n' + 60*'-')
    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        print('(%s) %s [%s]' % (idx, cell_obj.value, cell_type_str, ))

def get_column_stats(xl_sheet, col_idx):
    """
    :param xl_sheet:  Sheet object from Excel Workbook, extracted using xlrd
    :param col_idx: zero-indexed int indicating a column in the Excel workbook
    """
    if xl_sheet is None:
        print ('xl_sheet is None')
        return

    if not col_idx.isdigit():
        print ('Please enter a valid column number (0-%d)' % (xl_sheet.ncols-1))
        return

    col_idx = int(col_idx)
    if col_idx < 0 or col_idx >= xl_sheet.ncols:
        print ('Please enter a valid column number (0-%d)' % (xl_sheet.ncols-1))
        return 

    # Iterate through rows, and print out the column values
    row_vals = []
    for row_idx in range(0, xl_sheet.nrows):
        cell_obj = xl_sheet.cell(row_idx, col_idx)
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        print ('(row %s) %s (type:%s)' % (row_idx, cell_obj.value, cell_type_str))
        row_vals.append(cell_obj.value)

    # Retrieve non-empty rows
    nonempty_row_vals = [x for x in row_vals if x]    
    num_rows_missing_vals = xl_sheet.nrows - len(nonempty_row_vals)
    print ('Vals: %d; Rows Missing Vals: %d' % (len(nonempty_row_vals), num_rows_missing_vals))

    # Count occurrences of values 
    counts = Counter(nonempty_row_vals)

    # Display value counts
    print ('-'*40 + 'n', 'Top Twenty Values', 'n' + '-'*40 )
    print ('Value [count]')
    for val, cnt in counts.most_common(20):
        print ('%s [%s]' % (val, cnt))

def column_picker(xl_sheet):
    try:
        input = raw_input
    except NameError:
        pass

    while True:
        show_column_names(xl_sheet)
        col_idx = input("nPlease enter a column number between 0 and %d (or 'x' to Exit): " % (xl_sheet.ncols-1))
        if col_idx == 'x': 
            break
        get_column_stats(xl_sheet, col_idx)


if __name__=='__main__':
    excel_crime_data = join(dirname(dirname(abspath(__file__))), 'test_data', 'test.xls')
    xl_sheet = get_excel_sheet_object(excel_crime_data)
    column_picker(xl_sheet)