ma = int(input("Nhap ma dan toc: "))

dan_toc = {
    1: "Dan toc Kinh",
    2: "Dan toc Tay",
    3: "Dan toc Nung",
    4: "Dan toc Thai",
    5: "Dan toc Khome"
}

print(dan_toc.get(ma, "Dan toc khong xac dinh"))
