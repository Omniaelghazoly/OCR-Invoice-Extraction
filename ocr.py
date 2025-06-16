from importnb import Notebook
with Notebook():
    from notebooks.ocr import get_invoice_data


outputs = get_invoice_data(r"data\Invoices\3.jpg")   
print(outputs) 