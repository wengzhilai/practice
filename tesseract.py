from PIL import Image
import pytesseract
#上面都是导包，只需要下面这一行就能实现图片文字识别
# text=pytesseract.image_to_string(Image.open('/private/var/root/Pictures/WX20180522-115105.png'),lang='eng')
text=pytesseract.image_to_string(Image.open('/Users/isoft/Documents/QQ20180522-150423.png'),lang='chi_sim')
print(text)