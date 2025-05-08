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

<details> <summary><strong>Почему это нужно?</strong> (нажмите для раскрытия)</summary>
Firefox, установленный через snap, несовместим с Selenium

Путь /usr/bin/firefox гарантирует использование системной версии (.deb/apt)

Snap-пакеты работают в изолированной среде и блокируют доступ к профилям

Убедитесь, что Firefox установлен через apt:

bash
sudo apt install firefox
Дополнительная диагностика
Если возникает ошибка No such file or directory:

bash
sudo snap remove firefox  # Удалить snap-версию
which firefox            # Проверить путь (должен быть /usr/bin/firefox)
</details>
