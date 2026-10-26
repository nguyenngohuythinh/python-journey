class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print(self.MaMay, self.TenMay, self.HangSanXuat,
              self.DungLuongPin, self.GiaBan)


dt1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
dt2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

dt1.thongtindienthoai()
dt2.thongtindienthoai()
