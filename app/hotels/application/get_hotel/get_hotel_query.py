from dataclasses import dataclass
from cqrs.queries.query import Query

@dataclass(frozen=True)
class GetHotelsQuery(Query):
    pass