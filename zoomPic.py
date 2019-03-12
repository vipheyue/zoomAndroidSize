from PIL import Image


def extra_pic(oldDir, newDir):
    """操作layout文件夹"""
    import os
    for root, dirs, files in os.walk(oldDir, topdown=False):
        for name in files:  # 遍历文件夹
            src_file = os.path.join(root, name)
            # print(src_file)
            new_root = root.replace(oldDir, newDir)  # 新目录
            new_path_file = os.path.join(new_root, name)  # 新文件


            file_type = os.path.basename(name).split(".")[1]
            if file_type.find("png") >= 0 or file_type.find("jpg") >= 0:
                print(name)
                img = Image.open(src_file)
                (width, height) = img.size
                if width>4 and height>4:
                    rate=1.37# 缩放比例
                    # rate=1
                    out = img.resize((int(width/rate), int(height/rate)), Image.ANTIALIAS)
                    out.save(new_path_file,quality=100)

if __name__ == '__main__':

    # 调整21行 缩放比例

    input_dir=r"/Users/heyue/Desktop/66/drawable"# 输入文件夹

    output_dir=r"/Users/heyue/Documents/fenghe/2code/beeboxes/packages/apps/Settings/app/src/main/res/drawable-xxhdpi"# 输出文件夹
    extra_pic(input_dir,output_dir)