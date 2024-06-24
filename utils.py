from prefect.blocks.system import Secret
import re


def get_credentials(str_credential_name):
    block_str = Secret.load(str_credential_name).get()
    id_pattern = r"(?<=id:).+(?=\|)"
    password_pattern = r"(?<=password:).+(?=$)"

    user_id = re.search(pattern=id_pattern, string=block_str).group()
    user_password = re.search(pattern=password_pattern, string=block_str).group()
    return user_id, user_password
