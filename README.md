# uninstallHuaweiHarmonyOS2App
This Python script is designed for uninstalling&disabling the useless Huawei HarmonyOS2.0 factory-installed applications.
It uses Android Debug Bridge(adb) to execute shell command. Notice: adb.exe is in ./platform-tools/
The default JSON files contain such applications:
disable:
["com.huawei.scanner", 
"com.huawei.hilink.framework", 
"com.huawei.searchservice", 
"com.huawei.appmarket", 
"com.huawei.arengine.service", 
"com.huawei.hidisk", 
"com.huawei.hicloud", 
"com.huawei.hwasm", 
"com.huawei.hms.dupdateengine", 
"com.huawei.android.hwouc", 
"com.huawei.android.thememanager", 
"com.huawei.android.instantonline"]
uninstall:
["com.huawei.hwblockchain", 
"com.huawei.hicar", 
"com.huawei.himovie", 
"com.huawei.game.kitserver", 
"com.huawei.vassistant", 
"com.huawei.search", 
"com.huawei.ohos.search", 
"com.huawei.hwdiagnosis", 
"com.huawei.easygo", 
"com.huawei.android.hwupgradeguide", 
"com.huawei.magazine", 
"com.huawei.hwvoipservice", 
"com.android.mediacenter", 
"com.huawei.phoneservice", 
"com.huawei.android.pushagent", 
"com.huawei.fastapp", 
"com.huawei.videoeditor", 
"com.huawei.android.karaoke", 
"com.huawei.gameassistant", 
"com.huawei.himovie.partner1", 
"com.huawei.himovie.partner2", 
"com.huawei.hwdetectrepair", 
"com.huawei.hwstartupguide", 
"com.huawei.intelligent", 
"com.huawei.music", 
"com.sohu.sohuvideo.emplayer", 
"com.tencent.qqlivehuawei"]

You can add/remove the application package name to/from the JSON files to disable/uninstall the app, OR replace the JSON files entirely.

# 卸载华为HarmonyOS2出厂自带App
此Python脚本目的是卸载/禁用华为HarmonyOS2.0出厂自带的无用应用。
使用Android调试桥（adb）执行shell命令。注:adb.exe在/platform-tools/目录下。
默认JSON文件包含以下应用程序：
禁用:
["com.huawei.scanner", 
"com.huawei.hilink.framework", 
"com.huawei.searchservice", 
"com.huawei.appmarket", 
"com.huawei.arengine.service", 
"com.huawei.hidisk", 
"com.huawei.hicloud", 
"com.huawei.hwasm", 
"com.huawei.hms.dupdateengine", 
"com.huawei.android.hwouc", 
"com.huawei.android.thememanager", 
"com.huawei.android.instantonline"]
卸载:
["com.huawei.hwblockchain", 
"com.huawei.hicar", 
"com.huawei.himovie", 
"com.huawei.game.kitserver", 
"com.huawei.vassistant", 
"com.huawei.search", 
"com.huawei.ohos.search", 
"com.huawei.hwdiagnosis", 
"com.huawei.easygo", 
"com.huawei.android.hwupgradeguide", 
"com.huawei.magazine", 
"com.huawei.hwvoipservice", 
"com.android.mediacenter", 
"com.huawei.phoneservice", 
"com.huawei.android.pushagent", 
"com.huawei.fastapp", 
"com.huawei.videoeditor", 
"com.huawei.android.karaoke", 
"com.huawei.gameassistant", 
"com.huawei.himovie.partner1", 
"com.huawei.himovie.partner2", 
"com.huawei.hwdetectrepair", 
"com.huawei.hwstartupguide", 
"com.huawei.intelligent", 
"com.huawei.music", 
"com.sohu.sohuvideo.emplayer", 
"com.tencent.qqlivehuawei"]

你可以在JSON文件中添加/删除应用程序包名称以禁用/卸载应用程序，或完全替换JSON文件。