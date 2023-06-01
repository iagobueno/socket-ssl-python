import ssl

def createContext():
    """Cria um contexto SSL"""
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="./keys/server.crt", keyfile="./keys/server.key")
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    return context
