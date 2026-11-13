import shopping_data as sd

def test_add_item():
    items = []
    result = sd.add_item(items, 'яблоки')
    assert result == ['яблоки']

def test_total():
    prices = {
        'яблоки': 50,
        'бананы': 200
    }
    result = sd.total(prices)
    assert result == 250

def test_mark_bought():
    bought = set()
    sd.mark_bought(bought, 'хлеб')
    sd.mark_bought(bought, 'хлеб')
    assert bought == {'хлеб'}

def test_expensive():
    items = [
        'хлеб',
        'молоко',
        'сыр'
    ]
    prices = {
        'хлеб': 50,
        'молоко': 100,
        'сыр': 150
    }
    result = sd.expensive(items, prices)
    assert result == ['сыр']