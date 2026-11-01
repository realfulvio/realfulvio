from pathlib import Path
import base64, subprocess, html
root=Path(__file__).parent
def embedded(name,x,y,w,h):
 data=(root/'assets/source'/name).read_bytes(); mime='image/svg+xml' if name.endswith('.svg') else 'image/png'
 return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="data:{mime};base64,{base64.b64encode(data).decode()}"/>'
def save(name,w,h,body):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'
 path=root/'assets'/f'{name}.svg';path.write_text(svg)
 subprocess.run(['rsvg-convert','-o',str(root/'assets'/f'{name}.png'),str(path)],check=True)
save('officina-banner',1600,440,'<rect width="1600" height="440" fill="#0f171d"/><path d="M0 0H1260L1050 440H0Z" fill="#005e8e"/><path d="M1260 0H1325L1115 440H1050Z" fill="#f2c230"/><text x="66" y="73" font-family="monospace" font-size="21" letter-spacing="4" fill="#f2c230">SOFTWARE / SISTEMI / ESPERIMENTI</text>'+embedded('hcok-real-white.svg',66,136,760,123)+'<text x="66" y="348" font-family="sans-serif" font-size="27" fill="#d9e8f1">Sistemista di giorno. Smanettone di notte.</text>')
projects=[('cedro','cedro.svg','CEDRO','Conversione file sul PC, offline.'),('tracepunk','tracepunk.svg','TRACE//PUNK','Strumenti OSINT nel browser.'),('tracciadoc','tracciadoc.png','TracciaDoc','Ricerca documenti e OCR locale.'),('mouse-macro','mouse.png','Mouse Macro','Registra e ripeti le azioni del mouse.'),('assistenza-portale','assistenza.svg','Assistenza Portale','Richieste guidate e assistenza GLPI.'),('smart-working','rendiconto.png','Smart Working','Resoconti del lavoro agile per enti.')]
for slug,icon,title,desc in projects:
 save(slug,760,190,'<rect x="1" y="1" width="758" height="188" fill="#141d24" stroke="#244353" stroke-width="2"/><rect width="760" height="5" fill="#f2c230"/>'+embedded(icon,32,54,78,78)+f'<text x="140" y="85" font-family="sans-serif" font-size="34" font-weight="bold" fill="#e6edf3">{html.escape(title)}</text><text x="140" y="130" font-family="sans-serif" font-size="23" fill="#a9b6c2">{html.escape(desc)}</text>')
print('Banner e sei schede renderizzati dagli originali')
