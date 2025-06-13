#test ollama and make sure it's working as an LLM
from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.core.embeddings import resolve_embed_model


#instantiate our llm model
llm = Ollama(model="mistral", request_timeout=30.0)

parser = LlamaParse(result_type="markdown")

file_extractor = {".pdf": parser} 
documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data()

#creating access to a local model that will create different vector embeddings for us
embed_model = resolve_embed_model("local:BAAI/bge-m3")
vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

#allows you to utilize vector_index as question/answer bot
query_engine = vector_index.as_query_engine(llm=llm)

#test the query engine by sending it a query
result = query_engine.query("what are some of the routes in the api?")
print(result)