import sys
from pathlib import Path


def main(app_dirname):
    app_dir = Path(app_dirname)
    print(f'Removing migration files from {app_dirname} app')

    # Remove *.pyc migration files
    migration_pyc_files = app_dir.glob('migrations/*.pyc')
    for migration_file in migration_pyc_files:
        if migration_file.is_file():
            migration_file.unlink(missing_ok=True)
            print(f'  Removing {migration_file}')

    # Remove *.py migration files (except __init__.py files)
    migration_py_files = app_dir.glob('migrations/*.py')
    for migration_file in migration_py_files:
        if migration_file.is_file() and migration_file.stem != '__init__':
            migration_file.unlink(missing_ok=True)
            print(f'  Removing {migration_file}')


if __name__ == '__main__':
    try:
        app_name = sys.argv[1]
    except IndexError:
        print(f'Usage: {sys.argv[0]} <app_name>')
        sys.exit(1)
    main(app_name)
