# zoomAndroidSize
抽取layout布局文件 及style.xml 中的硬编码 dp sp dip 到dimens.xml



    一:重构
    *.建议使用 在之前设备上无问题的代码进行操作
    
    *.打开extract.py 填写输入 输出文件夹等5项   然后执行 python3 extract.py
    
    *.复制输出的dimens.xml文件中的内容  添加到原dimens.xml
    
    *.替换layout下所有文件 替换style.xml文件  然后就可以跑起来了
    
    
    二:兼容新设备
    *.计算两代屏幕密度比例 在run.py deal_dpsp中调整比例. (我们目前已经调好 1.7)
    *.在run.py 里面填写 新 老 设备的dimens.xml地址  然后执行 python3 run.py
    *.复制新的dimens.xml到对应尺寸文件夹 比如 values-720x1280     (小门禁)  
    *.建议生成的dimens.xml中的 关于style部分的dp sp dip 暂时注释调 手动调整
    
    
   

