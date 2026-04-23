'''
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
'''


# 方法1: 搞得太复杂了
def canCompleteCircuit1(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    length = len(gas)
    start_index = -1
    current_gas = -1
    for i in range(length):
        if current_gas < 0:
            if gas[i] >= cost[i]:
                current_gas = gas[i] - cost[i]
                start_index = i
        else:
            current_gas = current_gas + gas[i] - cost[i]

    if start_index != 0:
        for i in range(start_index):
            current_gas = current_gas + gas[i] - cost[i]
            if current_gas < 0:
                start_index = -1
                break

    if current_gas < 0: return -1
    return start_index


# 方法2:
def canCompleteCircuit2(gas, cost):
    length = len(gas)
    count = 0
    current_count = -1
    current_index = -1
    for i in range(length):
        count = count + gas[i] - cost[i]
        if gas[i] >= cost[i] and current_count < 0:
            current_count = gas[i] - cost[i]
            current_index = i
        else:
            current_count = current_count + gas[i] - cost[i]

    if count < 0: return -1
    return current_index


# 方法3:
def canCompleteCircuit3(gas, cost):
    length = len(gas)
    count = 0
    current_count = 0
    current_index = 0
    for i in range(length):
        count = count + gas[i] - cost[i]
        if current_count < 0:
            current_count = gas[i] - cost[i]
            current_index = i
        else:
            current_count = current_count + gas[i] - cost[i]

    if count < 0: return -1
    return current_index


gas1 = [1,2,3,4,5]
cost1 = [3,4,5,1,2]

print(canCompleteCircuit2(gas1, cost1))
