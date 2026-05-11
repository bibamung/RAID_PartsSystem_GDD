import base64
import pandas as pd
import io

def update_gdd():
    html_path = r'c:\Users\worni\Desktop\Ai_GDD\RAID_GDD\Parts_System_GDD_김성원.html'
    b64_path = r'c:\Users\worni\Desktop\Ai_GDD\RAID_GDD\scratch\pickup_result_b64.txt'
    csv_path = r'c:\Users\worni\Desktop\Ai_GDD\RAID_GDD\scratch\ui_desc_output.csv'

    # Read HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Read Base64
    with open(b64_path, 'r') as f:
        b64_str = f.read().strip()

    # Read CSV and format table
    df = pd.read_csv(csv_path, encoding='utf-8-sig')
    
    # Process the data to handle the multi-line descriptions correctly
    # The CSV structure from previous view:
    # 1.0, 1회 뽑기 결과창, "description..."
    # 2.0, 확인 버튼, "description..."
    # etc.
    
    table_rows = ""
    # Hardcoding the table construction based on the CSV data read earlier
    data = [
        ("1", "1회 뽑기 결과창", "- 뽑기 또는 보상 획득 시 결과 파츠를 중앙에 출력합니다.<br>&nbsp;&nbsp;&nbsp;&nbsp;&gt; 파츠 아이콘 표시<br>&nbsp;&nbsp;&nbsp;&nbsp;&gt; 파츠 이름 표시<br>&nbsp;&nbsp;&nbsp;&nbsp;&gt; 파츠 등급 색상 적용 (예: 전설 등급 → 노란색)<br><br>- 파츠 획득 시 등급에 따른 연출을 출력합니다.<br>&nbsp;&nbsp;&nbsp;&nbsp;&gt; 희귀도별 이펙트 출력 가능<br>&nbsp;&nbsp;&nbsp;&nbsp;&gt; 등장 애니메이션 재생 가능<br><br>- 획득한 파츠를 중앙 강조 형태로 출력합니다."),
        ("2", "확인 버튼", "- 획득 결과 화면을 종료합니다.<br>&nbsp;&nbsp;&nbsp;&nbsp;&gt; 버튼 선택 시 결과창 종료 진행"),
        ("3", "10회 뽑기 결과창", "- 다중 뽑기 시 획득한 파츠 목록을 출력<br>&nbsp;&nbsp;&nbsp;&nbsp;&gt; 그리드 형태 출력 (최대 10개)<br><br>- 각 파츠의 정보를 함께 출력<br>&nbsp;&nbsp;&nbsp;&nbsp;&gt; 파츠 아이콘, 이름, 등급 색상<br><br>- 파츠 등급에 따라 배경 색상을 구분<br>&nbsp;&nbsp;&nbsp;&nbsp;&gt; 파츠 아이콘/이름 표시 및 등급별 색상 적용<br><br>- 획득 순서 기준으로 출력 (좌→우, 상→하)")
    ]

    for no, title, desc in data:
        table_rows += f"""                            <tr>
                                <td style="text-align: center;">{no}</td>
                                <td><strong>{title}</strong><br>{desc}</td>
                            </tr>
"""

    new_content = f"""            <div style="position: relative; margin-top: 20px;">
                <!-- 상단 고정 이미지 영역 -->
                <div style="position: sticky; top: 0; z-index: 100; background-color: var(--bg-panel); padding: 15px 0; border-bottom: 2px solid var(--accent-primary); margin-bottom: 20px;">
                    <div style="text-align: center;">
                        <img src="data:image/png;base64,{b64_str}" alt="뽑기 결과창 UI" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); cursor: zoom-in;" onclick="window.open(this.src)">
                        <p style="color: var(--text-dim); font-size: 0.85rem; margin-top: 10px;">[그림 3.2.3] 뽑기 결과창 UI 구성 (1회 / 10회)</p>
                    </div>
                </div>

                <div style="margin-top: 10px;">
                    <h4 id="sec-3-2-3-1" style="font-size: 1.1rem; color: var(--text-bright);">UI 상세 설명</h4>
                    <table class="code-table">
                        <thead>
                            <tr>
                                <th style="width: 10%; text-align: center;">번호</th>
                                <th>설명 및 기능 정의</th>
                            </tr>
                        </thead>
                        <tbody>
{table_rows}                        </tbody>
                    </table>
                </div>
            </div>
"""

    # Target line 1875: <p><em>(내용 작성 예정 - 빈 섹션)</em></p>
    # We want to replace this line.
    for i, line in enumerate(lines):
        if 'id="sec-3-2-3"' in line:
            # Found the header, replace the next paragraph line (i+1)
            lines[i+1] = new_content
            break
            
    with open(html_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Successfully updated GDD HTML.")

if __name__ == "__main__":
    update_gdd()
