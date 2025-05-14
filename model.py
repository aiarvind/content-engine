from pypdf import PdfReader
from llama_index.core import Document
from llama_index.core import VectorStoreIndex
from sentence_transformers import SentenceTransformer
from llama_index.core import Settings
from llama_index.core.embeddings import BaseEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


'''
✅ Phase 2: Document Processing & Indexing
	1.	Write Code to Load the PDFs
	•	Read and extract text from all files in /pdfs.
	2.	Build a Document Index
	•	Use LlamaIndex to index the loaded documents.
	3.	Create a Query Engine
	•	Turn the index into a queryable object so you can ask questions.
'''

# class SentenceTransformerEmbedder(BaseEmbedding):
#     def __init__(self):
#         self.model = SentenceTransformer("all-MiniLM-L6-v2")

#     def get_text_embedding(self, text: str) -> list[float]:
#         embedding = self.model.encode(text)
#         return embedding.tolist()

alphabet = PdfReader('pdfs/alphabet.pdf')
tesla = PdfReader('pdfs/tesla.pdf')
uber = PdfReader('pdfs/uber.pdf')

alphabet_text = ""
tesla_text = ""
uber_text = ""

for page in alphabet.pages: 
    text = page.extract_text()
    # print(text)
    alphabet_text += text
for page in tesla.pages: 
    text = page.extract_text()
    # print(text)
    tesla_text += text
for page in uber.pages: 
    text = page.extract_text()
    # print(text)
    uber_text += text

# print(alphabet_text)
# print(tesla_text)
# print(uber_text)

documents = [Document(text=alphabet_text), Document(text=tesla_text), Document(text=uber_text)]
# print(documents)

embeddings = []

# for document in documents: 
#     embeddings.append(get_text_embedding(document))

embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")

Settings.embed_model = embed_model
Settings.llm = None
vector_index = VectorStoreIndex.from_documents(documents)
query_engine = vector_index.as_query_engine(llm=None)

response = query_engine.query(
    "What are the risk factors mentioned in Alphabet's 10-K?"
)
print(response)
