document.querySelectorAll('.select-slot').forEach(slot => {
    slot.addEventListener('click', () => {
        slot.classList.toggle('selected');
    });
});

   // Danh sách Time Slot theo từng ngày
   const timeSlots = {
    Monday: ["08:00 - 10:00", "14:00 - 16:00", "18:00 - 20:00"],
    Tuesday: ["09:00 - 11:00", "15:00 - 17:00", "19:00 - 21:00"],
    Wednesday: ["07:00 - 09:00", "13:00 - 15:00", "17:00 - 19:00"],
    Thursday: ["10:00 - 12:00", "16:00 - 18:00", "20:00 - 22:00"],
    Friday: ["08:30 - 10:30", "14:30 - 16:30", "18:30 - 20:30"],
    Saturday: ["09:30 - 11:30", "15:30 - 17:30", "19:30 - 21:30"],
    Sunday: ["10:00 - 12:00", "16:00 - 18:00", "20:00 - 22:00"]
};

function formatDateString(dateString) {
    const daysOfWeek = ["Chủ Nhật", "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy"];
    const date = new Date(dateString);
    if (isNaN(date)) return ""; // Kiểm tra nếu giá trị không hợp lệ

    const dayOfWeek = daysOfWeek[date.getDay()];
    const day = date.getDate();
    const month = date.getMonth() + 1; // Tháng bắt đầu từ 0 nên +1
    const year = date.getFullYear();

    return `${dayOfWeek}, ${day}/${month}/${year}`;
}

// Hiển thị thứ khi chọn ngày bắt đầu và kết thúc
document.getElementById("starDate").addEventListener("change", function() {
    document.getElementById("startDateDisplay").innerText = formatDateString(this.value);
});

document.getElementById("endDate").addEventListener("change", function() {
    document.getElementById("endDateDisplay").innerText = formatDateString(this.value);
});

// Xử lý thay đổi Time Slot khi chọn Thứ
document.getElementById("fixedDay").addEventListener("change", function() {
    const selectedDay = this.value; // Lấy giá trị của ngày đã chọn
    const timeSlotSelect = document.getElementById("timeSlot");
    
    // Xóa các option cũ
    timeSlotSelect.innerHTML = "";

    // Nếu có Time Slot cho ngày đã chọn
    if (timeSlots[selectedDay]) {
        timeSlots[selectedDay].forEach(slot => {
            const option = document.createElement("option");
            option.value = slot;
            option.textContent = slot;
            timeSlotSelect.appendChild(option);
        });
    } else {
        const option = document.createElement("option");
        option.value = "";
        option.textContent = "Không có Time Slot";
        timeSlotSelect.appendChild(option);
    }
});
