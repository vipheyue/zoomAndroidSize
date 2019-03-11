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
        conditions1 = line.find("name=") >= 0
        if conditions1:
            print(line)
            findindex = line.find(">")  # 左边的引号
            lastindex = line.rfind("<")  # 右边的引号
            original_text = line[findindex + 1:lastindex]  # 中间的内容
            deal_text = deal_dpsp(original_text, "dp")
            deal_text = deal_dpsp(deal_text, "sp")
            deal_text = deal_dpsp(deal_text, "dip")
            new_text = line.replace(original_text, deal_text)
            file_content += new_text
        else:
            file_content += line
    return file_content


def deal_dpsp(text, symbol):
    """"
    计算上一代屏幕密度
    计算当前一代屏幕密度 得到比例

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
                deal_text = int(deal_text / 1.37)
                replace_text = str(deal_text) + symbol
                return replace_text
            else:
                return text
        except Exception:  # 异常情况返回原行内容
            return text
    return text


if __name__ == '__main__':
    """
    对mimens.xml 进行 倍增
    """
    old_file = "/Users/heyue/Desktop/testPy/beeboxes/packages/apps/Settings/app/src/main/res/values-1280x800/dimens.xml" # 老的style 或者 dimens文件
    new_file = "/Users/heyue/Desktop/dimens.xml"# 新的 新尺寸的 dimens文件
    result_content=del_style_xml(old_file)
    with open(new_file, "w", encoding='utf-8') as f:
        f.write(result_content)

