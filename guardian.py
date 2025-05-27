# Lista blanca de IPs autorizadas
AUTORIZADOS = ["127.0.0.1", "::1"]

def verificar_acceso(ip):
    return ip in AUTORIZADOS
