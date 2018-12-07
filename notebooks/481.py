#!/usr/bin/env python
# coding: utf-8

# In[18]:


import os
from pprint import pprint
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient


# In[19]:


# Subscription id can be found at https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade
subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID') 

# Register an Application to get the client id: https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps
# Add a Key to the registered App to get the CLIENT_SECRET
# Tenant id is the same as the directory id, and can be found in the AD->properties page
# Where the heck to I configure rbac for this application?
# OK, shortcut, there is a cli commmand that will create an application and configure RBAC:
# az ad sp create-for-rbac
# I can't find where applications are on the UI, but this does work... 
credentials = ServicePrincipalCredentials(
    client_id=os.environ['AZURE_CLIENT_ID'],
    secret=os.environ['AZURE_CLIENT_SECRET'],
    tenant=os.environ['AZURE_TENANT_ID']
)

resource_client = ResourceManagementClient(credentials, subscription_id)
compute_client = ComputeManagementClient(credentials, subscription_id)


# In[26]:


# resource_client.resources does not include resource group info 
# which we need to get to the vm, so we have to start by getting all the groups
for groups in resource_client.resource_groups.list(): 

    resources = resource_client.resources.list_by_resource_group(groups.name)
    for resource in resources:
        if resource.type.startswith("Microsoft.Compute/virtualMachines"):
        # The only way to get the status of the VM is by looking at the instance View :(
        # and the only way to see the instance view is by looking at the vms 1 by 1, instead of 
        # calling vm.list_all() or vm.list()
            vm = compute_client.virtual_machines.get(
                resource_group_name=groups.name,
                vm_name=resource.name, expand='instanceView')
            
            for status in vm.instance_view.statuses:
                if status.code == "PowerState/running":
                    print("{} is running!".format(resource.name))    


# In[ ]:




