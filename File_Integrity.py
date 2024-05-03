import hashlib  #To create hash's 
import os # to interact with operating system
from pathlib import Path 
storage_file = 'C:/Users/JoseM/Security/security_storage/hash_database.txt' 

def store_string(string, data_store ):          # this is defining a function. This is useful because file hash and storage file can change. 
        with open( data_store, 'w') as post_hash_storage:  # the 'w' is for write, if you want to append change to 'a'. This line opens the file in (write) mode            
            post_hash_storage.write(str(string)) 

def check_for_hash(database_path, target_string):
        with open(database_path, 'r') as db:
            for line in db:
                if target_string in line:
                    return True
            return False


while True:
    query = input("For file hashing, type hash. To check your file against the records, type check. If you want to exit, type exit")
    if query == "hash":
        break
    elif query == "check":
        break      
    elif query == "exit":
        exit()
    else:
        print("Invalid input. Please try again")    


file_path = Path(input("Enter the path of the file in question"))
if not file_path.is_file():
    print(f"The file {file_path} does not exist.")
else:
    with open(file_path, 'rb') as f:
        file_data = f.read()
        hash_object = hashlib.sha256()
        hash_object.update(file_data)
        file_hash = hash_object.hexdigest()
print(f"Your hash is {file_hash}")

request = input("Would you like to store the hash, or check it against the database")
if request == "store": 
    store_string(file_hash, storage_file)    #calls the function. store_string(<string>, <filepath of file you want string in>)
    print("Your hash has been stored in hash_database.txt")
elif request == "check":
    result = check_for_hash(storage_file, file_hash)
    if result:
        print("Your file's integrity is intact")
    else:
        print("Your file has been compromised")           

else:
    print("Invalid input")
    exit()

    


         

