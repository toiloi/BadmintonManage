from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Kết nối MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="yourdatabase"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)

    # Lấy danh sách giao dịch thanh toán
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    transactions = cursor.fetchall()

    # Lấy danh sách khách hàng VIP
    cursor.execute("SELECT * FROM vip_customers ORDER BY booked_hours DESC")
    vip_customers = cursor.fetchall()

    # Lấy tổng doanh thu và số lượt đặt sân trong tháng này
    cursor.execute("""
        SELECT SUM(revenue) AS total_revenue, SUM(bookings) AS total_bookings
        FROM revenue_stats
        WHERE MONTH(date) = MONTH(CURRENT_DATE()) AND YEAR(date) = YEAR(CURRENT_DATE())
    """)
    monthly_stats = cursor.fetchone()

    # Lấy dữ liệu doanh thu theo ngày
    cursor.execute("SELECT * FROM revenue_stats ORDER BY date DESC")
    daily_stats = cursor.fetchall()

    cursor.close()
    
    return render_template('index.html', 
                           transactions=transactions,
                           vip_customers=vip_customers,
                           total_revenue=monthly_stats["total_revenue"] or 0,
                           total_bookings=monthly_stats["total_bookings"] or 0,
                           daily_stats=daily_stats)

if __name__ == '__main__':
    app.run(debug=True)
