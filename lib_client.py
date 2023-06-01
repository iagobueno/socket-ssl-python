import ssl

def createContext():
    """Cria um contexto SSL"""
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_cert_chain(certfile="./keys/client.crt", keyfile="./keys/client.key")
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    return context
