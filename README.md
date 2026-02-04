# Education Games (HTML)

Browserbasierte Lernspiele (Single-File-HTML) zu KI-Sicherheit, Datenschutz, SQL, Python und Medienkompetenz.

## Starten

### Direkt im Browser
Viele Spiele funktionieren per Doppelklick.

### Empfohlen: lokaler Webserver
Manche Browser blocken Features bei `file://` oder laden Assets zuverlässiger über HTTP.

```bash
python -m http.server 8000
Dann öffnen:

http://localhost:8000/

Ordnerstruktur
ai-security/ – KI-Sicherheit & Prompting-Awareness

data-protection/ – Datenschutz-Formate (u.a. VHS)

sql/ – SQL-Lernspiele (SELECT/FROM, WHERE, JOIN)

python/ – Python/Data-Themen (z.B. NumPy)

logic-and-math/ – Kombinatorik/Logik

media-literacy/ – Medienkompetenz / kritisches Denken

generic/ – Platz für themenoffene Demos

libs/ – gemeinsame Bibliotheken (falls genutzt)

Spiele (Auswahl / Überblick)
AI Security (ai-security/)
as-marketing_lernmaterial_spiele_ki-sicherheit-01_data-defender.html

as-marketing_lernmaterial_spiele_ki-sicherheit-02_prompt-puzzler.html

as-marketing_lernmaterial_spiele_ki-sicherheit-03_fake-or-fact.html

Data Protection (data-protection/)
as-marketing_lernmaterial_spiele_vhs-datenschutz_chat-raetsel.html

as-marketing_lernmaterial_spiele_vhs-datenschutz_hook.html

as-marketing_lernmaterial_spiele_vhs-datenschutz_industry-tool.html

as-marketing_lernmaterial_spiele_vhs-datenschutz_speed-quiz.html

as-marketing_lernmaterial_spiele_vhs-datenschutz_tarffic-light-quiz.html

VHS_Game_DataDefender.html

VHS_Game_FakeOrFact.html

SQL (sql/)
as-marketing_lernmaterial_spiele_sql_select-from.html

as-marketing_lernmaterial_spiele_sql_where.html

as-marketing_lernmaterial_spiele_sql_join.html

Python (python/)
as-marketing_lernmaterial_spiele_numpy-arrays.html

Logic & Math (logic-and-math/)
as-marketing_lernmaterial_spiele_kombinatorik.html

Media Literacy (media-literacy/)
as-marketing_lernmaterial_spiele_monalisa.html

Abhängigkeiten / Assets
Die Spiele sind grundsätzlich „static“ (kein Build). Einige Dateien binden Bibliotheken oder Assets per CDN ein (z.B. Fonts, Tailwind, html2canvas).

Hinweis: Three.js (Kombinatorik)
logic-and-math/as-marketing_lernmaterial_spiele_kombinatorik.html erwartet lokal:

logic-and-math/libs/three.min.js

Wenn du Offline-Nutzung willst: Datei hinzufügen.
Alternativ im HTML auf einen CDN-Link umstellen.

Optional: Development (Live Reload)
pip install -r requirements.txt
livereload
Lizenz
TODO: Lizenz ergänzen (z.B. MIT) + ggf. Hinweise zu Marken/CI.
⚠️ WebGL-Hinweis (für Kombinatorik-Spiel)
Dieses Spiel nutzt WebGL via Three.js.
Der Browser muss Hardwarebeschleunigung aktiviert haben.
