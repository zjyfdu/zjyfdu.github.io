---
title: python把bmp转换成jpg
tags:
  - python
categories: python
date: 2018-08-16 21:30:50
---

- 反正已经加到这么晚了，索性再水一篇博客再走
- 如何把bmp批量转换成jpg

```python
import os
from PIL import Image

for root, dirs, files in os.walk("."):
    for bmpfig in files:
        if not bmpfig.endswith('.bmp'):
            continue
        bmpfig = os.path.join(root, bmpfig)
        newfigname = bmpfig[:-4] + ".jpg"
        print "converting from", bmpfig, "to", newfigname
        img = Image.open(bmpfig)
        img.save(newfigname, format='jpeg', quality=95)
        img.close()
        os.remove(bmpfig)
```

- 这段代码贴在某个文件夹下，运行之后会递归地把所有bmp转换成jpg
- 其中，quality是生成jpg的质量，quality越大，jpg文件越大，图片细节越清晰，取值0-100
