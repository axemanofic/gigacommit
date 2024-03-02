import typer


from gigacommit.callbacks import AppContext
from gigacommit.llm.model import GptModel

from gigacommit.git import get_diff


def commit(ctx: AppContext):
    diff = get_diff()
    model = GptModel(ctx.obj)
    typer.echo(diff)
    typer.echo(model.get_commit_message(diff))
    typer.echo("zalupa")
