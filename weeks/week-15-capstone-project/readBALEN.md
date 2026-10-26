# Tuần 15 — Tóm tắt Capstone Project

## Tuần 15 làm gì?

Tuần 15 là tuần tổng kết Python Journey. Mục tiêu không phải học thêm thật nhiều cú pháp, mà dùng kiến thức đã học để hoàn thiện một chương trình giải quyết vấn đề rõ ràng, chạy được, kiểm thử được và có thể giải thích.

Đề bài, yêu cầu nộp và rubric chính thức nằm trong [FINAL_PROJECT.md](../../FINAL_PROJECT.md). Tuần 15 không có bộ bài tập nhỏ hoặc lời giải chính thức; sản phẩm chính là capstone của người học.

## 1. Xây dựng và tích hợp dự án

- Viết problem statement: dự án giải quyết vấn đề gì và dành cho ai.
- Chốt phạm vi, ghi rõ những gì chưa làm (out of scope).
- Hoàn thiện ít nhất **4 chức năng nghiệp vụ có ý nghĩa**.
- Chia logic thành hàm và module có trách nhiệm rõ ràng.
- Chọn cấu trúc dữ liệu phù hợp; dùng class khi thật sự giúp mô hình hóa vấn đề tốt hơn.
- Nếu cần lưu dữ liệu, sử dụng file như JSON hoặc CSV và xử lý tình huống dữ liệu bị thiếu hoặc sai định dạng.

## 2. Kiểm thử và debug

- Viết ít nhất **5 test có ý nghĩa** cho logic chính.
- Kiểm tra normal case, edge case và input không hợp lệ.
- Đọc traceback để tìm nguyên nhân, sửa lỗi và giữ regression test để ngăn lỗi quay lại.
- Phân biệt lỗi phần mềm với giới hạn đã biết của dự án.
- Không dùng bare `except:` hoặc `except: pass` để che lỗi.

## 3. Viết README cho dự án

README của capstone cần giúp người khác tự chạy được project, gồm:

- Vấn đề và phạm vi dự án.
- Danh sách chức năng chính.
- Hướng dẫn cài đặt, chạy chương trình và chạy test.
- Ví dụ input/output có thể tái hiện.
- Cấu trúc file/module và quyết định thiết kế quan trọng.
- Kết quả kiểm thử, một lỗi đã sửa và các giới hạn còn lại.
- Thông tin sử dụng AI, nếu có.

Có thể tham khảo [capstone README template](../../templates/capstone-readme-template.md).

## 4. Ghi lại việc sử dụng AI

Tạo file `AI_USAGE.md` trong dự án và trả lời:

1. AI đã hỗ trợ những việc gì?
2. Mình đã tự viết hoặc thay đổi phần nào?
3. Mình kiểm chứng code và lời gợi ý của AI bằng cách nào?
4. Mình hiểu rõ hơn điều gì sau khi làm dự án?

Quan trọng nhất là hiểu và kiểm chứng sản phẩm, không chỉ sao chép code.

Mẫu tham khảo: [AI_USAGE.template.md](../../templates/AI_USAGE.template.md).

## 5. Dùng Git/GitHub để lưu bằng chứng

- Tạo các commit nhỏ, có nội dung mô tả rõ ràng.
- Lịch sử commit nên thể hiện quá trình xây dựng, kiểm thử, sửa lỗi và cải tiến.
- Không commit secrets, file tạm hoặc môi trường ảo.
- Kiểm tra `git status` trước khi bàn giao.

## 6. Chạy capstone readiness check

Từ thư mục gốc repository, chạy:

```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py path/to/my-project
```

Thay `path/to/my-project` bằng đường dẫn tới thư mục dự án của bạn.

Readiness check kiểm tra một số bằng chứng cơ học như README, `AI_USAGE.md`, số lượng hàm và test, khả năng collect test bằng pytest, và bare `except:`. Kết quả PASS **không đồng nghĩa dự án được chấm điểm tối đa**; rubric và review chính thức vẫn nằm trong [FINAL_PROJECT.md](../../FINAL_PROJECT.md).

## 7. Capstone tham khảo trong repository

Repository có track tùy chọn [VuaCóc Bot Journey](../../projects/vuacoc-bot-journey/README.md). Track này kết nối kiến thức từ tuần 7 đến tuần 15 bằng bot, local arena, match, replay, tournament và evaluation.

Đây là mô hình học tập chạy local; nó **không tuyên bố tương thích với runtime production của VuaCóc**. Người học vẫn có thể chọn một đề tài capstone khác miễn đáp ứng yêu cầu trong `FINAL_PROJECT.md`.

## Checklist trước khi nộp

- [ ] Chương trình chạy được và có ít nhất 4 chức năng nghiệp vụ.
- [ ] Logic được chia thành hàm/module hợp lý.
- [ ] Có ít nhất 5 test có ý nghĩa và đã chạy test.
- [ ] Đã thử các trường hợp biên và input sai.
- [ ] Có README hướng dẫn setup, usage và test.
- [ ] Có `AI_USAGE.md`.
- [ ] Ghi lại giới hạn đã biết và ít nhất một bug đã xử lý.
- [ ] Git history dễ review, không có secrets hoặc file tạm.
- [ ] Có thể giải thích code, test và các quyết định thiết kế của mình.

## Kết luận

Sau tuần 15, mục tiêu là chuyển từ **biết cú pháp Python** sang **biết dùng Python giải quyết một vấn đề, kiểm chứng chương trình, sửa lỗi và giải thích vì sao giải pháp hoạt động**.

Vòng lặp làm việc xuyên suốt khóa học:

```text
Learn → Build → Test → Debug → Improve → Commit → Prove
```
