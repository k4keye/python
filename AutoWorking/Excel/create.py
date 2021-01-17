from openpyxl import Workbook

wb = Workbook() # 새 워크북 생성 = 엑셀 생성
ws = wb.active # 형재 활성화된 시트를 가져온다. 엑설의 첫 시트

ws.title = "first" #시트명
wb.save("test.xlsx") # 엑셀저장  시트를 저장하는게 아니라 엑셀을 저장해야한다.
wb.close() # 종료