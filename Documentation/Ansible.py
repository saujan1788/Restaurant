def SSH_Issues:
    Use terraform to pair the keys to the instances and then once that's done the keys are added' after that on the inventory file mention the absolute path to the key. and on iventory define the name as well. Test SSH this should work. Note : Perms should be good.


def K8s:
    Clone the repo of kube_spray 

    1) Move to 2.23.0, git checkout tags/v2.23.0

    2) Create a python venv, python3 -m venv kubespray-venc
    3) Activate and install the requirements tag, source kubespray-venv/bin/activate
    4) Copy the sample inventory to new inventory , cp -rfp /inventory/sample inventory/k8slab
    5) Decalre an array of variables of IP declare -a IPS = (private Ips of the machines , give space )
    6) Run an invenotry python script which outputs the host yaml and takes our decalred Ips variable , CONFIG_FILE = invetory/proxmo01/hosts.yaml python3 contrib/inventory_builder/inventory.py ${IPS[@]}
    7) After this all nodes will be added to the invetory , In the hosts files inside inventory change the name of the nodes
    8) Create a cluster-variabl.yaml file to hold variable, Define a specific kube_version in the yaml file , kube_version: v1.27.5 , helm_enable: true, kube_proxy_mode: iptables, By default kubespray uses ipvs which is not installed by default on the nodes, 
    9) When running the play book ensure to pass, the private key and the username use to ssh to the nodes
    10) sudo cat /etc/kubernetes/admin.conf, Copy this file to the master server, create a kubeconfig file and replca the server id in the file to the ip of the master

def Shutdown:
    Noticed that only the public IP gets changed after shutdown , The internal IPs stayed the same simplifying the restart and shutdwon process 

def IncreaseEBS:
    Created a playbook to recliam the added disk , changed from 8 to 15GB on all instances.
