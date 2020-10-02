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
#Mining Reward
#%%
UNIT = 1
COURSE_REWARD = UNIT*100
STUDENT_REWARD = UNIT*10
CREATOR_BONUS = UNIT
#%%md
#Accounts instead of Wallets
#%%
#Imports
from collections import OrderedDict
import binascii
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import requests, time, hashlib
#%%
class Account:
    def __init__(self):
        random_gen = Crypto.Random.new().read
        private_key = RSA.generate(1024, random_gen)
        public_key = private_key.publickey()
        self.__id = binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
        self.account = binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
    @property
    def id(self):
        return self.__id
#%%
