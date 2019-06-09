import hashlib, codecs

#calculates the target difficulty
def targetCalculator(bits):
    exponent = str(bits)[:2]
    coefficient = str(bits)[2:]

    target = int(coefficient, 16) * 256 ** (int(exponent, 16) - 3)
    return target

#does endian conversion
def endianConverter(value):
    return codecs.encode((codecs.decode(value, 'hex')[::-1]), 'hex').decode()

def miner(version, prevBlockHash, merkleRoot, time, bits, nonce):

    target = targetCalculator(bits)
    #decimal arguments are first represented in hexadecimal
    version = version.split('x')[-1]
    time = hex(time).split('x')[-1]
    nonce = hex(nonce).split('x')[-1]
    bits = hex(bits).split('x')[-1]

    #arguments are converted from big to little endian
    version = endianConverter(version)
    merkleRoot = endianConverter(merkleRoot)
    prevBlockHash = endianConverter(prevBlockHash)
    time = endianConverter(time)
    bits = endianConverter(bits)
    nonce = endianConverter(nonce)

    #the six arguments are concatenated in order
    #a change in order would change the hash
    header = version + str(prevBlockHash) + str(merkleRoot) + time + bits + nonce

    #it is represented in bytes
    #the hash function takes its arguments in bytes
    headerByte = codecs.decode(header, 'hex')

    #double hashed with SHA256
    headerHash = hashlib.sha256(hashlib.sha256(headerByte).digest()).digest()

    #represented in hexadecimal and big endian
    headerHash = codecs.encode(headerHash[::-1], 'hex').decode()


    print(headerHash)
    print(int(headerHash, 16) < target)

#Block 502871 data
#version number, merkle root and previous block hash are
#entered as string because of python's limited data type
miner('0x20000000', "00000000000000000061abcd4f51d81ddba5498cff67fed44b287de0990b7266",
                      "871148c57dad60c0cde483233b099daa3e6492a91c13b337a5413a4c4f842978",
                                          1305998791, 402690497, 2504433986 )