from elasticsearch import Elasticsearch
from transform_data_with_pandas import full_data


es = Elasticsearch()
for i, row in full_data.iterrows():
    doc = row.to_json()
    res = es.index(index='vaccines',
                   doc_type='doc', body=doc)
    print(res)