import click

from clients import commands as clients_commands

CLIENTS_TABLE = "E:\\platzi\\python\\2019\\platzi_ventas\\.clients.csv"


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all)
