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
@click.option('--nomin', is_flag=True, help='Disable minifier (use if no JRE/JVM), passes -n/--nomin to transcrypt')
def build(file, copy, nomin):
    click.echo('Transpiling to Javascript...')
    options = []
    if nomin:
        options += ['--nomin']
    t = envoy.run('transcrypt {} -p .none {}'.format(' '.join(options), file))  # --nomin means larger js file BUT does not need java (minifier)

    if t.status_code != 0:
        print('transcrypt compile error!')
        click.echo(t.std_out)
        sys.exit(-1)

    click.echo('Completed.')

    if copy is True:
        basename = os.path.basename(file)
        basename = os.path.splitext(basename)[0]
        basedir = os.path.dirname(file)
        # NOTE transcrypt version 3.6 emits to '__javascript__' directory, later versions (3.9) goto '__target__' directory
        if nomin:
            fpath = os.path.join(basedir, '__javascript__/{}.js'.format(basename))  # nomin version, i.e original un-minified version
        else:
            fpath = os.path.join(basedir, '__javascript__/{}.min.js'.format(basename))  # minified version
        with open(fpath, 'r') as minfile:
            pyperclip.copy(minfile.read())

        click.echo('Minified app.js copied to clipboard')
