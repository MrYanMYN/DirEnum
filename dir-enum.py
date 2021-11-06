import requests
import click
import time

def banner():
    click.echo("""
      ___  _       ___                
 |   \(_)_ _  | __|_ _ _  _ _ __  
 | |) | | '_| | _|| ' \ || | '  \ 
 |___/|_|_|   |___|_||_\_,_|_|_|_|
                                  
     """)
    click.echo("In case of an error please use the --help flag")

class Target():
    def __init__(self , target , subdomains):
        self.__target = target
        self.__subdomains = subdomains

    def get_subdomains(self):
        return self.__subdomains
    
    def get_domain(self):
        return self.__target

@click.command()
@click.option('--domain','-d', prompt="Enter the domain: " ,help='Enter a valid domain (without a subdomain)')
@click.option('--wordlist' ,'-w',prompt='Wordlist locaion: ' , help='enter the location of your preferred worlist')
@click.option('--verbose', '-v', help="Verbose mode", is_flag=False, show_default=False)
@click.version_option(version="0.1.0")

def program(domain, wordlist, verbose):
    results = []
    count = 0
    click.echo("Starting domain enumaration...")
    time.sleep(1)
    with open(wordlist , "r") as wl:
        for line in wl.readlines():
            word = line.strip("\n")
            try:
                req = requests.get(f'http://{domain}/{word}')
                if req.status_code == 200:
                    click.echo(f"Valid directory found {domain}/{word}")
                    results.append(f'http://{domain}/{word}')
                else:
                    pass
            except:
                pass
            if verbose:
                click.echo(f'Checking http://{domain}/{word}')
        click.echo("\n\nValid Directories found: \n-------------------------------")
        for item in results:
            click.echo(f'[{count}] Found valid: {item}')
            count += 1
        click.echo("""=========================
    Done
=========================""")

if __name__ == '__main__':
    banner()
    program()