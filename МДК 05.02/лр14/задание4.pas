// Необходимо сымитировать работу цикла for. Выводить каждый раз слово «привет» и значение счетчика.
procedure LoopFor(i, n: integer); //Параметризация
begin
  if n <= 0 then // База рекурсии
    exit;
  writeln('привет ', i);
  LoopFor(i + 1, n - 1) // Декомпозиция
end;
begin
  LoopFor(2,3);
end.
