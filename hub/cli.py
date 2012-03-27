"""
hub

this file contains all the helper cli commands for hub

"""
import sys

from pbs import git
from clint import args
from clint.textui import colored, puts, indent

#username  =
#password =

def get_help():
    puts('How to hub:')
    with indent(4):
        puts(colored.cyan('hub create <repo>'))
        puts(colored.cyan('hub delete <repo>'))
        puts(colored.cyan('hub pull <repo>'))

def version():
    puts('development 0.0.1')

def git_status():
    print git.status()

def get_issues():
    pass

def show_boating():
    puts('{0} by Mahdi Yusuf <@myusuf3>'.format(colored.yellow('hub')))
    puts('{0} http://github.com/myusuf3/hub'.format(colored.yellow('source')))


def begin():
    if args.flags.contains(('--version', '-v')):
        version()
        sys.exit(0)

    elif args.get(0) == None:
        show_boating()

    elif args.get(0) == 'status':
        git_status()
        sys.exit(0)

    elif args.flags.contains(('--help', '-h')):
        get_help()
        sys.exit(0)

    elif args.flags.contains('--issues', '-i', 'issues'):
        get_issues()
