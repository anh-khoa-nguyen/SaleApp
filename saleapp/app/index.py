from flask import render_template, request #Đối tượng lấy tham số đường dẫn
import dao #Muốn gửi dữ liệu ra view “index.html”: File “index.py” thêm 1 dòng: import dao
from app import app


@app.route("/")
def index():
    cates = dao.load_categories() #Đây là dữ liệu bạn muốn gửi ra View

    cate_id = request.args.get('category_id') #Query paragram, thêm phương thức get để an toàn (phòng trường hợp không có tham số)
    kw = request.args.get('kw')  # Lấy kw trên đường dẫn
    prods = dao.load_product(cate_id=cate_id, kw = kw) #Lấy các product từ dao

    return render_template('index.html', categories = cates, products = prods) #Dữ liệu từ Controller ra View gọi là Context paragrams
    #Công nghệ của Python, cách gửi là: đặt cái tên rồi gán đối tượng vô, như vậy ta có thuộc tính "categories" ngoài cái View

if __name__ == '__main__':
    app.run(debug=True)