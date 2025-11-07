import click
import json

@click.command()
@click.argument("name")
def greet(name):
    """Renvoie message JSON"""
    message = {"message": f"Bonjour {name}"}
    print(json.dumps(message))


if __name__ == "__main__":
    greet()