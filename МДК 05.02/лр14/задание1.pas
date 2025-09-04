//Распечатать последовательность, используя рекурсию: 25,23,21,19,17… 0
procedure seq_uence(n:integer);//Параметризация
begin
     if n >= 0 then begin // База рекурсии n < 0
        write (n, ' ');
        seq_uence(n - 2) // Декомпозиция
     end;
end;
begin
    seq_uence(25);
end.