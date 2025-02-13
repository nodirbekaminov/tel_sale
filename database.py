import sqlite3


def create_users_table():
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT
        );
        ''')
    database.commit()
    database.close()


# create_users_table()

def create_carts_table():
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carts(
        cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id),
        total_price DECIMAL(12, 2) DEFAULT 0,
        total_products INTEGER DEFAULT 0
        );
    ''')
    database.commit()
    database.close()


# create_carts_table()

def create_cart_products_table():
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart_products(
            cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR(30),
            quantity INTEGER NOT NULL,
            final_price DECIMAL(12, 2) NOT NULL,
            cart_id INTEGER REFERENCES carts(cart_id),

            UNIQUE(product_name, cart_id)
        );
    ''')
    database.commit()
    database.close()


# create_cart_products_table()

def create_categories_table():
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name VARCHAR(30) NOT NULL UNIQUE
        );
    ''')
    database.commit()
    database.close()


# create_categories_table()

def insert_categories():
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO categories(category_name) VALUES
    ('PHONES 📱'),
    ('COMPUTERS 💻'),
    ('HEADPHONES 🎧'),
    ('CAMERAS 📷')
    ''')
    database.commit()
    database.close()


# insert_categories()

def create_products_table():
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        product_name VARCHAR(30) NOT NULL UNIQUE,
        price DECIMAL (12, 2) NOT NULL,
        description VARCHAR(200),
        image TEXT,

        FOREIGN KEY(category_id) REFERENCES categories(category_id)
    );
    ''')
    database.commit()
    database.close()


# create_products_table()


def insert_products_table():
    try:
        database = sqlite3.connect('tel_sale.db')
        cursor = database.cursor()
        currency_rate = 12800
        products = [
            (1, "IPHONE 16plus", round(10900000 / currency_rate, 2), "color_ultramarine, 256gb",
             "media/phones/16plus.png"),
            (1, "IPHONE 15pro", round(9500000 / currency_rate, 2), "color_black, 512gb", "media/phones/15pro.jpg"),
            (1, "IPHONE 14pro_max", round(8900000 / currency_rate, 2), "color_purple, 1TB",
             "media/phones/14promax.jpg"),
            (1, "IPHONE 15pro_max", round(9800000 / currency_rate, 2), "color_titanium, 512gb",
             "media/phones/15promax.jpeg"),
            (1, "IPHONE 16plus_black", round(10850000 / currency_rate, 2), "color_black, 256gb",
             "media/phones/16plusb.png")
        ]

        cursor.executemany('''
        INSERT INTO products(category_id, product_name, price, description, image) 
        VALUES (?, ?, ?, ?, ?)
        ''', products)

        database.commit()
    finally:
        database.close()


# insert_products_table()

def insert_computers_table():
    try:
        database = sqlite3.connect('tel_sale.db')
        cursor = database.cursor()

        currency_rate = 12800
        products = [
            (2, "Linovo Thinkbook", round(6790000 / currency_rate, 2), "15 inch intel core 5 512gb",
             "media/computers/LinovoThinkbook.jpg"),
            (2, "CSLComputer", round(8050000 / currency_rate, 2), "Notebook CSL VenomGamer G16 / 32GB / 2000GB",
             "media/computers/cslcomputer.jpg"),
            (2, "XIAOMI Mi Notebook Pro", round(9550000 / currency_rate, 2), "GTX I5 15.6 256GB/8GB RAM",
             "media/computers/XIAOMI Mi Notebook Pro.jpg"),
            (2, "AcerNitroV15", round(10500000 / currency_rate, 2),
             "Acer Nitro V 15 review: Middling hardware ruined by overbearing softwa",
             "media/computers/acernitrov15.jpg"),
            (2, "Razer Blade 15", round(7800000 / currency_rate, 2),
             "15.6'' FHD-144 Hz Base Model, Intel Core i7-10750H 6-Core", "media/computers/Razer Blade 15.jpg")
        ]
        cursor.executemany('''
        INSERT INTO products(category_id, product_name, price, description, image) 
        VALUES (?, ?, ?, ?, ?)
        ''', products)
        database.commit()
    finally:
        database.close()


