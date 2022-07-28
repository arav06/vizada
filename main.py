from hashlib import sha256
from json import loads as jsonLoads

class Block:
      def __init__(self,data):

            self.data = data
            self.hash = sha256(self.data.encode()).hexdigest()

            dataList = self.data.split("-")
            self.fromPerson = dataList[0]
            self.toPerson = dataList[1]
            self.amount = dataList[2]
            self.previousHash = dataList[3]

            self.block_value = f'"From":"{self.fromPerson}","To":"{self.toPerson}","Amount":{self.amount},"Hash":"{self.hash}","Previous Hash":"{self.previousHash}"'
            self.block_value = "{"+self.block_value+"}," 

fromPerson = input("Who is making the transaction?\n")
toPerson = input(f"Who is {fromPerson} making the transaction to?\n")
amount = int(input(f"How many coins is {fromPerson} sending to {toPerson}?\n"))

blockchainRead = open("blockchain.json",'r')
previousHash = jsonLoads(blockchainRead.readlines()[len(blockchainRead.readlines())-1][:-2])["Hash"]
blockchainRead.close()

dataSet = f"{fromPerson}-{toPerson}-{amount}-{previousHash}"

block = Block(dataSet)

blockchainWrite = open("blockchain.json",'a')
blockchainWrite.write(f'{block.block_value}\n')
blockchainWrite.close()

blockValue = jsonLoads(block.block_value[:-1])

print(f"""
      \n
Your Block:
{{
      'From': '{blockValue["From"]}',
      'To': '{blockValue["To"]}',
      'Amount': {blockValue["Amount"]},
      'Hash': '{blockValue["Hash"]}',
      'Previous Hash': '{blockValue["Previous Hash"]}'
}}
""")
