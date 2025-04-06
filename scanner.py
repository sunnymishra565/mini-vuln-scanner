import socket

def clean_target_url(url):
    url = url.strip()
    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]
    if url.endswith("/"):
        url = url[:-1]
    return url

def port_scanner(target, ports):
    print(f"Scanning {target} for open ports...\n")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[+] Port {port} is open")
            s.close()
        except:
            pass

if __name__ == "__main__":
    target = input("Enter Target IP/Domain: ")
    cleaned_target = clean_target_url(target)
    ports = [21, 22, 23, 80, 443, 8080, 3306, 3389]
    port_scanner(cleaned_target, ports)
