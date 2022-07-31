import os

import fitz


def combine_plot_pdfs():
    print('💠 Combining PDFs')
    combined = fitz.open()
    
    plots = os.listdir('./plots')
    for plot in plots:
        # Only consider pdf files
        if not plot.endswith('.pdf'):
            continue

        pdf_plot = fitz.open(f'./plots/{plot}')

        # Open pdf and insert
        combined.insert_pdf(pdf_plot)

    combined.save('./plots/statistics.pdf')
