# @Author: two_0
# @Date:   02-10-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
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
#Blockchain
#%%
from urllib.parse import urlparse
class Blockchain:
    def __init__(self, node_id_):
        self.__data_content = []
        self.__open_transactions = []
        self.__chain = []
        self.__nodes = set()
        self.node_id = node_id_
        self.account = self.get_account()
        #load blockchain
        # self.load_chain()
        self.resolve_conflicts = False

    @property
    def open_transactions(self):
        return self.__open_transactions

    @open_transactions.setter
    def open_transactions(self, val):
        self.__open_transactions = val

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, val):
        self.__nodes = val

    @property
    def data_content(self):
        return self.__data_content[:]

    @data_content.setter
    def course_content(self, val):
        self.__data_content = val

    @property
    def chain(self):
        return self.__chain[:]

    @chain.setter
    def chain(self, val):
        self.__chain = val

    def get_account(self):
        if len(self.__chain) == 0:
            #create account
            return Account()

    def register_node(self, node_url):
        """
        Add a new node to the list of nodes
        """
        #Checking node_url has valid format
        parsed_url = urlparse(node_url)
        if parsed_url.netloc:
            self.__nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')

    def submit_transaction(self, sender_account, transaction, signature):
        """
        Add a transaction to open_transactions list if the signature verified
        """
        if transaction.verify_transaction_signature(sender_account, signature, transaction.to_dict()):
            self.__open_transactions.append(transaction)

    def sumbit_content(self, creator_account, _content, _signature):
        """
        Add a data object to the list of course_content if signature is verified
        """
        if _content.verify_data_signature(creator_account, _signature, _content.to_dict()):
            if not _content in self.__data_content:
                #only 1 course per account per block
                self.__data_content.append(_content)
        else:
            return 'INVALID SIGNATURE'

    def submit_student(self, student_account, student_score, student_signature):
        pass
#%%
