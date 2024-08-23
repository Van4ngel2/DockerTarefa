# app.py
from flask import Flask, render_template_string
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Gerar gráfico
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.figure(figsize=(6,4))
    plt.plot(x, y, marker='o')
    plt.title('Gráfico Simples')
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # Salvar gráfico em um buffer de memória
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # HTML com gráfico
    html = '''
    <html>
    <body>
        <h1>Gráfico Simples</h1>
        <img src="data:image/png;base64,{{ img_data }}" />
    </body>
    </html>
    '''
    
    return render_template_string(html, img_data=img_data)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
