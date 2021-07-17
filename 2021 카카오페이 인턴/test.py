from cryptography.fernet import Fernet  # symmetric encryption
import json



# 암복호화 클래스
class SimpleEnDecrypt:
    def __init__(self, key=None):
        if key is None:  # 키가 없다면
            key = Fernet.generate_key()  # 키를 생성한다
        self.key = key
        self.f = Fernet(self.key)

    # Encryption Function
    def encrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):
            ou = self.f.encrypt(data)  # 바이트형태이면 바로 암호화
        else:
            ou = self.f.encrypt(data.encode('utf-8'))  # 인코딩 후 암호화
        if is_out_string is True:
            return ou.decode('utf-8')  # 출력이 문자열이면 디코딩 후 반환
        else:
            return ou

     # Decryption Funtion
    def decrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):
            ou = self.f.decrypt(data)  # 바이트형태이면 바로 복호화
        else:
            ou = self.f.decrypt(data.encode('utf-8'))  # 인코딩 후 복호화
        if is_out_string is True:
            return ou.decode('utf-8')  # 출력이 문자열이면 디코딩 후 반환
        else:
            return ou

# 블록 정보 클래스
class Block(): # index, timestamp, channel_name, sensor_val, service_val
    def __init__(self, index, timestamp, channel_name, sensor_val, service_val):
        self.channel_name = channel_name
        self.index = index
        self.satisfaction = ""
        self.previous_block_id = ""
        self.current_block_id = self.calHash(timestamp, index)
        self.timestamp = timestamp
        self.sensor_val = sensor_val
        self.service_val = service_val
        self.runtime = ""


    # 블록 ID 해시 생성
    def calHash(self, timestamp, index):
        simpleEnDecrypt = SimpleEnDecrypt()
        message = timestamp + str(index)
        return simpleEnDecrypt.encrypt(message)

# 블록체인에서의 블록 생성 클래스
class BlockChain:
    def __init__(self):
        self.chain = []
        self.createGenesis()

    def createGenesis(self):
        self.chain.append(Block(0, "", "", "", ""))


    def addBlock(self, nBlock):  # Block Add method
        nBlock.previous_block_id = self.chain[len(self.chain) - 1].current_block_id
        nBlock.current_block_id = nBlock.calHash(nBlock.timestamp, nBlock.index)
        self.chain.append(nBlock)

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def isValid(self):
        i = 1
        while (i < len(self.chain)):
            if (self.chain[i].current_block_id != self.chain[i].calHash()):
                return False
            if (self.chain[i].previous_block_id != self.chain[i - 1].hash):
                return False
            i += 1
        return True

block = BlockChain()

# Body에서 받아야하는 정보들
req_timestamp = 'time'
req_channel_name ='12343'
req_sensor_val = 'sensor_val'
req_service_val ='service_val'

block.addBlock(Block(len(block.chain), req_timestamp, req_channel_name, req_sensor_val, req_service_val))

# Body에서 받아야하는 정보들
req_timestamp = 'time'
req_channel_name ='12343'
req_sensor_val = 'sensor_val'
req_service_val ='service_val'


# 마지막 블록
for recent_block in block.chain:
    continue

print(json.dumps(vars(recent_block)))



