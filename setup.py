from os import mkdir,getcwd
from hashlib import sha256

print("""

▀█ █▀  ▀  ▀▀█ █▀▀█ █▀▀▄ █▀▀█ 
 █▄█  ▀█▀ ▄▀  █▄▄█ █  █ █▄▄█ 
  ▀   ▀▀▀ ▀▀▀ ▀  ▀ ▀▀▀  ▀  ▀

- By Arav Budhiraja
""")

print("\nEnter the name of your database")
dbName = input("> ")
print(f"\nCreating '{dbName}' database")
mkdir(dbName)
print(f"\n{dbName} has been created!\nYou can access the database by executing python3 blockchain.py {dbName}")
