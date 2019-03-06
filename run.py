def deal_line(src_file):
    print(src_file)
    file_content = ""
    for line in open(src_file):
        print(line)
        conditions1 = line.find("android:") >= 0
        conditions2 = line.find("dp") >= 0 or line.find("sp") >= 0
        if conditions1 and conditions2:
            print(line)
            findindex = line.find("\"")  # 左边的引号
            lastindex = line.rfind("\"")  # 右边的引号
            original_text = line[findindex + 1:lastindex]  # 中间的内容 66dp or 66sp
            deal_text = deal_dpsp(original_text, "dp")
            deal_text = deal_dpsp(deal_text, "sp")
            new_text = line.replace(original_text, deal_text)
            file_content += new_text
        else:
            file_content += line
    return file_content


def del_style_xml(src_file):
    """
    可不用这个 建议手动调style
    :param src_file:
    :return:
    """
    print(src_file)
    file_content = ""
    for line in open(src_file):
        print(line)
        conditions1 = line.find("item name=") >= 0
        if conditions1:
            print(line)
            findindex = line.find(">")  # 左边的引号
            lastindex = line.rfind("<")  # 右边的引号
            original_text = line[findindex + 1:lastindex]  # 中间的内容
            deal_text = deal_dpsp(original_text, "dp")
            deal_text = deal_dpsp(deal_text, "sp")
            new_text = line.replace(original_text, deal_text)
            file_content += new_text
        else:
            file_content += line
    return file_content


def deal_dpsp(text, symbol):
    """"
    计算上一代屏幕密度
    计算当前一代屏幕密度 得到比例1.7

    处理数值
    66dp or 66sp
    66/1.7=39
    39dp


    """
    dp_index = text.find(symbol)
    if dp_index >= 0:
        try:
            deal_text = text[:dp_index]  # 取数字
            deal_text = int(float(deal_text)) #非数字直接跑异常返回原内容即可
            if deal_text > 4:
                deal_text = int(deal_text / 1.7)
                replace_text = str(deal_text) + symbol
                return replace_text
            else:
                return text
        except Exception:  # 异常情况返回原行内容
            return text
    return text


def deal_layout(oldDir, newDir):
    """操作layout文件夹"""
    import os
    for root, dirs, files in os.walk(oldDir, topdown=False):
        for name in files:  # 遍历文件夹
            src_file = os.path.join(root, name)
            print(src_file)
            new_root = root.replace(oldDir, newDir)  # 新目录
            new_path_file = os.path.join(new_root, name)  # 新文件
            new_content = deal_line(src_file)  # 操作过后的文件内容
            # 这句话自带文件关闭功能，所以和那些先open再write再close的方式来说，更加pythontic！
            with open(new_path_file, "w", encoding='utf-8') as f:
                f.write(new_content)


if __name__ == '__main__':
    """
    处理两代设备屏幕密度问题导致的显示问题 (layout布局调整)
    1.计算两代屏幕密度比例 在deal_dpsp调整比例
    2.填写输入输出文件夹
    3.运行一下,收工. 
    """
    # old_file = "/Users/heyue/Desktop/actionbar_head_main.xml"
    # showLine(old_file)
    # old_file = "/Users/heyue/Documents/fenghe/2code/beeboxes/packages/apps/Settings/app/src/main/res/values/styles.xml"
    # del_style_xml(old_file)

    oldDir = "/Users/heyue/Desktop/testPy/beeboxes/packages/apps/Settings/app/src/main/res/layout"  # layout文件夹
    newDir = "/Users/heyue/Desktop/img"  # 输出文件夹
    deal_layout(oldDir, newDir)
