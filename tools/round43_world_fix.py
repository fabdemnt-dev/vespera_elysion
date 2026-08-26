from pathlib import Path
from bs4 import BeautifulSoup

p = Path('world.html')
soup = BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser')

# Current-world facts: rewrite by dt label to avoid touching historical sections.
status = soup.find(id='status')
if not status:
    raise RuntimeError('status section not found')

def set_dd(label, html_text):
    dt = next((x for x in status.find_all('dt') if x.get_text(strip=True) == label), None)
    if not dt or not dt.find_next_sibling('dd'):
        raise RuntimeError(f'status field not found: {label}')
    dd = dt.find_next_sibling('dd')
    dd.clear()
    dd.append(BeautifulSoup(html_text, 'html.parser'))

set_dd('最新新聞', '2026年8月26日号（43周目で8月25日号・26日号の本文を確認し、<a href="elysion_newspapers.md">新聞原文台帳</a>へ保存）')
set_dd('会話状態分類', '<strong>継続2組 / 終了34組</strong>（43周目 #378〜#379完了。継続2組を各8ターン再確認）。<a href="elysion_observation/conversation_status.md">36組の判定一覧</a>')
set_dd('最新周回', '43周目 #378〜#379を完了。#378 / #379とも8ターン（4+4）で観察。<a href="world/round43.html">43周目の最終world_state</a>')
set_dd('events / pending', 'raw world_state.events 50件（scene 49・moved 1） / pending 3件。scene event累計は136件。pendingは「鐘楼から、新しい一日の始まりを告げる鐘の音が響き渡った。」「鐘楼の鐘が、新しい朝の訪れを告げる音を響かせた。」「鐘楼の鐘が、夕暮れを告げる穏やかな音を響かせた。」。eventsの50件上限で古いeventが押し出されてもmovements配列8件は保持される。')
set_dd('#379終了時のaffinity', '完全rawから全36ペア・72方向の現在値を確認。継続2組は双方100 / 100。43周目#378/#379でも対象2組は100 / 100を維持。<a href="elysion_affinity.md">好感度台帳</a>に14〜43周目の各会話も記録。')
set_dd('movements', '<strong>8件</strong>。43周目の新規movementは0件。会話上のパン屋入店や駅へ向かう意図はraw movementへ補完しない。')
set_dd('turns_since_event', '6（#379終了時）')

# Historical round42 summary must remain historical, not be rewritten as round43.
r42 = soup.find(id='round42-behavior')
if not r42:
    raise RuntimeError('round42 behavior section not found')
h2 = r42.find('h2')
h2.string = '42周目 #369〜#377：終了挙動比較と最終world_state'
for li in r42.find_all('li'):
    text = li.get_text()
    if text.startswith('#377終了時：'):
        li.string = '#377終了時：weather=2026-08-24・通り雨・30℃、events=50（scene49/moved1）、movements=8、pending=3、turns_since_event=9、items/rumors/overheard=0。'
for a in r42.find_all('a'):
    if a.get('href') == 'world/round42.html':
        a.string = '🌍 42周目の詳細と最終world_state'
    if a.get('href') == 'conversations/round42.html':
        a.string = '💬 #369〜#377会話原文'

# Archive index: preserve round42 and add round43.
latest = soup.find(id='latest-rounds')
if not latest:
    raise RuntimeError('latest-rounds section not found')
latest.find('h2').string = '12〜43周目の世界記録'
a42 = latest.find('a', href='world/round42.html')
if not a42:
    raise RuntimeError('round42 archive link not found')
a42.string = '42周目 #369〜#377'
if not latest.find('a', href='world/round43.html'):
    a43 = soup.new_tag('a', href='world/round43.html')
    a43['class'] = 'chip'
    a43.string = '43周目 #378〜#379'
    latest.append(' ')
    latest.append(a43)

p.write_text(str(soup), encoding='utf-8')

# Validate current vs historical separation.
t = p.read_text(encoding='utf-8')
checks = [
    '2026年8月26日号（43周目で8月25日号・26日号の本文を確認',
    'scene event累計は136件',
    '43周目の新規movementは0件',
    '42周目 #369〜#377：終了挙動比較と最終world_state',
    '#377終了時：weather=2026-08-24・通り雨・30℃',
    '12〜43周目の世界記録',
    '>43周目 #378〜#379</a>',
]
for x in checks:
    if x not in t:
        raise RuntimeError(f'validation failed: {x}')

# Remove temporary helpers from final diff.
for helper in ['tools/round43_world_fix.py', '.github/workflows/round43-world-fix.yml']:
    q = Path(helper)
    if q.exists():
        q.unlink()
print('round43 world static repair complete')