# insert_computers_table()


def insert_headphone_products():
    try:
        database = sqlite3.connect('tel_sale.db')
        cursor = database.cursor()
        currency_rate = 12800
        products = [
            (3, "SHURE AONIC 50 GEN 2", round(680000 / currency_rate, 2), "Wireless Noise Cancelling Headphones",
             "media/headphones/SHURE AONIC 50(GEN 2).jpeg"),
            (3, "Beats Solo 4", round(1020000 / currency_rate, 2), "Bluetooth Wireless On-Ear Headphones",
             "media/headphones/Beats Solo 4.jpg"),
            (3, "VIVO TWS Air 2 TWS", round(180000 / currency_rate, 2),
             "Earphone Bluetooth 5.3 AI Call Noise Cancelling True Wireless Headset 30 Hour",
             "media/headphones/VIVO TWS Air 2 TWS.jpeg"),
            (3, "Komodos Bluetooth", round(580000 / currency_rate, 2), "Headphones with Comfortable Over-Ear Fit",
             "media/headphones/Komodos Bluetooth .jpg"),
            (3, "Sony WH-CH520", round(1550000 / currency_rate, 2),
             "Bluetooth On-Ear Headphones Blue - HiFi Corporation", "media/headphones/Sony WH-CH520.png")
        ]

        cursor.executemany('''
        INSERT INTO products(category_id, product_name, price, description, image) 
        VALUES (?, ?, ?, ?, ?)''', products)

        database.commit()

    finally:
        database.close()


# insert_headphone_products()

def insert_cameras_products():
    try:
        database = sqlite3.connect('tel_sale.db')
        cursor = database.cursor()
        currency_rate = 12800
        products = [
            (4, "Canon EOS R7", (1800), "Mirrorless Camera with 18-150mm Lens | Shams Stores",
             "media/cameras/CanonEOSR7.jpg"),
            (4, "HSC-300R", round(20800000 / currency_rate, 2), "HSC-300R Digital Triax Broadcast Camera - Utopia",
             "media/cameras/HSC-300R.jpg"),
            (4, "NikonZFC", round(7800000 / currency_rate, 2), "Digital Photography Review",
             "media/cameras/NikonZFC.jpeg"),
            (4, "SonyA7", round(12800000 / currency_rate, 2), "Sony a7 IV Review PCMag", "media/cameras/SonyA7.jpeg"),
            (4, "CanonEOSR5", round(17500000 / currency_rate, 2), "ISO 100 – 51 200", "media/cameras/CanonEOSR5.jpeg")
        ]

        cursor.executemany('''
        INSERT INTO products(category_id, product_name, price, description, image) 
        VALUES (?, ?, ?, ?, ?)''', products)

        database.commit()
    finally:
        database.close()


# insert_cameras_products()

def first_select_user(chat_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE telegram_id = ?
    ''', (chat_id,))
    user = cursor.fetchone()
    database.close()
    return user


def first_register_user(chat_id, full_name):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO users(telegram_id, full_name) VALUES(?, ?)
    ''', (chat_id, full_name))
    database.commit()
    database.close()


def update_user_to_finish_register(chat_id, phone):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    UPDATE users
    SET phone = ?
    WHERE telegram_id = ?
    ''', (phone, chat_id))
    database.commit()
    database.close()


def insert_to_cart(chat_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO carts(user_id)
    VALUES (
        (SELECT user_id FROM users WHERE telegram_id = ?)
    )
    ''', (chat_id,))
    database.commit()
    database.close()


def get_all_categories():
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM categories;
    ''')
    categories = cursor.fetchall()
    database.close()
    return categories


def get_products_by_category_id(category_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_id, product_name
    FROM products WHERE category_id = ?
    ''', (category_id,))
    products = cursor.fetchall()
    database.close()
    return products


