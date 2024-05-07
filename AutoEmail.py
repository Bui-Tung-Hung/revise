import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_info():
    email = input("Insert your Email Address: ")
    password = input("Insert your App Password: ")
    Sender = input("Insert your Name: ")
    Phone_number = input("Insert your Phone Number")
    Category = input("Insert your Category: ")
    return email, password, Sender, Phone_number, Category
email = "buitunghung123@gmail.com"
password = "tpuc dyds aufc uigw"
receiver = ["npngvein12@gmail.com", "npngvein@gmail.com", "anhphat@flytoskycharity.vn"]

session = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls()
session.login(email, password)

Unit_name = ["Công ty TNHH Thương Mại VKU", "Cỏ Huỳnh Lâm", "Ekko green"]
for i in range(len(Unit_name)):
    Sender = "Bùi Tùng Hưng"
    Phone_number = "0852366778"
    Category = "sản phẩm tái chế từ nhựa, nilon"
    # Create the email message
    content = f'''<span style="color: #000000;">Kính gửi:</span> <span style="color: #FF0000;">{Unit_name[i]}</span><br><br>
    <span style="color: #000000;">Em tên là</span> <span style="color: #FF0000;">{Sender}</span> <span style="color: #000000;">– Đại diện phụ trách Đối ngoại của Chương trình “Đổi sách lấy cây” năm 2024 do Nhóm từ thiện Fly To Sky, trực thuộc Trung tâm Tình nguyện Quốc gia (Trung ương Đoàn TNCS Hồ Chí Minh) tổ chức</span>.<br><br>
    <span style="color: #000000;">Lời đầu tiên, thay mặt Nhóm từ thiện Fly To Sky, Ban Điều hành, Ban Tổ chức Chương trình xin được gửi đến Quý vị lời chào thân ái và trân trọng nhất. Kính chúc Quý vị được dồi dào sức khỏe, hạnh phúc, thành công và phát triển bền vững</span>.<br><br>
    <span style="color: #000000;">Nhóm từ thiện Fly To Sky xin trân trọng gửi tới Quý đơn vị lời mời tài chợ <b>Chương trình “Đổi sách lấy cây” năm 2024</b> - Một chương trình thường niên do Nhóm từ thiện Fly To Sky (Thành viên các Mạng lưới Tình nguyện Quốc gia, trực thuộc Trung tâm Tình nguyện Quốc gia – T.Ư Đoàn TNCS Hồ Chí Minh) khởi xướng và phát triển kể từ năm 2019. Năm 2024 là năm thứ 06 Nhóm tổ chức Chương trình.<br><br></span>
    <span style="color: #000000;">Thông qua chương trình, FTS mong muốn góp phần hỗ trợ sách cho giáo dục vùng cao, tạo động lực tiếp bước các học sinh nghèo có điều kiện tham gia học tập, gia tăng tỷ lệ học sinh đến trường, duy trì sĩ số ở các điểm trường khó khăn, đặc biệt khó khăn; cải thiện, nâng cao chất lượng học tập. Bên cạnh đó góp phần lan tỏa các thông điệp bảo vệ môi trường, biết yêu thiên nhiên, chăm sóc và bảo vệ cây xanh, bảo vệ rừng, tạo thói quen sử dụng ít nhựa, tiêu dùng xanh, lối sống bảo vệ môi trường, chuyển đổi sử dụng các sản phẩm thân thiện với môi trường, thuần chay, có nguồn gốc từ thực vật, hữu cơ, sản xuất và tiêu dùng bền vững, đẩy mạnh tái chế và giảm thiểu rác thải. Mỗi năm chương trình đã hỗ trợ hàng trăm trẻ em vùng cao có sách giáo khoa để học vào đầu năm học mới, thành lập, đồng hành cùng hàng chục thư viện trường học, thư viện cộng đồng, cùng với đó thu hút hàng ngàn người tham gia quy đổi và tham gia tình nguyện.<br><br></span>
    <span style="color: #000000;">Năm 2024, Chương trình dự kiến tổ chức từ ngày 11/5/2024 đến ngày 28/7/2024 (Tổng cộng khoảng 35 ngày, kéo dài 12 tuần), vào các ngày thứ 4, 7 và Chủ nhật (Các tỉnh miền núi sẽ thứ 7 và Chủ nhật) và dự kiến tổ chức tại 40 điểm đổi tại 8-10 tỉnh, thành phố, trong đó trọng tâm tại Gia Lai, TP. Hồ Chí Minh, ngoài ra còn có Thủ đô Hà Nội, Bình Dương,…<br><br></span>
    <span style="color: #000000;">Xin trân trọng kính mời</span> <font color="#FF0000;">{Unit_name[i]}</font> <span style="color: #000000;">tài trợ sản phẩm các sản phẩm tái chế từ nhựa, nilon<br><br>
    <span style="color: #000000;">Phía BTC cũng rất mong có cơ hội được trao đổi, thống nhất về phương án, quyền lợi với phía mình.<br><br></span>
    <span style="color: #000000;">Thông tin chi tiết và các gói tài trợ:</span> <a href="https://heyzine.com/flip-book/7797f3c85a.html">https://heyzine.com/flip-book/7797f3c85a.html</a><br><br>
    <span style="color: #000000;">Sự đồng hành của Quý đơn vị chính là động lực hỗ trợ Nhóm từ thiện Fly To Sky tổ chức Chương trình ý nghĩa, đạt hiệu quả, đóng góp tích cực cho cộng đồng. Để làm được điều đó, chúng tôi rất mong có cơ hội hợp tác, nhận được sự quan tâm, đồng hành, ủng hộ của Quý vị.<br><br>
    Vì quy mô chương trình sẽ tổ chức ở nhiều địa bàn nên công tác chuẩn bị cần được hoàn tất trước kỳ nghỉ lễ, rất mong sớm nhận được sự phản hồi của Quý vị <b>trước ngày 03/05/2024</b> ạ.<br><br>

    Trân trọng cảm ơn!<br><br>
    ---------<br></span>
    <span style="color: #FF0000;">{Sender}</span><br>
    <span style="color: #000000;">Đại diện phụ trách Đối ngoại của Chương trình “Đổi sách lấy cây” năm 2024 do Nhóm từ thiện Fly To Sky, trực thuộc Trung tâm Tình nguyện Quốc gia (Trung ương Đoàn TNCS Hồ Chí Minh) tổ chức</span><br>
    <span style="color: #000000;">Số điện thoại:</span> <span style="color: #FF0000;">{Phone_number}</span><br>
    <span style="color: #000000;">Email công:</span> <span style="color: #FF0000;">donghanh@flytoskycharity.vn</span>
    '''



    msg = MIMEMultipart('alternative')
    msg['From'] = email
    msg['To'] = receiver[i]
    msg['Subject'] = "FLYTOSKY MỜI TÀI TRỢ CHƯƠNG TRÌNH ĐỔI SÁCH LẤY CÂY NĂM 2024"

    # Attach HTML content
    msg.attach(MIMEText(f"<h1>{msg['Subject']}</h1>", 'html'))
    msg.attach(MIMEText(content, 'html'))
    
    # Connect to SMTP server
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(email, password)

    # Send email
    session.sendmail(email, receiver[i], msg.as_string())
    print(f"Mail no {i} Sent")

    # Quit SMTP session
    session.quit()