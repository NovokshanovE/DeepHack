from langchain.schema import HumanMessage
from langchain.chat_models.gigachat import GigaChat
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from chromadb.config import Settings
from langchain.vectorstores import Chroma
from langchain_community.embeddings.gigachat import GigaChatEmbeddings

from ..evgeny.parser import parser_links, parser


credentials = 'Yjg4MTQzMmUtNDAwMS00NDk0LThjOGUtNmU5ZWQ2YzQ4NDQ2OmQ4MWMxZGZiLTFmNGYtNDk5NS05OGQzLTBiMzYyYWJmNjk3OA=='
llm = GigaChat(credentials=credentials, verify_ssl_certs=False, scope="GIGACHAT_API_CORP")
embeddings = GigaChatEmbeddings(credentials=credentials, verify_ssl_certs=False, scope="GIGACHAT_API_CORP")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50,
)


def get_sources_links(llm: GigaChat, embeddings: GigaChatEmbeddings, text_splitter: RecursiveCharacterTextSplitter, prompt: str = "математика",) -> dict:
    prompt = translate_to_eng(prompt, llm, embeddings)
    links = parser_links(prompt)
    docs = [parser(i) for i in links] # {"title": title, "text": text, "links": links}
    
    filenames = []
    for i, doc in enumerate(docs):
        filenames.append(encode_file(doc["text"], links[i])) # text == link
    db = sources_initialization(filenames, text_splitter)
    
    result_docs = db.similarity_search(prompt, k=20)
    
    result = []
    for doc in result_docs:
        link = decode_link_from_file(doc[i].metadata['source'])#[len("docs/"):-len(".txt")]
        doc_index = find_doc_by_link(link, links)
        title = docs[doc_index]['title']
        outer_sources = docs[doc_index]['links']
        annotation = docs[doc_index]['text']
        result.append({
            "title": title,
            "links": outer_sources,
            "annotation": annotation
        })
    return result
    
    
def encode_name(name:str) -> str:
    name = name.replace("/", "(")
    name = name.replace(".", "_")
    name = name.replace(":", ")")
    return name 


def encode_file(doc: str, link: str) -> str:
    name = link
    name = name.replace("/", "(")
    name = name.replace(".", "_")
    name = name.replace(":", ")")
    with open(f"docs/{name}.txt", "w", encoding="utf-8") as file:
        file.write(doc)
    return f"docs/{name}.txt"

    
def decode_link_from_file(file_name: str) -> str:
    name = file_name[len("docs/"):-len(".txt")]
    name = name.replace("(", "/")
    name = name.replace("_", ".")
    name = name.replace(")", ":")
    return name


def find_doc_by_link(link: str, links: list) -> int:
    return links.index(link)


def detect_language(llm: GigaChat, text: str) -> str:
  question = f"На каком языке? {text[:20]}"
  answer = llm([HumanMessage(content=question)]).content #[0:200]
  if "рус" in answer:
    return "ru"
  return "en"


def translate_to_eng(llm: GigaChat, text: str, embeddings: GigaChatEmbeddings) -> str:
  #if detect_language(text, llm) != "en":
  question = f"Переведи на английский. {text}"
  answer = llm([HumanMessage(content=question)]).content 
  return answer
    

def sources_initialization(filenames: list, text_splitter: RecursiveCharacterTextSplitter):
    documents=[]
    for filename in filenames:
        loader = TextLoader(filename)
        document = loader.load()
        document = text_splitter.split_documents(document)
        documents.append(document)

    db = Chroma.from_documents(
        documents,
        embeddings,
        client_settings=Settings(anonymized_telemetry=False),
    )
    return db
