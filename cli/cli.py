import typer

app=typer.Typer()

@app.command()
def build(name:str):
    print(f"building {name}")

if __name__=="__main__":
    app()
