// сортировка данных с помощью алгоритма подсчетом 
type
    TComparator = function(a, b: integer): boolean;

// Компаратор для сортировки по возрастанию
function Top(a, b: Integer): boolean;
begin
    Top := a < b;
end;

// Компаратор для сортировки по убыванию
function Down(a, b: Integer): boolean;
begin
    Down := a > b;
end;
    
procedure CountingSort(var arr: array of integer; comparator: TComparator);
var
    max_n, m, i, a: integer;
    count: array of integer;
begin
    // Находим максимальное значение в массиве
    max_n := arr[0];
    for i := 1 to length(arr) - 1 do
        if arr[i] > max_n then
            max_n := arr[i];

    m := max_n + 1;  // Задаем размер массива count на единицу больше максимального значения

    // Инициализируем массив count с нулями, размером m
    setlength(count, m);
    for i := 0 to m - 1 do
        count[i] := 0;

    // Подсчитываем количество каждого элемента в исходном массиве
    for a := 0 to length(arr) - 1 do
        count[arr[a]] := count[arr[a]] + 1;  // Увеличиваем счетчик для значения arr[a]

    // Переписываем исходный массив с учетом количества каждого элемента
    i := 0;

    // Заполняем массив, применяя компаратор
    for a := 0 to m - 1 do  // Проходим по значениям от 0 до max_val
    begin
        while (count[a] > 0) and (i < length(arr)) do
        begin
            arr[i] := a;
            i += 1;  // Переходим к следующей позиции в исходном массиве
            count[a] := count[a] - 1; // Уменьшаем счетчик
        end;
    end;

    // Дополнительный шаг для изменения порядка в зависимости от компаратора
        for i := 0 to length(arr) - 1 do
            for a := i + 1 to length(arr) - 1 do
                if comparator(arr[a], arr[i]) then
                begin
                    // Меняем местами элементы
                    arr[i] := arr[i] + arr[a];
                    arr[a] := arr[i] - arr[a];
                    arr[i] := arr[i] - arr[a];
                end;
end;

// Процедура для чтения чисел из файла
function ReadFile(filename: string): array of integer;
var
    f: text;
    number: integer;
    numbers: array of integer;
begin
    assign(f, filename);
    reset(f);
    setlength(numbers, 0);
    while not eof(f) do
    begin
        readln(f, number);
        setlength(numbers, length(numbers) + 1);
        numbers[High(numbers)] := number;
    end;
    close(f);
    ReadFile := numbers;
end;

// Процедура для записи чисел в файл
procedure WriteFile(filename: string; arr: array of Integer);
var
    f: text;
    i: integer;
begin
    assign(f, filename);
    rewrite(f);
    for i := 0 to length(arr) - 1 do
    begin
        writeln(f, arr[i]);
    end;
    close(f);
end;

var
    numbers: array of integer;
    i: integer;
begin
    // Читаем числа из файла
    numbers := ReadFile('C:\2курс\осн алг и пр\дкр5\input1.txt');

    // Сортируем массив по возрастанию
    CountingSort(numbers, Top);

    // Выводим отсортированный массив
    for i := 0 to length(numbers) - 1 do
        write(numbers[i], ' ');
    
    // Записываем отсортированный массив в файл
    WriteFile('C:\2курс\осн алг и пр\дкр5\output1.txt', numbers);
end.

