import re
import PIL 
from pathlib import Path
from PIL import Image
base_dir = Path(r"D:\code\html library\falcon\Falcon-Admin-Dashboard-WebApp-Template-v3.4.0-and-v2.8.2\falcon-v3.4.0\public")
with open("index.html",'r') as fp,open("report.txt",'a') as report_fp:
    data = fp.read()
    img_relative_list = re.findall(r'<img .*? src="(.*?)" .* \/>',data)
    for relative_address in img_relative_list:
        absolute_address = base_dir.joinpath(relative_address)
        if absolute_address.suffix!=".svg":
            im = Image.open(absolute_address)
            width, height = im.size
            report_fp.write(f"name: {absolute_address.name}, width: {width}, height: {height}\n")
