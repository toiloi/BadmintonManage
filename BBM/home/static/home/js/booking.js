document.getElementById('starDate').addEventListener('change', function() {
    const startDate = new Date(this.value);
    const options = { weekday: 'long', year: 'numeric', month: 'numeric', day: 'numeric' };
    document.getElementById('startDateDisplay').innerText = startDate.toLocaleDateString('vi-VN', options);

    // Tính toán ngày kết thúc
    const endDate = new Date(startDate);
    endDate.setDate(startDate.getDate() + 21); // Thêm 21 ngày (3 tuần) để đến tuần thứ 4

    // Đặt ngày kết thúc vào input và hiển thị
    document.getElementById('endDate').value = endDate.toISOString().split('T')[0];
    document.getElementById('endDateDisplay').innerText = endDate.toLocaleDateString('vi-VN', options);
});

document.getElementById('endDate').addEventListener('change', function() {
    const endDate = new Date(this.value);
    const options = { weekday: 'long', year: 'numeric', month: 'numeric', day: 'numeric' };
    document.getElementById('endDateDisplay').innerText = endDate.toLocaleDateString('vi-VN', options);
});

// Xử lý khi nhấn nút "Đặt sân"
function submitBooking() {
    const playDate = document.getElementById("playDate").value;
    const court = document.getElementById("court").value;
    const selectedSlot = document.querySelector(".select-slot.selected");

    if (!playDate || !selectedSlot) {
        alert("Vui lòng chọn ngày và giờ chơi!");
        return;
    }

    // Giả lập lưu dữ liệu (bạn có thể gửi API ở đây)
    console.log("Ngày chơi:", playDate);
    console.log("Sân:", court);
    console.log("Giờ:", selectedSlot.innerText);

    // Load trang xác nhận thành công
    loadPage('booking-success.html');
}
