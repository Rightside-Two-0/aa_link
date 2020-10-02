# @Author: two_0
# @Date:   02-10-2020
# @Email:  philip@two-0.org
# @Project: AA-Link
# @Last modified by:   two_0
# @Last modified time: 02-10-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
#     ___ __ ._`.*.'_._ ____ רףאל
#    . +  * .\   o.* `.`. +.  א .
#   *  .ת' '  \^/|  `. * .  * `
#             \V/ . +
#    יהוה      /_\  .`.
#   ======== _/W\_ =אדני:By: Two.0:.*
def personal_independence(income, ave_expenses):
    if type(income) == type('PASSIVE'):
        return income > ave_expenses
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%%md
#Data
#%%
class Data:
    def __init__(self, member, block_acc, block_acc_id, filename_):
        self.member = member
        self.block_account = block_acc
        self.block_account_id = block_acc_id
        self.content = self.get_bytes(filename_)
        self.size = self.get_bytes_size(filename_)
        self.signature = self.sign_data()

    def get_bytes(self, filename):
        with open(filename, 'rb') as file:
            return file.read()

    def get_bytes_size(self, filename):
        return len(self.get_bytes(filename))

    def to_dict(self):
        return OrderedDict({'author': self.author,
                  'block account': self.block_account,
                  'block ID': self.block_account_id,
                  'file': self.content,
                  'size': self.size,
                  'creator bonus': CREATOR_BONUS,
                  'student reward': STUDENT_REWARD
                  })

    @classmethod
    def is_valid(cls, filename):
       return filename.endswith('.ipynb')

    def sign_data(self):
        """
        Sign transaction with private key/account ID
        """
        private_key = RSA.importKey(binascii.unhexlify(self.block_account_id))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    def verify_data_signature(self, account, signature, content):
        """
        Check that the provided signature corresponds to the data
        signed by the public key/account (author)
        """
        public_key = RSA.importKey(binascii.unhexlify(account))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA.new(str(content).encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(signature))
#%%
