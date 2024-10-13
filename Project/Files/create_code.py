import random
import hashlib
import base64
import xor

def create_code(filename):
    # Generate the sha256 hash of a radnom number
    random_number = random.randint(0, 1000000)
    random_string = str(random_number).encode('utf-8')
    hashed_number = hashlib.sha256(random_string).hexdigest()

    #Generate the md5 hash of the sha256 hash
    hashed_number_md5 = hashed_number.encode('utf-8')
    hashed_number_md5 = hashlib.md5(hashed_number_md5).hexdigest()

    #Generate the hash of the filename
    filename_string = filename.encode('utf-8')
    hashed_filename = hashlib.sha256(filename_string).hexdigest()

    #XOR encrypt the hashed_filename with the hashed_number_md5
    encrypted_hashed_filename = ''.join(chr(ord(hf) ^ ord(hm)) for hf, hm in zip(hashed_filename, hashed_number_md5))

    #Make it readable in base64
    encrypted_hashed_filename = base64.b64encode(encrypted_hashed_filename.encode('utf-8')).decode().lower().replace("=", "")

    return encrypted_hashed_filename
