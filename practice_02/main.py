def words_per_page(words, pages):
    """Возвращает среднее число слов на одной странице."""
    if pages == 0:
        return "На ноль делить нельзя"
    return words / pages

assert words_per_page(1200, 4) == 300.0                  
assert words_per_page(500, 0) == "На ноль делить нельзя"  
assert words_per_page(750, 5) == 150.0                   

# Сортировка слов по длине
words = ["шум", "звук", "мелодия"]
result = sorted(words, key=lambda word: len(word))
print(result)
