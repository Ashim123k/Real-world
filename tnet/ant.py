import click
#from functions import eigrphack
print( """.----------------.  .-----------------. .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || | ____  _____  | || |  _________   | || |  _________   | |
| | |  _   _  |  | || ||_   \|_   _| | || | |_   ___  |  | || | |  _   _  |  | |
| | |_/ | | \_|  | || |  |   \ | |   | || |   | |_  \_|  | || | |_/ | | \_|  | |
| |     | |      | || |  | |\ \| |   | || |   |  _|  _   | || |     | |      | |
| |    _| |_     | || | _| |_\   |_  | || |  _| |___/ |  | || |    _| |_     | |
| |   |_____|    | || ||_____|\____| | || | |_________|  | || |   |_____|    | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' """)
@click.group()
def ant():
   pass
   
@ant.command()
def ipscanner():
   """provides ui to the user"""
   import functions
   from functions import IP_scanner
     
@ant.command()
@click.option('-ip',help='Ip of Gateway to show neighborship',required=True)
def scan(ip):
    """Show network neighborship"""
    from functions import network_scanner
    a=network_scanner.Scan(ip)
    print(network_scanner.print_result(network_scanner.Scan(ip)))
     
@ant.command()
def gui():
   """provides ui to the user"""
   import functions
   from functions import GUI
   
@ant.command()
@click.option('-ip',help="IP of eigrp neighbor",required=True)
def eigrp(ip):
   """This allows user to break eigrp neighborship in the network"""
   from functions import eigrphack
   a=eigrphack.eigrp(ip)

@ant.command()
@click.option('-ip',help="IP of router to dos",required=True)
def eigrp_dos(ip):
   """This allows user to ddos eigrp network"""
   from functions import DDOS_eigrp
   a=DDOS_eigrp.ddos(ip)   

@ant.command()
@click.option('-ip',help="IP of router to dos",required=True)
def rip_dos(ip):
   """This allows user to ddos rip network"""
   from functions import rip
   a=rip.rip_ddos(ip)   
 
@ant.command()
@click.option('-ip',help="IP of router to dos",required=True)
def pod(ip):
   """Automates ICMP Flood"""
   import functions
   from functions import POD
   a=POD.pod(ip)
  

    



   
    