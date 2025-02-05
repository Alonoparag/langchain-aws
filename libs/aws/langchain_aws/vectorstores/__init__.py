import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from langchain_aws.vectorstores.inmemorydb import InMemoryVectorStore
    from langchain_aws.vectorstores.documentdb import MongoDBVectorStore

__all__ = [
    "InMemoryVectorStore",
    "MongoDBVectorStore",
]

_module_lookup = {
    "InMemoryVectorStore": "langchain_aws.vectorstores.inmemorydb",
    "MongoDBVectorStore": "langchain_aws.vectorstores.documentdb",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
