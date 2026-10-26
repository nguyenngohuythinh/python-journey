# Gợi ý — Week 14

## Exercise 01 — Class và object

- Khởi tạo state trong `__init__`; dùng `self.completed` và
  `self.total` để giữ dữ liệu trên mỗi object.
- `percentage()` trả về số phần trăm, không cần in bên trong method.
- `__str__` phải **return** một string; `print()` sẽ dùng string đó.
- Nghĩ đến các trường hợp tổng bằng 0 và số mục hoàn thành không hợp lệ.

## Exercise 02 — Composition

- `Bot.__init__` lưu function được truyền vào `self.strategy`.
- `choose_action(state)` chỉ cần gọi strategy với state rồi trả kết quả.
- Viết helper `move_toward(state, target)` để không hardcode `"right"`.
- Kiểm tra cả goal `0` và goal `4`.
- Policy defensive nên ưu tiên an toàn khi đối thủ gần; balanced tiến về goal;
  aggressive có thể đuổi đối thủ khi ở gần.
- Đổi strategy mà không viết lại class `Bot`.

## Exercise 03 — Inheritance

- `Animal` lưu thuộc tính dùng chung như `name`.
- `Dog(Animal)` nhận thuộc tính `name` từ class cha.
- `Dog.speak()` là hành vi riêng của Dog.
- Câu giải thích có thể bắt đầu bằng: “Dog là một Animal vì ...”.

## Sau khi làm xong

Chạy machine check theo hướng dẫn trong [checks](checks/README.md). Nếu check
thất bại, đọc assertion và so sánh expected action với state đầu vào.
