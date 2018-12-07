#!/usr/bin/env python
# coding: utf-8

# # Copy Image Across Accounts
# 
# 
# This is the python SDK equivalent of 
# ```
# az storage blob copy start --destination-blob --container --source-blob --source-container --source-account-name --source-account-key --account-name --account-key
# ```
# 
# This is dependent on the `azure-storage-blob` library:    
# ```
# pip install azure-storage-blob
# ```
# 
# This script copies over all blobs with the extension `.vhd`. This does not gurantee us all the vhd blobs, but there doesn't seem to be a better way ¯\\\_(ツ)\_/¯ blob.type isn't of any use here, since that gets us the blob storage type. 
# 

# In[1]:


from datetime import datetime, timedelta
from getpass import getpass
from pprint import pprint
from urllib.parse import quote, urlparse

from azure.storage.blob.baseblobservice import BaseBlobService
from azure.storage.blob.sharedaccesssignature import BlobSharedAccessSignature
from azure.storage.blob.models import BlobPermissions


# In[2]:


SAFE_CHARS = '/()$=\',~'

# this is Bizhang's account
SOURCE_PASSWORD = getpass(prompt="Password of source storage account")

# this is Brad's account
DEST_PASSWORD = getpass(prompt="Password of destination storage account")


# In[3]:


dest_client = BaseBlobService(account_name='bloooobs', 
                               account_key=DEST_PASSWORD)

source_client = BaseBlobService(account_name='cloudigradegroupdisks', 
                               account_key=SOURCE_PASSWORD)


# In[8]:


blobs = source_client.list_blobs(container_name='vhds')

#Create a shared access signature for the source container
expiry = (datetime.utcnow() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
sas = BlobSharedAccessSignature(account_name='cloudigradegroupdisks', 
                                account_key=SOURCE_PASSWORD)
source_sas = sas.generate_container(
    'vhds', 
    expiry=expiry, 
    protocol='https', 
    permission=BlobPermissions(read=True)
)


for blob in blobs:
    
    # if the blob is not a vhd, don't copy it.
    if not blob.name.endswith('vhd'):
        continue
    
    source_blob_url = source_client.make_blob_url(
        container_name='vhds', 
        blob_name=quote(blob.name, SAFE_CHARS), 
        sas_token=source_sas
    )
    
    dest_client.copy_blob(
        container_name='containerofblobs', 
        blob_name=blob.name, 
        copy_source=source_blob_url
    )  


# In[9]:


# Check the destination Account to make sure blobs are copied over

brads_blobs = dest_client.list_blobs(container_name='containerofblobs')
for blob in brads_blobs:
    pprint(blob.name)

