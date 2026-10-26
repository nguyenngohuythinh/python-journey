# Tuần 14 — OOP Essentials · Composition · Basic inheritance

Tuần này học cách gom dữ liệu và hành vi có liên quan vào object. Trọng tâm
không phải dùng class cho mọi thứ, mà là chọn cấu trúc giúp code dễ hiểu hơn.
Trong project VuaCóc Bot Journey, ta dùng **composition** để thay strategy mà
không phải viết lại bot core.

## Sau tuần này, bạn có thể

- phân biệt class, object, instance attribute và method;
- giải thích vai trò của `self`, `__init__` và `__str__`;
- giữ state khởi tạo hợp lệ bằng kiểm tra đơn giản;
- chọn class khi dữ liệu và hành vi liên quan cần đi cùng nhau;
- dùng composition để tiêm/thay strategy;
- viết và so sánh ba policy nhỏ: defensive, balanced, aggressive;
- dùng inheritance trong một ví dụ “is-a” rõ ràng;
- chạy machine check và giải thích bằng chứng hành vi.

## Lộ trình học

1. Đọc [notes](notes.md), đặc biệt class/object và responsibility.
2. Chạy ba file trong [examples](examples/).
3. Tự làm ba bài trong [exercises](exercises/) trước khi xem đáp án.
4. Dùng [hints](hints.md) nếu bị kẹt.
5. Hoàn thành [mini-project](mini-project/README.md).
6. Chạy [machine check](checks/README.md) để xác minh solution tham khảo.

## Lệnh kiểm tra

Từ thư mục gốc repository:

```bash
python weeks/week-14-oop-essentials/checks/check_week.py
```

Các file trong `exercises/` là starter có chủ đích để người học tự hoàn thiện;
machine check hiện xác minh solution tham khảo trong `solutions/`, không tự
điền đáp án vào starter.
