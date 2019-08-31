#coding=utf-8
from selenium_5itest.ShowapiRequest import ShowapiRequest

#image = Image.open("D:/MyPythonPro/seleniumpro/image/5itest1.png")
#使用ocr识别验证码
#text = pytesseract.image_to_string(image)
#print(text)

#使用第三方sdk识别验证码
r = ShowapiRequest("http://route.showapi.com/184-4", "100948", "63ad6f9c72d444cd80fe13ec216e3e9a")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"D:/MyPythonPro/seleniumpro/image/5itest1.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text)