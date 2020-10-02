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
#Block
#%%
class Block:
    def __init__(self, prev_hash, content, transactions_):
        self.previous_hash = prev_hash
        self.data = content
        self.transactions = transactions_
        self.timestamp = time.time()
        self.hash = self.fingerprint()

    def fingerprint(self):
        """
        Create a SHA-256 hash of a block
        """
        block_string = (str(self.previous_hash)+str(self.data)+str(self.transactions)+str(self.timestamp)).encode()
        return hashlib.sha256(block_string).hexdigest()
#%%
