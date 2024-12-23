FAT (таблица размещения файлов), FAT16, FAT32
========================

FAT — одна из старейших и простейших файловых систем. Первоначально она была разработана для MS-DOS и до сих пор используется во многих съемных устройствах хранения. Две основные версии этой системы — FAT16 и FAT32. FAT использует таблицу размещения файлов для отслеживания расположения файлов на диске. Однако в ней отсутствуют некоторые дополнительные функции, такие как права доступа к файлам и ведение журнала. В результате она менее подходит для современных операционных систем. FAT 16 была представлена в 1987 году вместе с DOS 3.31, а FAT32 внедрена в Windows 95 OSR2 (MS-DOS 7.1) в 1996 году.

## Преимущества
- Простота. Простота упрощает реализацию и использование, благодаря чему эта файловая система подходит для устройств с ограниченными ресурсами или требованиями к совместимости.
- Восстановление данных. Благодаря простой структуре файловые системы FAT относительно легко восстанавливаются в случае повреждения или случайного удаления данных.
- Совместимость: Изначально обеспечивает запись и чтение файлов в операционных системах Windows, MacOS и Linux без необходимости использования стороннего программного обеспечения.

## Недостатки
- Фрагментация. Фрагментация происходит, когда данные в файле разбросаны по разным частям диска, что приводит к снижению производительности. Для оптимизации производительности диска требуется регулярная дефрагментация.
- Отсутствие расширенных функций. В самой новой версии FAT32 отсутствуют некоторые расширенные функции, имеющиеся в других файловых системах. Она не поддерживает разрешения безопасности на уровне файлов, ведение журнала, шифрование или сжатие.
- Ограничения на имена томов. Имена томов для FAT16 и FAT32 не могут содержать больше 11 символов и не могут включать в себя большинство специальных символов.
- Ограничения на имена файлов. Имена файлов в файловой системе FAT16 не могут превышать 8.3 символов. Это означает 8 символов плюс 3 символа расширения файла.