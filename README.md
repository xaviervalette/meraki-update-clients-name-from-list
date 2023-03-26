# Meraki update clients name from list

## What is it ?
Python script to update the clients name of devices displayed on the ```Network-wide``` > ```Clients```

<p align="center">
<img width="898" alt="image" src="https://user-images.githubusercontent.com/28600326/227801958-494c3566-735c-440a-9f7a-dcd76bb2061f.png">
</p>

## Prerequisites
- Meraki Dashboard access
- Meraki API key
- Meraki network ID

## Get started
1. Clone or download this repo
```console
git clone https://github.com/xaviervalette/meraki-update-clients-name-from-list

```
2. Install required packages
```console
python3 -m pip install -r requirements.txt
```
3. Add a ```config.yml``` file as follow:
```diff
└── meraki-update-l7-firewall-rules/
+   ├── config.yml
    ├── requirements.txt
    └── src/
         └── main.py  
```
4. In the ```config.yml``` file, add the following variables:
```yaml
#config.yml
---
apiKey: "<yourApiKey>"
networkId: "<yourNetworkId1>"
clients:
  - mac: "<firstClientMac>"
    name: "<firstClientName>"
  - mac: "<secondClientMac>"
    name: "<secondClientName>"
    
[...]

  - mac: "<lastClientMac>"
    name: "<lastClientName>"
    
...

```
> ⚠ The script will work even if the MAC is not in the given network clients page



5. Now you can run the code by using the following command:
```console
python3 src/main.py
```

## Output
The output should be as followed:
```console
Request status code : 201 
```




