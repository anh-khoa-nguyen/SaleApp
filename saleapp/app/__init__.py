from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote #Do mật khẩu DB có ký tự đặc biệt



app = Flask(__name__) #Tất cả cấu hình của dự án nằm trong đây

#Kết nối CSDL luôn luôn có một thứ gọi là chuỗi kết nối. Flask sử dụng tên biến "SQLALCHEMY_DATABASE_URI" để kết nối DB
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Abc@123')
#TB1: Driver CSDL kết nối ;; TB2: Un,pass CSDL mình kết nối ;; TB3: Server chạy DB ;; TB4: Tên DB ;; TB5: Cờ tương tác tiếng việt dễ dàng
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
