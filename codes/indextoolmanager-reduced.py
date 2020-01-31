from arango import ArangoClient
from elasticsearch import Elasticsearch
class IndexToolManager:
    def __init__(self, indexName='default_index',
                 bm25_b=0.75, bm25_k1=1.2, bm25_k3=0.0, top_k=100):
        # Inicializa classes das ferramentas e conecta com os bancos de 
    def log_result(self, itemKey, itemBody):
        # Insere um documento no banco de dados do Elasticsearch
    def get_documents(self, db='authorprof', documents_xml_folder='db_authorprof/en/',
                      truth_txt='db_authorprof/truth.txt',
                      append_class_to_id=False):
        # Generates a list with all documents from db formatted files.
    def calc_IR(self, result_df, positive_class='true'):
        # Calcula os atributos de RI sugeridos para a pesquisa
        # e retorna esses atributos em um dicionário do Python
    def insertArango(self, itemKey, itemBody):
        # Insere um documento na coleção 'indexName' do ArangoDB.
    def arango_query(self, query, ignore_first_result=False):
        # Consulta uma 'view' do ArangoDB e retorna um DataFrame do 
        # Pandas com os resultados.
    def arango_get_IR_variables(self, query, positive_class='true', ignore_first_result=False):
        # Consulta uma 'view' do ArangoDB e retorna um 'dict' com os
        # atributos de RI.