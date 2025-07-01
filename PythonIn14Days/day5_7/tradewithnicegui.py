from nicegui import ui
import httpx

# A simple in-memory leaderboard
leaderboard = []

# Get current Bitcoin price from CoinGecko
async def get_btc_price():
    try:
        response = await httpx.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        return response.json()['bitcoin']['usd']
    except:
        return "Error"

# Title
ui.label('📊 Crypto Prediction App').classes('text-2xl font-bold mb-4')

price_label = ui.label('Fetching BTC price...').classes('text-lg mb-2')

# Update BTC price every 10 seconds
async def update_price():
    while True:
        price = await get_btc_price()
        price_label.text = f'🪙 Current BTC Price: ${price}'
        await ui.sleep(10)

ui.timer(0.1, update_price)

# Input prediction
name_input = ui.input('Your name').props('outlined')
prediction_input = ui.select(['Up', 'Down'], label='Your BTC Prediction').props('outlined')

def submit_prediction():
    name = name_input.value
    pred = prediction_input.value
    if name and pred:
        leaderboard.append((name, pred))
        update_leaderboard()
        name_input.value = ''
        prediction_input.value = None

ui.button('Submit Prediction', on_click=submit_prediction).classes('mt-2')

# Leaderboard
leaderboard_column = ui.column().classes('mt-8')
ui.label('📈 Prediction Leaderboard').classes('text-xl font-semibold')

def update_leaderboard():
    leaderboard_column.clear()
    for idx, (name, pred) in enumerate(reversed(leaderboard), 1):
        leaderboard_column.label(f'{idx}. {name} → {pred}').classes('text-md')

# Run the app
ui.run()
