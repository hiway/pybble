import os
import sys

import click
import envoy
import pyperclip


@click.group()
def cli():
    pass


@cli.command()
@click.argument('file')
@click.option('--copy', is_flag=True, help='Copies compiled, minified '
                                           'javascript to system clipboard.')
def build(file, copy):
    click.echo('Transpiling to Javascript...')
    t = envoy.run('transcrypt -f -p .none {}'.format(file))

    if t.status_code != 0:
        click.echo(t.std_out)
        sys.exit(-1)

    click.echo('Completed.')

    if copy is True:
        basename = os.path.basename(file)
        basename = os.path.splitext(basename)[0]
        basedir = os.path.dirname(file)
        fpath = os.path.join(basedir, '__javascript__/{}.min.js'.format(basename))
        with open(fpath, 'r') as minfile:
            pyperclip.copy(minfile.read())

        click.echo('Minified app.js copied to clipboard')
