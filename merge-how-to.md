# Полное руководство по работе с ветками в Git

## Введение

Работа с ветками - одна из ключевых возможностей Git, позволяющая вести параллельную разработку разных функциональностей. Это руководство подробно объясняет все аспекты работы с ветками: от базовых операций до продвинутых техник.

## 1. Основные концепции

### 1.1 Что такое ветка?

Ветка в Git - это подвижный указатель на один из коммитов. Когда вы создаете коммит, указатель ветки автоматически перемещается вперед, указывая на новый коммит.

**Ключевые особенности:**
- Легковесные (только указатели)
- Быстрое создание и переключение
- Позволяют изолировать изменения

### 1.2 Основные ветки в проекте

Типичная структура веток:
main (или master) - стабильная версия проекта
develop - основная ветка разработки
feature/* - ветки для новых функций
release/* - ветки подготовки релиза
hotfix/* - срочные исправления

Copy

## 2. Работа с локальными ветками

### 2.1 Создание веток

**Создание новой ветки:**
```bash
git branch new-feature
Создание и переключение:

bash
Copy
git checkout -b new-feature
# Или в новых версиях Git:
git switch -c new-feature
2.2 Переключение между ветками
Базовое переключение:

bash
Copy
git checkout branch-name
# Или:
git switch branch-name
Важные нюансы:

Непереданные изменения будут перенесены в новую ветку

Для чистого переключения используйте git stash

3. Работа с удаленными ветками
3.1 Получение информации
Просмотр всех веток:

bash
Copy
git branch -a  # Локальные и удаленные
git branch -r  # Только удаленные
Просмотр связи веток:

bash
Copy
git branch -vv
3.2 Синхронизация с сервером
Получение изменений:

bash
Copy
git fetch origin
Создание локальной ветки на основе удаленной:

bash
Copy
git checkout --track origin/remote-branch
4. Слияние веток
4.1 Основные стратегии
1. Fast-forward merge (если возможно):

bash
Copy
git checkout main
git merge feature
2. Recursive merge (создает коммит слияния):

bash
Copy
git merge --no-ff feature
4.2 Ребазирование
Базовое ребазирование:

bash
Copy
git checkout feature
git rebase main
Интерактивное ребазирование:

bash
Copy
git rebase -i HEAD~3
5. Разрешение конфликтов
5.1 Типы конфликтов
Конфликты содержимого - разные изменения в одних строках

Конфликты переименования - файл переименован в обеих ветках

Конфликты удаления - файл удален в одной ветке и изменен в другой

5.2 Процесс разрешения
Найдите конфликтующие файлы (git status)

Откройте файлы и разрешите конфликты

Добавьте исправленные файлы (git add)

Завершите слияние (git commit)