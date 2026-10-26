# Mini-project — Strategy Composition

## Bài toán

Tạo một class `Bot` chỉ chịu trách nhiệm giữ và gọi strategy. Strategy nhận
state của bot và trả về một action thuộc tập `left`, `right`, `wait`.
Không để class `Bot` chứa toàn bộ logic của từng policy.

## Yêu cầu

1. Tạo `Bot(strategy)` và method `choose_action(state)`.
2. Viết ba strategy:
   - **defensive**: chờ nếu đối thủ cách một bước hoặc ít hơn; nếu không thì
     tiến về goal.
   - **balanced**: tiến một bước về goal.
   - **aggressive**: nếu đối thủ cách tối đa hai bước thì tiến về phía đối thủ;
     nếu không thì tiến về goal.
3. Tạo ít nhất hai state: một state có goal là `4`, state còn lại có goal là
   `0`.
4. Chạy cùng một state qua nhiều strategy và quan sát action khác nhau.
5. Thêm kiểm tra cho trường hợp bot đã ở goal và trường hợp đối thủ ở gần.
6. Viết 2–3 câu giải thích vì sao thay strategy không yêu cầu sửa class `Bot`.

## Tiêu chí hoàn thành

- [ ] `Bot` không hardcode policy cụ thể.
- [ ] Có thể thay strategy khi tạo object hoặc gán strategy khác.
- [ ] Strategy xử lý đúng cả hai hướng goal.
- [ ] Action trả về nằm trong contract của bài học.
- [ ] Có ít nhất bốn assertion hoặc kiểm tra hành vi.
- [ ] Có thể giải thích composition và một ví dụ “is-a” phù hợp với inheritance.

## Kiểm tra solution tham khảo

Từ thư mục gốc repository:

```bash
python weeks/week-14-oop-essentials/checks/check_week.py
```

Giữ strategy là function hoặc object nhỏ. Không sửa arena core và không biến
inheritance thành kiến trúc bắt buộc.
