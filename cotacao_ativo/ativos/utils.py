import yfinance as yf

def obter_cotacao(codigo_ativo):
    try:
        ativo = yf.Ticker(codigo_ativo)
        cotacao = ativo.history(period='1d')['Close'].iloc[-1]
        return cotacao
    except Exception as e:
        print(f"Erro ao obter cotação para {codigo_ativo}: {e}")
        return None
    
