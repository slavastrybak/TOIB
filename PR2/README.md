1. Создать виртуальную машину на базе ОС Debian 12 
2. Создать пользователя super-{ФИО}, наделить его привилегиями суперпользователя
   ![image](https://github.com/slavastrybak/TOIB/assets/70744558/d0fcb759-6f78-4713-9ffe-fe4a367aae80)
   ![image](https://github.com/slavastrybak/TOIB/assets/70744558/018e51a1-a8a2-4571-8b1b-fbeeb5f69ee7)
4. Зайти под созданным пользователем и создать группу group-{группа}
   ![image](https://github.com/slavastrybak/TOIB/assets/70744558/1a58ddc1-c1bf-4305-a5aa-32287ac2e43b)
6. Добавить пользователя super-{ФИО} в группу group-{группа}
   ![image](https://github.com/slavastrybak/TOIB/assets/70744558/c2579477-70a2-40d1-9dcd-f90e3054c587)
8. Продемонстрировать наличие пользователя в группе
   ![image](https://github.com/slavastrybak/TOIB/assets/70744558/d9517295-f263-4bdf-98c2-b802f55e5f12)
10. Создать пользователя user-{ФИО}, добавить его в группу group-{группа}
    ![image](https://github.com/slavastrybak/TOIB/assets/70744558/d3cd83f9-caf2-46fc-8b25-927967090261)
12. Наделить полномочиями (с использованием механизмов дискреционного управления
доступом chmod) пользователя user-{ФИО} по созданию и удалению файлов в домашнем
каталоге пользователя super-{ФИО}
![image](https://github.com/slavastrybak/TOIB/assets/70744558/6989e2cc-ba41-472c-a7e7-922417915cda)
14. Продемонстрировать работу механизмов разграничения доступа.
    ![image](https://github.com/slavastrybak/TOIB/assets/70744558/fb2f0356-77cf-4c7c-85f1-f7c814ce0c41)
