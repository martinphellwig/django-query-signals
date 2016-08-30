#! /usr/bin/env python
"""
Developer Reset.
"""
import os
APP = 'django_query_signals'
DIR = os.path.dirname(os.path.abspath(__file__))


def get_last_migration_file():
    "Fetch the latest migration file."
    _ = os.path.join(DIR, APP, 'migrations')

    _ = [os.path.join(_, item) for item in os.listdir(_) if not item.startswith('_')]
    _.sort()
    if len(_) > 0:
        return _[-1]
    else:
        return None

def modify_migration():
    "Modify migration, add pylint disable line."
    path = get_last_migration_file()
    if path is None:
        return
    text = '# pylint: disable=invalid-name, missing-docstring, line-too-long\n'
    with open(path, 'r+') as file_open:
        data = file_open.readlines()
        data.insert(1, text)
        file_open.seek(0)
        file_open.write(''.join(data))


def execute_shell(command, prefix='python manage.py', pipe=None):
    "Execute shell python manage.py"
    import subprocess
    cmd = prefix + ' ' + command
    if pipe is not None:
        cmd = pipe + ' | ' + cmd
    subprocess.call(cmd, shell=True)

def add_superuser(username, password):
    "Add superuser"
    from django.contrib.auth.models import User
    user = User(username=username)
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return user

def remove_db():
    "remove the db if it exists"
    _ = os.path.join(DIR, 'db.sqlite3')
    if os.path.exists(_):
        os.remove(_)

def remove_last_migration():
    "remove last migration file."
    _ = get_last_migration_file()
    if _ is not None:
        os.remove(_)

def add_migrations():
    "set up the new migrations and migrate"
    execute_shell('makemigrations ' + APP)
    execute_shell('makemigrations')
    execute_shell('migrate')
    modify_migration()

def main():
    "Executed when this is the interface module"
    remove_db()
    remove_last_migration()
    add_migrations()
    #
    # This will run a shell which imports this file as a module, this means
    # we can execute things in a Django environment.
    execute_shell('shell', pipe='echo "import devset"')
    #
    execute_shell('runserver')

def as_module():
    "Executed when this is imported."
    add_superuser('admin', 'admin')


if __name__ == '__main__':
    main()
else:
    as_module()

