# Полезные команды для работы с проектом

## Очистка кеша pytest
Если pytest не находит тесты или выдает ошибки импорта, выполните:

**PowerShell (Windows):**
```powershell
Remove-Item -Recurse -Force tests\__pycache__, pages\__pycache__
```

**Bash (Linux/macOS):**
```bash
rm -rf tests/__pycache__ pages/__pycache__

```

## Инспектирование исчезающего элемента
```JS
setTimeout(function() { debugger; }, 5000);
```
# Настройка Firefox для Linux

При запуске тестов на Linux необходимо явно указать путь к Firefox:

1. Откройте `conftest.py`
2. Раскомментируйте строку:
```bash
options.binary_location = "/usr/bin/firefox"  # Обязательно для Linux
```

# Запуск тестов с генерацией отчетов
```bash
pytest tests/ --alluredir=./allure_results ; allure serve ./allure_results
```
# запуск одного теста
```bash
pytest tests/form_test.py --alluredir=./allure_results ; allure serve ./allure_results
```
