// сортировка данных с помощью алгоритма слияния

// Тип TComparator: определен тип для компараторов функции, который принимает два целых числа и возвращает логическое значение.
type
    TComparator = function(a, b: integer): boolean;
    
// Процедура Merge: обработает слияние двух половин с использованием компаратора, переданного как параметр.
procedure Merge(arr: array of Integer; left, mid, right: integer; comparator: TComparator);
var
    i, j, k: integer;
    left_half, right_half: array of integer;
begin
    // Создаем левые и правые массивы
    setlength(left_half, mid - left + 1);
    setlength(right_half, right - mid);

    // Копируем данные в левые и правые массивы
    for i := 0 to length(left_half) - 1 do
        left_half[i] := arr[left + i];

    for j := 0 to length(right_half) - 1 do
        right_half[j] := arr[mid + 1 + j];

    // Слияние отсортированных половин обратно в основной массив
    i := 0; // Индекс для левой половины
    j := 0; // Индекс для правой половины
    k := left; // Индекс для основного массива

    while (i < length(left_half)) and (j < length(right_half)) do
    begin
        if comparator(left_half[i], right_half[j]) then
        begin
            arr[k] := left_half[i];
            i := i + 1;
        end
        else
        begin
            arr[k] := right_half[j];
            j := j + 1;
        end;
        k := k + 1;
    end;

    // Добавляем оставшиеся элементы из левой половины, если такие остались
    while i < length(left_half) do
    begin
        arr[k] := left_half[i];
        i := i + 1;
        k := k + 1;
    end;

    // Добавляем оставшиеся элементы из правой половины, если такие остались
    while j < length(right_half) do
    begin
        arr[k] := right_half[j];
        j := j + 1;
        k := k + 1;
    end;
end;

 // Процедура MergeSort: прием компаратора и передача его в процедуру Merge
procedure MergeSort(var arr: array of integer; left, right: integer; comparator: TComparator);
var
    mid: integer;
begin
    // Если массив содержит более одного элемента, продолжаем деление
    if left < right then
    begin
        // Определяем середину массива
        mid := (left + right) div 2;

        // Рекурсивно вызываем MergeSort для каждой половины
        MergeSort(arr, left, mid, comparator);
        MergeSort(arr, mid + 1, right, comparator);

        // Сливаем отсортированные половины
        Merge(arr, left, mid, right, comparator);
    end;
end;

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
    numbers := ReadFile('C:\2курс\осн алг и пр\дкр5\input2.txt');

    // Сортируем массив по возрастанию
    MergeSort(numbers, 0, Length(numbers) - 1, Top);

    // Выводим отсортированный массив
    for i := 0 to length(numbers) - 1 do
        write(numbers[i], ' ');
    
    // Записываем отсортированный массив в файл
    WriteFile('C:\2курс\осн алг и пр\дкр5\output2.txt', numbers);
end.

