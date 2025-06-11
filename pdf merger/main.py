from PyPDF2 import PdfMerger
import os

def merge_pdfs_interactive():
    """Interactive PDF merger that asks for files and output name"""
    pdf_merger = PdfMerger()
    
    print("PDF Merger - Combine multiple PDFs into one")
    print("Enter the PDF filenames one by one (leave empty to finish):")
    
    files_to_merge = []
    while True:
        file_name = input("> ").strip()
        if not file_name:
            break
        if not os.path.exists(file_name):
            print(f"File '{file_name}' not found. Try again.")
            continue
        if not file_name.lower().endswith('.pdf'):
            print("Please enter only PDF files.")
            continue
        files_to_merge.append(file_name)
    
    if not files_to_merge:
        print("No files selected. Exiting.")
        return
    
    output_name = input("Enter output filename (default: merged.pdf): ").strip()
    if not output_name:
        output_name = 'merged.pdf'
    elif not output_name.lower().endswith('.pdf'):
        output_name += '.pdf'
    
    merge_pdfs(files_to_merge, output_name)

def merge_pdfs(file_paths, output_path):
    """Same merge function as before"""
    pdf_merger = PdfMerger()
    
    for path in file_paths:
        with open(path, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)
    
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)
    
    print(f"Successfully merged {len(file_paths)} PDFs into {output_path}")

if __name__ == "__main__":
    merge_pdfs_interactive()