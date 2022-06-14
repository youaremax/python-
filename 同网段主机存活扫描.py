import os
def main(duan):
# 查找0～255的地址
    a = []
    for i in range(duan):
        ip = "192.168.0.{}".format(i)
        ret =os.system('ping -n 2 -w 1 %s'%ip) #每个ip ping 1次，等待时间为1s
        if ret:
            print('主机 %s 处于休眠状态'%ip)
        else:
            print('主机 %s 处于存活状态'%ip)
            a.append(ip)
            # break
    print("存活的主机有一下列表：")
    print(a)
if __name__ == "__main__":
    duan = int(input("请输入最大的地址段（如255）：\n"))
    main(duan)
