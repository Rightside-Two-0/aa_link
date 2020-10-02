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
#Transaction
#%%
from functools import reduce
class Transaction:
    def __init__(self, account_, account_id_, recipient_account_, amount_):
        self.account = account
        self.account_id = account_id_
        self.recipient_account = recipient_account_
        self.amount = amount_
        self.signature = self.sign_transaction()

    def to_dict(self):
        return OrderedDict({'sender account': self.account,
                'recipient account': self.recipient_account,
                'amount': self.amount})

    def sign_transaction(self):
        """
        Sign transaction with private key/account ID
        """
        private_key = RSA.importKey(binascii.unhexlify(self.account_id))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    def verify_transaction_signature(self, account, signature, transaction):
          """
          Check that the provided signature corresponds to the data
          signed by the public key/account (author)
          """
          public_key = RSA.importKey(binascii.unhexlify(account))
          verifier = PKCS1_v1_5.new(public_key)
          h = SHA.new(str(transaction).encode('utf8'))
          return verifier.verify(h, binascii.unhexlify(signature))
#%%
