import click

@click.command()
@click.argument('src', type=click.Path(exists=True, resolve_path=True))
@click.argument('dest',type=click.Path(exists=False, writable=True, resolve_path=True))
@click.option('--extensions', type=click.STRING, help='List of extensions to move separated by comma')
@click.option('--override/--no-override', default=False)
@click.option('-v', '--verbose', count=True)
def main(src, dest, extensions, override, verbose):
    click.echo(src) 
    click.echo(dest) 
    click.echo(override)
    if extensions:
        click.echo(extensions)
    if verbose:
        click.echo(verbose) 

if __name__ == '__main__':
    main()
