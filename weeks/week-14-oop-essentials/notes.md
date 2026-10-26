# Week 14 — OOP essentials

Mục tiêu của tuần này không phải biến mọi thứ thành class. Ta học cách gom
dữ liệu và hành vi có liên quan, rồi chọn cách tổ chức đơn giản nhất giải
quyết được bài toán.

## 1. Class, object và responsibility

- **Class** là bản mô tả cách tạo ra một loại object.
- **Object** là một instance cụ thể được tạo từ class.
- **Attribute** là dữ liệu gắn với object.
- **Method** là function được định nghĩa trong class và thường làm việc với
  object đó.
- `self` là tham chiếu tới instance hiện tại; Python truyền nó tự động khi
  gọi một instance method như `progress.percentage()`.

```python
class Progress:
    def __init__(self, completed: int, total: int):
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100
```

Khi chạy `progress = Progress(3, 4)`, Python tạo object và gọi `__init__`
để thiết lập state ban đầu. `completed` và `total` trở thành instance
attributes, nên mỗi object giữ dữ liệu riêng.

Một class hữu ích khi dữ liệu và những thao tác liên quan thường đi cùng nhau.
Nếu chỉ cần lưu vài giá trị một lần, dict hoặc tuple có thể đơn giản hơn.

## 2. `__str__` và state hợp lệ

`__str__` định nghĩa biểu diễn thân thiện khi dùng `print(object)`. Nó nên
trả về string và không nên thực hiện side effect.

```python
def __str__(self) -> str:
    return f"Progress: {self.completed}/{self.total}"
```

Object nên có state hợp lệ ngay sau khi được tạo. Ví dụ, tiến độ không thể có
tổng bằng 0 hoặc số mục hoàn thành nằm ngoài khoảng từ 0 đến tổng. Ta có thể
báo lỗi rõ ràng bằng `ValueError` ngay trong `__init__`.

## 3. Composition — ghép object với collaborator

**Composition** là khi một object chứa hoặc nhận một object/function khác để
ủy quyền một phần công việc. Trong ví dụ bot, class `Bot` điều phối việc chọn
action, còn strategy quyết định action cụ thể.

```python
class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)
```

`Bot` không cần biết strategy được cài đặt thế nào. Nó chỉ cần biết strategy
nhận state và trả về action. Nhờ vậy ta có thể thay đổi hành vi mà không sửa
class `Bot` hoặc arena.

Đây là **composition over inheritance**: ghép các thành phần nhỏ trước khi
xây dựng cây kế thừa. Strategy trong tuần này có thể chỉ là function; không
cần tạo class riêng cho từng strategy.

## 4. Strategy swap: ba policy minh họa

Với course-local Line Arena, action hợp lệ là `left`, `right` và `wait`.
State có `position`, `opponent_position` và `goal`.

- **defensive**: chờ nếu đối thủ cách một bước hoặc ít hơn; nếu không thì tiến
  về goal.
- **balanced**: luôn chọn bước hướng về goal.
- **aggressive**: nếu đối thủ cách tối đa hai bước thì tiến về phía đối thủ;
  nếu không thì tiến về goal.

Các policy này dùng để so sánh cách đóng gói hành vi, không phải khẳng định
aggressive luôn chơi tốt hơn. Vì goal có thể là `0` hoặc `4`, đừng hardcode
`"right"`: hãy so sánh `position` với `goal` để quyết định hướng đi.

## 5. Basic inheritance — chỉ khi quan hệ “is-a” rõ

Inheritance cho phép class con nhận hành vi và dữ liệu từ class cha, rồi bổ
sung hành vi riêng.

```python
class Animal:
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"
```

Dog là một loại Animal, nên quan hệ “is-a” tự nhiên. Không dùng inheritance
chỉ để chia sẻ vài dòng code; nếu muốn thay đổi một hành vi độc lập, composition
thường linh hoạt hơn.

## 6. Cách tự kiểm tra

Sau mỗi thay đổi:

1. Chạy ví dụ liên quan.
2. Chạy machine check:
   `python weeks/week-14-oop-essentials/checks/check_week.py`
3. Nếu sai, đọc assertion hoặc traceback để tìm hành vi không khớp.
4. Thử cả goal ở hai đầu (`0` và `4`) và trường hợp đã ở goal.
5. Giải thích được vì sao class chịu trách nhiệm điều phối, còn strategy chịu
   trách nhiệm quyết định.

Tuần này không học inheritance hierarchy phức tạp, design patterns, metaclass,
descriptor hay framework trừu tượng.
