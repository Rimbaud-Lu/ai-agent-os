from rag.code_indexer import index

def search(q):

    result=[]

    for k,v in index.items():
        if q in v:
            result.append(k)

    return result
