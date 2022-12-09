import TradingAPI


#get_market_movements(polygon_client)
#client = boto3.client('dynamodb')
#view_avaliable_symbols()    
#view_favorite_symbol()
#get_market_movements(polygon_client,'AAPL',"2022-04-01","2022-04-02")
#save_market_CSV(polygon_client,'APPL')
#view_market(polygon_client,'APPL')

def run_view_avaliable_symbols():
    TradingAPI.view_avaliable_symbols()

def run_view_favorite_symbol():
    TradingAPI.view_favorite_symbol(3)

def run_view_market():
    symbol=input("Please type a trading symbol ")
    startdate=input("Please type a starting date (YYYY-MM-DD) ")
    finishdate=input("Please type a starting date (YYYY-MM-DD) ")
    TradingAPI.view_market(symbol,startdate,finishdate)

def run_save_market_CSV():
    symbol=input("Please type a trading symbol ")
    TradingAPI.save_market_CSV(symbol)

def show_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOptions")
    print("1. Check all avaliable symbols")
    print("2. Check your favorite Symbols")
    print("3. Check Stock Price")
    print("4. Download market data (CSV)")
    print("5. Quit")

def start_app():
    """Ejecuta el programa para el usuario."""
    continuar = True
    canciones = list()
    while continuar:
        show_menu()
        opcion_seleccionada = int(input("Please select an option: "))
        if opcion_seleccionada == 1:
            run_view_avaliable_symbols()
        elif opcion_seleccionada == 2:
            run_view_favorite_symbol()
        elif opcion_seleccionada == 3:
            run_view_market()
        elif opcion_seleccionada == 4:
            run_save_market_CSV()
        elif opcion_seleccionada == 5:
            continuar = False
        else:
            print("Please select a valid option")

#PROGRAMA PRINCIPAL
start_app()