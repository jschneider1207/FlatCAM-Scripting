import click


@click.command()
@click.argument('kicad_project', type=click.Path(file_okay=False, dir_okay=True))
@click.option('--rubout/--no-rubout', default=True)
@click.option('--prefer-mill-drill/--no-prefer-mill-drill', default=True)
@click.option('--tools', type=click.File('rb'), default='r:/FlatCAM Scripting/tools.yaml')
@click.option('--out-dir', type=click.Path(file_okay=False, dir_okay=True), default='r:/FlatCAM/')
def generate(kicad_project, rubout, prefer_mill_drill, tools, out_dir):

    return


if __name__ == '__main__':
    generate()
