import click

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Manage the client lifecycle"""


@clients.command()
@click.option("-n", "--name", type=str, prompt=True, help="The client name")
@click.option("-c", "--company", type=str, prompt=True, help="The client company")
@click.option("-e", "--email", type=str, prompt=True, help="The client email")
@click.option("-p", "--position", type=str, prompt=True, help="The client position")
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    clientService = ClientService(ctx.obj['clients_table'])

    clientService.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients = client_service.list_clients()

    #for idx, client in enumerate(clients):
    for client in clients:
        click.echo(' {name} | {company} | {email} | {position} | {uid} '.format(
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'],
            uid=client['uid']
        ))


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    
    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == client_uid]
    
    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_clients(client)
        print("Client updated")
    else:
        click.echo("Client not found")


def _update_client_flow(client):
    click.echo("Leave empty if you don't want to modify the value")

    client.name = click.prompt("New name", type=str, default=client.name)
    client.company = click.prompt("New company", type=str, default=client.company)
    client.email = click.prompt("New email", type=str, default=client.email)
    client.position = click.prompt("New position", type=str, default=client.position)

    return client


@clients.command()
@click.argument("client_uid", type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Delete a client"""
    client_service = ClientService(ctx.obj["clients_table"])

    clients = client_service.list_clients()

    client = [client for client in clients if client['uid'] == client_uid]

    if client:
        client_service.delete_client(Client(**client[0]))
        print("Client deleted")
    else:
        click.echo("Client not found")


all = clients
