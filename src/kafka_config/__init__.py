
import os

SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
API_KEY = "OBA7HQK2ISLI5WAS"
ENDPOINT_SCHEMA_URL  = "https://psrc-10dzz.ap-southeast-2.aws.confluent.cloud"
API_SECRET_KEY = "vOo6yS8J/i5jILiL+bxldZbCZJAL57QJcTI9YTlleKhST0Wigpqgl4Sm04dD7Wbu"
BOOTSTRAP_SERVER = "pkc-l7pr2.ap-south-1.aws.confluent.cloud:9092"
#WSECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
#SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SCHEMA_REGISTRY_API_KEY = "PICMAKJPVOCLEPY7"
SCHEMA_REGISTRY_API_SECRET = "K0KxDZBv+FaOz43ZIhpSNMVMKVa3BBTqATVCPf4TAFsbrk8UMxfydT6hKm1JvgmS"


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