def get_product_detail(product_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM products
    WHERE product_id = ?
    ''', (product_id,))
    product = cursor.fetchone()
    database.close()
    return product


def get_user_cart_id(chat_id):
    try:
        database = sqlite3.connect('tel_sale.db')
        cursor = database.cursor()
        cursor.execute('''
        SELECT cart_id FROM carts
        WHERE user_id = (SELECT user_id FROM users WHERE telegram_id = ?)
        ''', (chat_id,))
        result = cursor.fetchone()
        if result is None:
            return None
        return result[0]
    finally:
        database.close()


def insert_or_update_cart_product(cart_id, product, quantity, final_price):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    try:
        cursor.execute('''
        INSERT INTO cart_products(cart_id, product_name, quantity, final_price)
        VALUES (?, ?, ?, ?)
        ''', (cart_id, product, quantity, final_price))
        database.commit()
        return True
    except:
        cursor.execute('''
        UPDATE cart_products
        SET quantity = ?,
        final_price = ?
        WHERE product_name = ? AND cart_id = ?
        ''', (quantity, final_price, product, cart_id))
        database.commit()
        return False
    finally:
        database.close()


def update_total_product_total_price(cart_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    UPDATE carts
    SET total_products = (
    SELECT SUM(quantity) FROM cart_products
    WHERE cart_id = :cart_id
    ),
    total_price = (
    SELECT SUM(final_price) FROM cart_products
    WHERE cart_id = :cart_id
    )
    WHERE cart_id = :cart_id
    ''', {'cart_id': cart_id})
    database.commit()
    database.close()


def get_cart_products(cart_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_name, quantity, final_price
    FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    return cart_products


def get_total_products_price(cart_id):
    try:
        database = sqlite3.connect('tel_sale.db')
        cursor = database.cursor()
        cursor.execute('''
        SELECT total_products, total_price FROM carts WHERE cart_id = ?
        ''', (cart_id,))
        result = cursor.fetchone()
        if result is None:
            return 0, 0
        total_products, total_price = result
        return total_products, total_price
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return 0, 0
    finally:
        database.close()


def get_cart_products_for_delete(cart_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT cart_product_id, product_name
    FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    return cart_products


def delete_cart_product_from_database(cart_product_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM cart_products WHERE cart_product_id = ?
    ''', (cart_product_id,))
    database.commit()
    database.close()


def drop_cart_products_default(cart_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    database.commit()
    database.close()


def orders_check():
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders_check(
    order_check_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER REFERENCES carts(cart_id),
    total_price DECIMAL (12, 2) DEFAULT 0,
    total_products INTEGER DEFAULT 0,
    time_order TEXT,
    data_order TEXT
    );
    ''')
    database.commit()
    database.close()


# orders_check()


def order():
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_check_id INTEGER REFERENCES orders_check(order_check_id),
        product_name VARCHAR(100) NOT NULL,
        quantity INTEGER NOT NULL,
        final_price DECIMAL(12, 2) NOT NULL
    );
    ''')
    database.close()
    database.commit()


# order()


def save_oder_check(cart_id, total_products, total_price, time_order, data_order):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO orders_check(cart_id, total_products, total_price, time_order, data_order)
    VALUES (?, ?, ?, ?, ?)
    ''', (cart_id, total_products, total_price, time_order, data_order))
    database.commit()
    database.close()


def get_order_check_id(cart_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT order_check_id FROM orders_check
    WHERE cart_id = ?
    ''', (cart_id,))
    order_check_id = cursor.fetchall()[-1][0]
    database.close()
    return order_check_id


def save_order(order_check_id, product_name, quantity, final_price):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO orders(order_check_id, product_name, quantity, final_price)
    VALUES(?, ?, ?, ?)
    ''', (order_check_id, product_name, quantity, final_price))
    database.commit()
    database.close()


def get_order_check(cart_id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM orders_check
    WHERE cart_id = ?
    ''', (cart_id,))
    order_check_info = cursor.fetchall()
    database.close()
    return order_check_info


def get_detail_order(id):
    database = sqlite3.connect('tel_sale.db')
    cursor = database.cursor()
    cursor.execute('''
        SELECT product_name, quantity, final_price FROM orders
        WHERE order_check_id = ?
    ''', (id,))
    detail_order = cursor.fetchall()
    database.close()
    return detail_order
