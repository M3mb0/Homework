import sys
import pathlib
import logging
from exceptions import ArgvException, NotTextFile, CrypterBaseException
from crypter import Caesar, Shift


def get_file_text(path):
    """Get the file from a text file"""
    with open(path) as fin:
        content = fin.read()
    return content


ROOT = pathlib.Path(__file__).parent
LOGS_DIR = ROOT / "logs"

try:
    LOGS_DIR.mkdir(exist_ok=True)
except OSError:
    logs_file_name = None
else:
    logs_file_name = LOGS_DIR / "log.log"

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s line:  %(lineno)d %(message)s",
                    filename=logs_file_name)


def get_path_from_argv(idx):
    """Get path from CLI using sys module and is taking 1 argument which is the index"""
    if len(sys.argv) == 1:
        raise ArgvException("Error: Argumentul Path nu a fost gasit")

    path = pathlib.Path(sys.argv[idx])
    if not path.is_file():
        raise NotTextFile(f"Error: Nu am gasit fisierul {sys.argv[idx]}")
    return path


def crypt(msg, cypher):
    """Returns a string with the encrypted message and takes 2 arguments"""
    return str(cypher.crypt(msg))


def write_crypt_msg(path, msg, cipher):
    """Writes the encrypted message in a file text and takes 3 arguments"""
    with open(path, "w") as f:
        crypt_mes = f.write(crypt(msg, cipher))
    return crypt_mes


"""----------------------------------------------------------------------------------------------------------------"""


def decrypt(msg, cypher):
    """Returns a string with the decrypted message and takes 2 arguments"""
    return str(cypher.decrypt(msg))


def write_decrypt_msg(path, msg, cipher):
    """Writes the decrypted message in a file text and takes 3 arguments"""
    with open(path, "w") as f:
        decrypt_mes = f.write(decrypt(msg, cipher))
    return decrypt_mes


main_msg = get_file_text("my_text.txt")
my_cypher = Caesar(3)
my_cypher2 = Shift(5)
crypt_msg = get_file_text("encrypted.txt")

if sys.argv[1] == "c":
    try:
        logging.info(f"The file {get_path_from_argv(2)} will be encrypted")
        encrypted_msg = "encrypted.txt"
    except OSError:
        encrypted_msg = None
    except CrypterBaseException as err:
        logging.error(err)
    else:
        write_crypt_msg(encrypted_msg, main_msg, my_cypher2)
        logging.info(f"In {encrypted_msg} file you will find the encrypted message")

elif sys.argv[1] == "d":
    try:
        logging.info(f"The file {get_path_from_argv(2)} will be decrypted")
        decrypted_msg = "decrypted.txt"
    except OSError:
        decrypted_msg = None
    except CrypterBaseException as err:
        logging.error(err)
    else:
        if crypt_msg.split()[0] == 'Shift':
            write_decrypt_msg(decrypted_msg, crypt_msg, my_cypher2)
            logging.info(f"In {decrypted_msg} file you will find the decrypted message")
        elif crypt_msg.split()[0] == 'Caesar':
            write_decrypt_msg(decrypted_msg, crypt_msg, my_cypher)
            logging.info(f"In {decrypted_msg} file you will find the decrypted message")
        else:
            logging.info("Message cannot be decrypted")
else:
    raise NotTextFile("Command dose not exist")
