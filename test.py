data = {
    "nodes": [
        {"name": "node1",
         "cpu_cap": 2,
         "mem_cap": 4},
        {"name": "node2",
         "cpu_cap": 8,
         "mem_cap": 16},
    ],
    "pods": [
        {"name": "pod1",
         "cpu_cap": 1,
         "mem_cap": 2},
        {"name": "pod2",
         "cpu_cap": 2,
         "mem_cap": 8},
        {"name": "pod3",
         "cpu_cap": 2,
         "mem_cap": 8},
        {"name": "pod4",
         "cpu_cap": 1,
         "mem_cap": 1},
    ]
}

check = 0
cntPod = len(data["pods"])
res = dict()

for i, node in enumerate(data["nodes"]):  # O(n)
    nName = node["name"]
    nCpu = node["cpu_cap"]
    nMem = node["mem_cap"]
    while nCpu != 0 and nMem != 0:
        for j, pod in enumerate(data['pods']):  # O(m)
            pName = pod["name"]
            pCpu = pod["cpu_cap"]
            pMem = pod["mem_cap"]
            if nCpu - pCpu >= 0 and nMem - pMem >= 0 and pCpu != 0 and pMem != 0:
                nCpu -= pCpu
                nMem -= pMem
                res[pName] = nName
                data['pods'][j]["cpu_cap"] = 0
                data['pods'][j]["mem_cap"] = 0
print(res)

# while check < cntPod:
#     curInd = 0
#     pod = data["pods"][0]
#     pName, pCpu, pMem = pod["name"], pod["cpu_cap"], pod["mem_cap"]
#
#     node = data["nodes"][0]
#     nName, nCpu, nMem = node["name"], node["cpu_cap"], node["mem_cap"]
#
#     print('pods:', data["pods"])
#     print('node:', data["nodes"])
#     print()
#     if nCpu - pCpu >= 0 and nMem - pMem >= 0:
#         data["nodes"][0]["cpu_cap"] -= pCpu
#         data["nodes"][0]["mem_cap"] -= pMem
#         data["pods"].pop(0)
#         res[pName] = nName
#         cntPod += 1
#
#         if data["nodes"][0]["cpu_cap"] <= 0 or data["nodes"][0]["mem_cap"] <= 0:
#             data['nodes'].pop(0)
#
#     else:
#         data["pods"].append(data["pods"].pop(0))
#
#     print('pod:', pod)
#     print('node:', node)
#     print()
#     print('pods:', data["pods"])
#     print('node:', data["nodes"])
#     print()
#     print('res:', res)
#     print()
#     print()
#     # break
