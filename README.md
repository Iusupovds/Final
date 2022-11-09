# Final
Для выполнения тестирования применялись методы:
- Тестирование требований
- Ручное тестирование
- Автотестирование с помощью Python, Devtools, Selenium
- Позитивное/негативное/деструктивное тестирование
- Функциональное тестирование (Регистрация, Авторизация)
- Нефункциональное тестирование (Тестирование пользовательского интерфейса)
- Кроссбраузерное тестирование
- Тестирование на мобильных устройствах
Комманда для запуска тестов python '-m pytest -v --driver Chrome --driver-path C:\chromedriver.exe' при условии нахождения chromedriver в указаной директории.
Честно говоря мог бы сделать лучше, но в связи с ограниченным временем от многого пришлось отказаться.
По возможности стоит добавить нагрузочное тестирование, при одновременном использовании большого количества пользователей. 
Если присутствует API документация можно так же добавить REST API тестирование.
Можно добавить проверку сайта с помощью SEO Tools, проверить на коды ошибок в DevTools 
Знаю про assert проверки в тестах, но честно не успеваю.
Что не получилось:
- поймать всплывающее окно при вызове телефона
- удалить зарегистрированного пользователя
- найти стабильную ссылку для отдельного открытия страницы регистрации, поэтому reg_page получился таким убогим, да и тесты пополнились поиском локаторов
- проверить полный функционал сайта(из-за времени)
