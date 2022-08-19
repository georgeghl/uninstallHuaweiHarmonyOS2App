import os
import json

print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print("|||禁用/卸载 华为Mate305G 鸿蒙2.0自带的多余应用 Device Model:Huawei.TAS-AN00.HarmonyOS2.0|||")
print("------------------------------注：其它华为鸿蒙系统手机同样适用------------------------------")
print("--------------------------默认禁用系统更新、华为应用市场、华为汽车等-------------------------")
print("-------------------------------默认卸载华为音乐、华为视频等---------------------------------")
print("------------------------可右键-解压后替换默认的禁用/卸载列表JSON文件-------------------------")
print("----------------------------------|||按任意键继续...|||-----------------------------------")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
os.system("pause")


with open("TAS-AN00_todo_disable.json",mode='r',encoding="utf-8") as f:
    disablePackages=json.load(f)

print("可用设备:")
os.system("adb devices")

for i in disablePackages:
    print("[禁用]当前应用包名: "+str(i))
    command=".\\platform-tools\\adb.exe shell pm disable-user "+str(i)
    os.system(command)

print("[禁用]全部执行完毕......")



with open("TAS-AN00_todo_uninstall.json",mode='r',encoding="utf-8") as f:
    uninstallPackages=json.load(f)

print("------------------------------------------------------")
print("------------------------------------------------------")
print("------------------------------------------------------")
print("可用设备:")
os.system("adb devices")

for j in uninstallPackages:
    print("[卸载]当前应用包名: "+str(j))
    command=".\\platform-tools\\adb.exe shell pm uninstall --user 0 "+str(j)
    os.system(command)
    command=".\\platform-tools\\adb.exe shell pm uninstall -k –user 0 package:"+str(j)
    os.system(command)

print("[卸载]全部执行完毕......")