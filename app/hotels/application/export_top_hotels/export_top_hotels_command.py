from dataclasses import dataclass

from cqrs.commands.command import Command

@dataclass(frozen=True)
class ExportTopHotelsCommand(Command):
    rating_gte: float
    pass