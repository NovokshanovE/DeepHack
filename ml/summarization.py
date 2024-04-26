from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts.prompt import PromptTemplate
from langchain.chat_models.gigachat import GigaChat
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from PyPDF2 import PdfFileReader

credentials = 'Yjg4MTQzMmUtNDAwMS00NDk0LThjOGUtNmU5ZWQ2YzQ4NDQ2OmQ4MWMxZGZiLTFmNGYtNDk5NS05OGQzLTBiMzYyYWJmNjk3OA=='
llm = GigaChat(credentials=credentials, verify_ssl_certs=False, scope="GIGACHAT_API_CORP")


def parse_pdf_text_to_txt(pdf_filename, txt_filename):
    extracted_text = ""
    
    # Открытие PDF-файла для чтения
    with open(pdf_filename, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        
        # Извлечение текста из каждой страницы
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            page_text = page.extractText()
            extracted_text += page_text
    
    # Запись извлеченного текста в файл txt
    with open(txt_filename, "w", encoding="utf-8") as txt_file:
        txt_file.write(extracted_text)


def get_summarization(filename: str, llm: GigaChat):

    # Пример использования функции
    parse_pdf_text_to_txt(filename, "extracted_text.txt")

    loader = TextLoader("extracted_text.txt", encoding="utf-8")
    doc = loader.load()

    split_docs = RecursiveCharacterTextSplitter(chunk_size=8000, chunk_overlap=1500).split_documents(
        doc
    )

    map_prompt = PromptTemplate(
    template="Изложи суммаризацию следующего как можно более развернуто и подробно:\n{text}",
    input_variables=["text"]
    )

    chain = load_summarize_chain(llm, chain_type="map_reduce", map_prompt=map_prompt)
    res = chain.run(split_docs)

    return {'text': res}