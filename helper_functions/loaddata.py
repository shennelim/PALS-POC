# list of filenames to load

import os
from langchain_community.document_loaders import PyPDFLoader

def load_files():
    filename_list = [
        'Advisory for pet owners if pet is suspected to be exposed to poisons_final.pdf',
        'AM Public Registry Listing 27Dec2020 (2).pdf',
        'Boarding Conditions.pdf',
        'Breeding Conditions.pdf',
        'List of Accredited Dog Trainers_Updated.pdf'
    ]

    # load the documents
    list_of_documents_loaded = []
    for filename in filename_list:
        pdf_doc = []
        try:
            # try to load the document
            markdown_path = os.path.join('data', filename)
            # metadata, page_content
            loader = PyPDFLoader(markdown_path)

            # load() returns a list of Document objects
            for page in loader.lazy_load():
                pdf_doc.append(page)
            # use extend() to add to the list_of_documents_loaded
            list_of_documents_loaded.append(pdf_doc)
            print(f"Loaded {filename}")

        except Exception as e:
            # if there is an error loading the document, print the error and continue to the next document
            print(f"Error loading {filename}: {e}")
            continue

    #print("Total documents loaded:", len(list_of_documents_loaded))
    return list_of_documents_loaded