# Tạo Entity Class
from itertools import product
from xmlrpc.client import Boolean

from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey  # Tạo các trường
from sqlalchemy.orm import relationship
from app import db, app


# import cái biến db, app bên file __init__ từ gói "app"


class Category(
    db.Model):  # Kế thừa db.Model, Python cho phép đa kế thừa, kể từ thời điểm kế thừa, lớp này trở thành Entity Class, đại diện cho 1 bảng dưới Database, lưu trữ, tương tác với dữ liệu dưới DB
    # Mỗi thuộc tính khai báo trong lớp sẽ ánh xạ thành 1 cột "Column" dưới database, kiểu dữ liệu của Python ánh xạ thành kiểu dữ liệu của Database
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)  # Không trùng lắp giữa các thể hiện
    products = relationship('Product', backref='category',
                            lazy=True)  # MQH giữa Cate và Prod, để trong dấu nháy vì Python là ngôn ngữ thông dịch, product được định nghĩa sau đó
    # Khai báo backref thì sẽ thêm 1 cái trường category vào cái mqh (Cate bỏ vào Prod), Category là đối tượng đại diện cho category_id
    # lazy: Khi mà lấy danh mục ra thì những sản phẩm của danh mục nó chưa truy vấn, cho đến khi nào truy cập vào 'products' thì mới truy vấn, nhiều thì thường Lazy = True

    # MQH: Một danh mục nhiều SP, 1 SP thuộc 1 danh mục


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))  # Không trùng lắp giữa các thể hiện
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100), nullable=True)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':  # Tự phát hiện cái bảng này chưa có và nó tạo ra
    with app.app_context():  # Trong phiên bản mới bắt lệnh này chạy trong ngữ cảnh ứng dụng
        db.create_all()  # Biến tất cả thành bảng dữ liệu, chuyển chữ "C" thành chữ "c"
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Laptop')
        #
        # db.session.add_all([c1,c2,c3]) #Lấy tất cả đối tượng xuống db, trong tất cả ORM thì 1 phiên tương tác với dữ liệu gọi là Session
        # db.session.commit() #Nó sẽ insert 3 cái đối tượng vào Category

        products = [{
            "id": 1,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "id": 2,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "id": 3,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }, {
            "id": 4,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "id": 5,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "id": 6,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }, {
            "id": 7,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "id": 8,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "id": 9,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }]

        for p in products:
            prod = Product(**p)
            db.session.add(prod)

        db.session.commit()