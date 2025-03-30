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