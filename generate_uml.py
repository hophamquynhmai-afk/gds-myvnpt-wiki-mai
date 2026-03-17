import zlib
import base64
import requests

plantuml_code = """
@startuml
skinparam shadowing false
skinparam ParticipantPadding 20
skinparam BoxPadding 10
skinparam ParticipantBackgroundColor #DAE8FC
skinparam ParticipantBorderColor #6C8EBF
skinparam SequenceLifeLineBorderColor #6C8EBF
skinparam SequenceGroupBodyBackgroundColor transparent
skinparam ArrowColor black
skinparam defaultFontName Arial

participant ":Khách hàng" as User
participant ":MyVNPT" as App
participant ":Hệ thống" as Sys
participant ":Cổng SMS" as SMS

User -> App: Thanh toán thành công
activate App
App -> Sys: Gửi API kiểm tra điều kiện CTKM
activate Sys
Sys -> Sys: Kiểm tra điều kiện

Sys --> App: Trả trạng thái Hợp lệ
deactivate Sys

App --> User: Hiển thị Banner/Box nhận voucher
deactivate App

User -> App: Click "Nhận voucher"
activate App

App -> Sys: Gửi request cấp mã Voucher
activate Sys

Sys -> Sys: Cấp mã & Lưu vào kho quà

Sys -> SMS: Yêu cầu gửi SMS
activate SMS
SMS --> User: Gửi SMS chứa mã Voucher Grab
deactivate SMS

Sys --> App: Trả kết quả thành công
deactivate Sys

App --> User: Popup nhận quà thành công
App --> User: Hiển thị trạng thái đã nhận
deactivate App

@enduml
"""

def generate_diagram(code, filename):
    compressed = zlib.compress(code.encode('utf-8'))
    payload = base64.urlsafe_b64encode(compressed).decode('utf-8')
    url = f"https://kroki.io/plantuml/png/{payload}"
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Saved to {filename}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    generate_diagram(plantuml_code, "c:/Users/caida/gds-myvnpt-wiki/Voucher_Grab_Sequence.png")
