import tabula

pdfpath="dd.pdf"
# pdfpath="https://sedl.org/afterschool/toolkits/science/pdf/ast_sci_data_tables_sample.pdf"

dfs=tabula.read_pdf(pdfpath,pages="1")

print(dfs)