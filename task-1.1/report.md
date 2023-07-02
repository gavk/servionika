# Отчёт о выполнении задания 1.1

## Работа скрипта
Исходный файл storage.data:
```
$ cat storage.data 
{
    "1": [
        "4",
        "3"
    ],
    "key": [
        "value"
    ]
}
```
Добавляем значение к существующему ключу:
```
$ ./storage.py --key key --val 6
```
Содержимое файла storage.data:
```
$ cat storage.data 
{
    "1": [
        "4",
        "3"
    ],
    "key": [
        "value",
        "6"
    ]
}
```
Добавляем значение с несуществующим ключом:
```
$ ./storage.py --key second_key --val 12
```
Содержимое файла storage.data:
```
$ cat storage.data 
{
    "1": [
        "4",
        "3"
    ],
    "key": [
        "value",
        "6"
    ],
    "second_key": [
        "12"
    ]
}
```
Получение данных по ключу, содержащему одно значение, не одно значение и несуществующему ключу:
```
$ ./storage.py --key second_key
12
$ ./storage.py --key key
value,6
$ ./storage.py --key other_key
None
```
