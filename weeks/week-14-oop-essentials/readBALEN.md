# Tuần 14 — Tóm tắt OOP, Composition và Inheritance

## Tuần này học gì?

Tuần 14 giới thiệu **lập trình hướng đối tượng (Object-Oriented Programming — OOP)** trong Python. Mục tiêu là biết cách nhóm dữ liệu và hành vi liên quan vào một object, đồng thời chọn cách tổ chức code đơn giản, dễ đọc.

### 1. Class, object và method

- **Class** là bản thiết kế mô tả dữ liệu và hành vi.
- **Object/instance** là một đối tượng được tạo từ class.
- **Attribute** lưu dữ liệu của object.
- **Method** là hàm được định nghĩa trong class.
- `__init__()` khởi tạo trạng thái ban đầu; `self` tham chiếu đến instance hiện tại.
- `__str__()` cung cấp cách biểu diễn object dễ đọc khi dùng `print()`.

Trong bài tập `ex01_classes.py`, class `Progress` lưu số mục đã hoàn thành và tổng số mục, tính phần trăm tiến độ, đồng thời kiểm tra dữ liệu đầu vào hợp lệ.

### 2. Composition — kết hợp các thành phần

**Composition** là cách xây dựng hành vi của một đối tượng bằng cách kết hợp hoặc giao cho thành phần khác xử lý một nhiệm vụ. Cách này giúp thay đổi hành vi mà không cần sửa toàn bộ class chính.

Trong `ex02_composition.py`, class `Bot` nhận một strategy để quyết định hành động. Có ba strategy mẫu:

- `defensive`: ưu tiên chờ khi đối thủ ở gần.
- `balanced`: di chuyển từng bước về mục tiêu.
- `aggressive`: đuổi theo đối thủ khi đủ gần, nếu không thì tiến về mục tiêu.

Có thể đổi `bot.strategy` để thay hành vi của bot. `Bot` cũng kiểm tra hành động strategy trả về có thuộc `left`, `right` hoặc `wait` hay không.

### 3. Inheritance — kế thừa

**Inheritance** cho phép class con kế thừa thuộc tính và hành vi từ class cha khi có quan hệ **“is-a”** phù hợp.

Trong `ex03_inheritance.py`:

- `Animal` là class cơ sở có thuộc tính `name`.
- `Dog` kế thừa `Animal` và bổ sung method `speak()`.
- `isinstance(dog, Animal)` minh họa rằng một object `Dog` cũng là một `Animal`.

Không nên dùng kế thừa chỉ để tái sử dụng code nếu quan hệ giữa hai class không hợp lý.

## Chạy các bài tập

Chạy các lệnh sau từ thư mục gốc repository:

```bash
python weeks/week-14-oop-essentials/exercises/ex01_classes.py
python weeks/week-14-oop-essentials/exercises/ex02_composition.py
python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
```

Chạy machine check của tuần:

```bash
python weeks/week-14-oop-essentials/checks/check_week.py
```

## Những điều cần nhớ

- Chỉ tạo class khi nó giúp nhóm dữ liệu và hành vi liên quan rõ ràng hơn.
- Giữ trạng thái object hợp lệ bằng cách kiểm tra dữ liệu đầu vào.
- Ưu tiên composition khi muốn thay đổi hành vi linh hoạt.
- Dùng inheritance khi thật sự có quan hệ “is-a”.
- Chạy code và kiểm tra kết quả để có bằng chứng rằng chương trình hoạt động như mong đợi.

## Cấu trúc nội dung tuần 14

- `notes.md`: ghi chú lý thuyết.
- `examples/`: ví dụ minh họa.
- `exercises/`: ba bài tập thực hành.
- `solutions/`: lời giải tham khảo.
- `checks/`: kiểm tra tự động.
- `mini-project/`: bài thực hành tổng hợp.

