import xlsxwriter

# Create a new workbook and add worksheets
output_file = 'D:/Learning/aaaa/Single_Loan_Repayment_Tracker_Formula.xlsx'
workbook = xlsxwriter.Workbook(output_file)

# Add formats
header_format = workbook.add_format({'bold': True, 'bg_color': '#D9E1F2', 'border': 1})
currency_format = workbook.add_format({'num_format': '₹#,##0', 'border': 1})
percent_format = workbook.add_format({'num_format': '0.00%', 'border': 1})
normal_format = workbook.add_format({'border': 1})

# ---------------- Loan Summary Sheet -------------------
summary_sheet = workbook.add_worksheet('Loan Summary')
summary_headers = [
    'Loan Amount (₹)', 'Interest Rate (%)', 'Time (Months)',
    'Interest Amount (₹)', 'Total Payable (₹)', 'Loan Start Date'
]
for col, header in enumerate(summary_headers):
    summary_sheet.write(0, col, header, header_format)

# Write values
summary_sheet.write(1, 0, 900000, currency_format)  # Loan Amount
summary_sheet.write(1, 1, 9.10 / 100, percent_format)  # Interest Rate (as decimal for Excel)
summary_sheet.write(1, 2, 12, normal_format)  # 12 months
summary_sheet.write_formula(1, 3, '=A2*B2*C2', currency_format)  # Interest = Principal * Rate * Time
summary_sheet.write_formula(1, 4, '=A2+D2', currency_format)  # Total Payable = Principal + Interest
summary_sheet.write(1, 5, '01-May-2025', normal_format)  # Start Date

# ---------------- Repayment Tracker Sheet -------------------
tracker_sheet = workbook.add_worksheet('Repayment Tracker')
tracker_headers = [
    'Date of Repayment', 'Amount Paid (₹)', 'Principal Repaid (₹)',
    'Interest Paid (₹)', 'Remaining Principal (₹)',
    'Remaining Interest (₹)', 'Total Remaining (₹)'
]
for col, header in enumerate(tracker_headers):
    tracker_sheet.write(0, col, header, header_format)

# Pre-fill 20 rows with formulas for dynamic calculation
rows = 20
for row in range(1, rows + 1):
    # Date and Amount Paid columns are left for user input
    tracker_sheet.write_blank(row, 0, None, normal_format)  # Date
    tracker_sheet.write_blank(row, 1, None, currency_format)  # Amount Paid

    if row == 1:  # First row, initial balances come from Loan Summary
        # Interest Paid: minimum of amount paid and total interest remaining
        tracker_sheet.write_formula(row, 3, '=MIN(B2, \'Loan Summary\'!D2)', currency_format)
        # Principal Repaid: rest goes to principal
        tracker_sheet.write_formula(row, 2, '=B2 - D2', currency_format)
        # Remaining Principal
        tracker_sheet.write_formula(row, 4, '=\'Loan Summary\'!A2 - C2', currency_format)
        # Remaining Interest
        tracker_sheet.write_formula(row, 5, '=\'Loan Summary\'!D2 - D2', currency_format)
        # Total Remaining
        tracker_sheet.write_formula(row, 6, '=E2 + F2', currency_format)
    else:  # For other rows
        prev_row = row
        # Interest Paid: minimum of amount paid and previous remaining interest
        tracker_sheet.write_formula(row, 3, f'=MIN(B{row+1}, F{prev_row})', currency_format)
        # Principal Repaid: rest goes to principal
        tracker_sheet.write_formula(row, 2, f'=B{row+1} - D{row+1}', currency_format)
        # Remaining Principal
        tracker_sheet.write_formula(row, 4, f'=E{prev_row} - C{row+1}', currency_format)
        # Remaining Interest
        tracker_sheet.write_formula(row, 5, f'=F{prev_row} - D{row+1}', currency_format)
        # Total Remaining
        tracker_sheet.write_formula(row, 6, f'=E{row+1} + F{row+1}', currency_format)

# Set column widths
tracker_sheet.set_column('A:A', 18)
tracker_sheet.set_column('B:G', 18)

workbook.close()

output_file
