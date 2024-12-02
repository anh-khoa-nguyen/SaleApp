from app.models import Category, Product #Dùng DL trong bảng dữ liệu

def load_categories():  # Load danh mục kinh doanh
    return Category.query.order_by("id").all() #Tất cả đều thông qua cái Query của cái Model - SELECT * FROM
    #Sắp xếp tăng theo id


def load_product(cate_id=None, kw=None):  # Load danh mục sản phẩm
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id: #Kiểm tra vừa khác none vừa khác rỗng
        query = query.filter(Product.category_id == cate_id)

    return query.all()
