# zoomAndroidSize
抽取layout布局文件 及style.xml 中的硬编码 dp sp dip 到dimens.xml



    一:重构
    *.建议使用 在之前设备上无问题的代码进行操作
    
    *.打开extract.py 填写输入 输出文件夹等5项   然后执行 python3 extract.py
    
    *.复制输出的dimens.xml文件中的内容  添加到原dimens.xml
    
    *.替换layout下所有文件 替换style.xml文件  然后就可以跑起来了
    
    
    二:兼容新设备
    *.计算两代屏幕密度比例 在run.py deal_dpsp中调整比例. (我们目前已经调好)
    *.在run.py 里面填写 新 老 设备的dimens.xml地址  然后执行 python3 run.py
    *.替换dimens.xml文件即可(values文件夹 默认dimens.xm)同时也可放到 values-1200x720 (小门禁)文件夹  之前的备份到values-1280x800目录 dimens.xml  
    *.建议生成的dimens.xml中的 关于style部分的dp sp dip 暂时用老的
    
    
    三:批量调整图片大小(可不用)
    *.pip install -r requirements.txt
    *.填写输入输出文件夹,运行 python3 zoomPic.py

    
   

