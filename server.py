from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import pandas as pd,json,os
BASE=os.path.dirname(os.path.abspath(__file__)); XLSX=os.path.join(BASE,'FASTAG_FINAL_REAL_CUSTOMER_QUERY_ANALYSIS.xlsx')
class H(SimpleHTTPRequestHandler):
 def do_GET(self):
  if self.path.startswith('/api/data'):
   l1=pd.read_excel(XLSX,'L1_Overall').fillna(''); l2=pd.read_excel(XLSX,'L2_All').fillna(''); l3=pd.read_excel(XLSX,'L3_All_Actual_Queries').fillna('')
   if 'Date' in l3: l3['Date']=pd.to_datetime(l3['Date'],errors='coerce').dt.strftime('%d-%b-%Y').fillna('')
   b=json.dumps({'l1':l1.to_dict('records'),'l2':l2.to_dict('records'),'l3':l3.to_dict('records'),'source':os.path.basename(XLSX)},ensure_ascii=False).encode()
   self.send_response(200); self.send_header('Content-Type','application/json; charset=utf-8'); self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(b); return
  super().do_GET()
os.chdir(BASE); print('Open http://127.0.0.1:5500/index.html'); ThreadingHTTPServer(('127.0.0.1',5500),H).serve_forever()
