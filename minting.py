from ravenrpc import Ravencoin
import time
import ipfshttpclient

rpcuser=<rpcusername>
rpcpassword=<rpcpassword>
rvn = Ravencoin(rpcuser, rpcpassword)

new = []
new_hash = []
a_range = range(1, 5000)

for index in a_range:
    client = ipfshttpclient.connect('/dns4/ipfs.infura.io/tcp/5001/https', auth=(
            <PROJECT ID>, <PROJECT SECRET>))
    numbers = str(index)
    res = client.add(<FILE LOCATION> + numbers + '.png')
    new.append(res)


for index in range(len(new)):
    apes = str(new[index])
    gorilla = apes[72:118]
    new_hash.append(apes)

banana = []
banana1 = []
banana2 = []
banana3 = []
data1 = {}

for t3 in a_range:
    banana.append({"name": f'0{t3}'})

for t2 in range(len(new_hash)):
    banana1.append({"IPFS": new_hash[t2]})

for t4 in range(len(new_hash)):
    banana2 = [banana[t4], banana[t4]]
    banana3.append(banana2)
    data1[t4] = banana3[t4]


for i in data1:
    rvn.walletpassphrase(<walletpassword>, 100)
    info = data1[i]
    name = info[0]["name"]
    IPFS = info[1]["IPFS"]
    root_name = "BILLION_APE_CLUB"
    unique_asset = rvn.issueunique(root_name, [name], [IPFS])
    print(unique_asset)

time.sleep(300)

data2 = {}

for s1 in a_range:
    data2[f'BILLION_APE_CLUB#0{s1}'] = 1

for t in data2:
    rvn.walletpassphrase(<password>, 100)
    wallet = <wallet address>
    asset_sent = rvn.transfer(t, '1', wallet)
    print(asset_sent)
