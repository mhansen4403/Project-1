# 6:09 PM 9/11/2023 was able to get it to successfully scan through pdf to find most relevant section
import os
import getpass
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
unstructuredLoader = UnstructuredPDFLoader("asop18.pdf")
pypdfLoader = PyPDFLoader("asop18.pdf")
data = unstructuredLoader.load()
pages = pypdfLoader.load_and_split()
counter = 1
faissIndex = FAISS.from_documents(pages, OpenAIEmbeddings())
documents = faissIndex.similarity_search("Cognitive impairment", k = 2)
documentString = ""
for document in documents:
    documentString += str(document)
documentString = documentString.replace("\\n", "")