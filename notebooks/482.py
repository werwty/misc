#!/usr/bin/env python
# coding: utf-8

# In[109]:


import os

from urllib.parse import urlparse

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient


# In[87]:


subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID') 
credentials = ServicePrincipalCredentials(
    client_id=os.environ['AZURE_CLIENT_ID'],
    secret=os.environ['AZURE_CLIENT_SECRET'],
    tenant=os.environ['AZURE_TENANT_ID']
)
compute_client = ComputeManagementClient(credentials, subscription_id)


# In[120]:


for image in compute_client.images.list():
    print(image)
    print("Image: {}".format(image.name))
    print("Image Tags: {}".format(str(image.tags)))    
    print("Image Owner Subscription ID: {}".format(image.id.split("/")[2]))    
    print("Detected OS: {}".format(image.storage_profile.os_disk.os_type.name))


# In[ ]:




