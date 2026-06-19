import socket

print("Welcome to Vulnerability Scanner")

target = input("Enter IP address or website: ")

ports = [21,22,23,25,53,80,110,143,443,3306]

services = {
    21:"FTP",
    22:"SSH",
    23:"Telnet",
    25:"SMTP",
    53:"DNS",
    80:"HTTP",
    110:"POP3",
    143:"IMAP",
    443:"HTTPS",
    3306:"MySQL"
}

open_ports = []
vulnerabilities = []

print("\nScanning...\n")

for port in ports:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(1)

    result = sock.connect_ex((target,port))

    if result == 0:

        print("Port",port,"OPEN")

        open_ports.append(port)

    sock.close()

print("\nServices Found\n")

for port in open_ports:

    if port in services:
        print(port,"-",services[port])

for port in open_ports:

    if port == 21:
        vulnerabilities.append(
            "FTP detected - unencrypted communication"
        )

    elif port == 23:
        vulnerabilities.append(
            "Telnet detected - insecure protocol"
        )

    elif port == 3306:
        vulnerabilities.append(
            "MySQL database exposed publicly"
        )

risk = "Low"

if len(vulnerabilities) >= 3:
    risk = "High"

elif len(vulnerabilities) >= 1:
    risk = "Medium"

print("\nRisk Level:",risk)

file = open("report.txt","w")

file.write("VULNERABILITY REPORT\n")
file.write("====================\n\n")

file.write("Target: "+target+"\n\n")

file.write("Open Ports\n")

for port in open_ports:
    file.write(str(port)+" - "+services.get(port,"Unknown")+"\n")

file.write("\nVulnerabilities\n")

for item in vulnerabilities:
    file.write(item+"\n")

file.write("\nRisk Level: "+risk)

file.close()

print("\nReport saved as report.txt")
