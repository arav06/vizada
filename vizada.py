from sys import argv
from os import path,getcwd,remove,listdir
from json import loads,dumps
from hashlib import sha256

try:
      dbName = argv[1]
except:
      print("Specify the relative path of your database: python3 vizada.py <DATABASE NAME>\nDont have a database? Run setup.py to get started!")
      exit()
dbName = argv[1]
dbPath = f"{getcwd()}/{dbName}"

if not path.exists(dbPath):
      print(f"{dbName} was not found in the current working directory :(")
      exit()

print(f"""
▀█ █▀  ▀  ▀▀█ █▀▀█ █▀▀▄ █▀▀█ 
 █▄█  ▀█▀ ▄▀  █▄▄█ █  █ █▄▄█ 
  ▀   ▀▀▀ ▀▀▀ ▀  ▀ ▀▀▀  ▀  ▀

Welcome!
""")
while True:
      try:
            command = input("> ")
            commandList = command.split(" ")

            if commandList[0].lower() == "help":
                  print("""
                  
                  """)
            elif commandList[0].lower() == "ct" or commandList[0].lower() == "createtable":
                  try:
                        tableName = commandList[1]
                  except:
                        print("[+] Specify a table name \n[+] ct tableName or createtable tableName")
                        continue
                  tableName = commandList[1]
                  if tableName.isspace() or tableName == "":
                        print("[+] Table name cannot be empty \n[+] ct tableName or createtable tableName")
                        continue
                  if path.exists(f"{dbPath}/{tableName}.json"):
                        print("[+] Table already exists")
                        continue
                  with open(f"{dbPath}/{tableName}.json", 'w') as newTable:
                        newTable.write(f'{{"starting":true,"toBeDeleted":false,"Hash":"{sha256(tableName.encode()).hexdigest()}"}}\n')
                  print(f"[+] '{tableName}' table has been created")

            elif commandList[0].lower() == "dt" or commandList[0].lower() == "deletetable":
                  try:
                        tableName = commandList[1]
                  except:
                        print("[+] Specify a table name \n[+] dt tableName or deletetable tableName")
                        continue
                  tableName = commandList[1]
                  if tableName.isspace() or tableName == "":
                        print("[+] Table name cannot be empty \n[+] dt tableName or deletetable tableName")
                        continue
                  if not path.exists(f"{dbPath}/{tableName}.json"):
                        print("[+] Table does not exist")
                        continue
                  remove(f"{dbPath}/{tableName}.json")
                  print(f"[+] '{tableName}' table has been deleted")
            
            elif commandList[0].lower() == "vt" or commandList[0].lower() == "viewtable":
                  try:
                        tableName = commandList[1]
                  except:
                        print("[+] Specify a table name \n[+] vt tableName or viewtable tableName")
                        continue
                  tableName = commandList[1]
                  if tableName.isspace() or tableName == "":
                        print("[+] Table name cannot be empty \n[+] vt tableName or viewtable tableName")
                        continue
                  if not path.exists(f"{dbPath}/{tableName}.json"):
                        print("[+] Table does not exist")
                        continue
                  table = open(f"{dbPath}/{tableName}.json",'r')
                  tableLines = table.readlines()
                  del tableLines[0]
                  for line in tableLines:
                        line = loads(line)
                        del line["Hash"]
                        try:
                              del line["Previous Hash"]
                        except:
                              pass
                        print(line)
                  table.close()

            elif commandList[0].lower() == "lt" or commandList[0].lower() == "list" or commandList[0].lower() == "ls" or commandList[0].lower() == "listtables":
                  dirsLst = listdir(dbPath)
                  for d in dirsLst:
                        print(d.replace(d[len(d) - 5:],""))

            elif commandList[0].lower() == "id" or commandList[0].lower() == "insertdata":
                  try:
                        tableName = commandList[1]
                  except:
                        print("[+] Specify a table name \n[+] id tableName or insertdata tableName")
                        continue
                  tableName = commandList[1]
                  if tableName.isspace() or tableName == "":
                        print("[+] Table name cannot be empty \n[+] id tableName or insertdata tableName")
                        continue
                  if not path.exists(f"{dbPath}/{tableName}.json"):
                        print("[+] Table does not exist")
                        continue
                  
                  print("[+] Enter your JSON data")
                  data = input(f"{tableName}> ")
                  try:
                        jsonData = loads(data)
                  except:
                        print("[+] Data is not in JSON format")
                        continue

                  blockchainRead = open(f"{dbPath}/{tableName}.json",'r')
                  previousHash = loads(blockchainRead.readlines()[len(blockchainRead.readlines())-1])["Hash"]
                  blockchainRead.close()

                  jsonData = loads(data)
                  jsonData.update({"Previous Hash":previousHash})
                  
                  strData = dumps(jsonData)

                  strHash = sha256(strData.encode()).hexdigest()

                  jsonData.update({"Hash":strHash})

                  tableData = dumps(jsonData)

                  table = open(f"{dbPath}/{tableName}.json",'a')
                  table.write(f"{tableData}\n")
                  table.close()
            
            elif commandList[0].lower() == "exit" or commandList[0].lower() == "bye":
                  exit()
            elif commandList[0] == "":
                  continue
            else:
                  print("[+] Unrecognized command :(")
      except KeyboardInterrupt:
            print("")
