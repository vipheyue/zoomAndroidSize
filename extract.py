import os


def deal_line(src_file):
    print(src_file)
    file_content = ""
    line_index = 0
    basename = os.path.basename(src_file).split(".")[0]
    for line in open(src_file):
        line_index += 1
        print(line)
        conditions1 = line.find("android:") >= 0
        conditions2 = line.find("dp") >= 0 or line.find("sp") >= 0 or line.find("dip") >= 0  # 行中包含 sp dp dip
        if conditions1 and conditions2:
            print(line)
            findindex = line.find("\"")  # 左边的引号
            lastindex = line.rfind("\"")  # 右边的引号
            original_text = line[findindex + 1:lastindex]  # 中间的内容 66dp or 66sp

            extra_line_name = str(basename) + "_" + str(line_index)

            deal_text = extract_detail(original_text, "dp", extra_line_name)
            deal_text = extract_detail(deal_text, "sp", extra_line_name)
            deal_text = extract_detail(deal_text, "dip", extra_line_name)
            new_text = line.replace(original_text, deal_text)
            file_content += new_text
        else:
            file_content += line
    return file_content


def extract_detail(text, symbol, extra_line_name):
    """
    抽取 22dp or 23sp  变为  @dimen/xx_xxxxx_xxxx
    并在 dimens.xml中添加 <dimen name="text_margin">22dp</dimen>

    :param original_text:
    :return:
    """

    dp_index = text.find(symbol)
    if dp_index >= 0:
        try:
            deal_text = text[:dp_index]  # 取数字
            deal_text = int(float(deal_text))  # 非数字直接跑异常返回原内容即可
            if deal_text > 0:
                replace_text = "@dimen/" + extra_line_name

                dimens_content = f'<dimen name="{extra_line_name}">{text}</dimen>\r\n'
                # dimens_content = '<dimen name="%s">%s</dimen>\r\n' % (extra_line_name, text)
                # 在dimens.xml中添加
                with open(dimens_xml_file, "a", encoding='utf-8') as f:
                    f.write(dimens_content)
                return replace_text
            else:
                return text
        except Exception:  # 异常情况返回原行内容
            return text
    return text
    pass


def extra_layout(oldDir, newDir):
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


def extra_style(input_style_file, output_style_file):
    """
    抽取 style 到 dimens.xml
    :param src_file:
    :return:
    """
    print(input_style_file)
    file_content = ""
    line_index = 0
    basename = os.path.basename(input_style_file).split(".")[0]

    for line in open(input_style_file):
        print(line)
        line_index += 1

        conditions1 = line.find("name=") >= 0
        if conditions1:
            print(line)
            findindex = line.find(">")  # 左边的引号
            lastindex = line.rfind("<")  # 右边的引号
            original_text = line[findindex + 1:lastindex]  # 中间的内容
            extra_line_name = str(basename) + "_" + str(line_index)

            deal_text = extract_detail(original_text, "dp", extra_line_name)
            deal_text = extract_detail(deal_text, "sp", extra_line_name)
            deal_text = extract_detail(deal_text, "dip", extra_line_name)
            new_text = line.replace(original_text, deal_text)
            file_content += new_text
        else:
            file_content += line

        # 这句话自带文件关闭功能，所以和那些先open再write再close的方式来说，更加pythontic！
        with open(output_style_file, "w", encoding='utf-8') as f:
            f.write(file_content)


if __name__ == '__main__':
    """
    1.抽取资源文件中  sp dp dip
    2.生成新的资源文件
    3.生成新的dimens.xml  
    
    
    
    其他: 遇到.ds 文件报错 用命令行删除.ds即可
    """

    dimens_xml_file = r"/Users/heyue/Desktop/testPy/beeboxes/packages/apps/DataTool/app/src/main/res/values-1280x800/dimens.xml"  # 输出dimens.xml文件 之后需要手动粘贴

    inputDir = r"/Users/heyue/Desktop/testPy/beeboxes/packages/apps/DataTool/app/src/main/res/layout"  # layout  输入文件夹
    outputDir = r"/Users/heyue/Desktop/img"  # layout 输出文件夹
    extra_layout(inputDir, outputDir)  # 抽取layout

    input_style_file = r"/Users/heyue/Desktop/testPy/beeboxes/packages/apps/DataTool/app/src/main/res/values/styles.xml"  # style.xml文件
    output_style_file = r"/Users/heyue/Desktop/testPy/beeboxes/packages/apps/DataTool/app/src/main/res/values-1280x800/styles.xml"  # style.xml文件
    extra_style(input_style_file, output_style_file)  # 抽取style.xml
