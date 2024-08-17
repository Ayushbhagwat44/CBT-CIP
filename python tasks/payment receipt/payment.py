from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Function to create a payment receipt
def create_receipt(filename, data):
    pdf = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Title
    styles = getSampleStyleSheet()
    title = Paragraph("Payment Receipt", styles['Title'])
    elements.append(title)

    # Table for the receipt
    table = Table(data)

    # Table style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    elements.append(table)
    
    # Build the PDF
    pdf.build(elements)
    print(f"Receipt saved as {filename}")

# Sample data for the receipt
data = [
    ["Item", "Quantity", "Price"],
    ["Product 1", "2", "$10.00"],
    ["Product 2", "1", "$15.00"],
    ["Product 3", "3", "$7.00"],
    ["Total", "", "$54.00"]
]

# Create the receipt
create_receipt("payment_receipt.pdf", data)
