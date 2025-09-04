// Написать рекурсивную функцию  sumTo(n), которая для данного n вычисляет сумму чисел от 1 до n.
var x: integer;
   function sumTo (a: integer): integer; //Параметризация
   begin
        if (a<=1) then // База рекурсии
          a:=1
        else
          a:=a + (sumTo(a-1));  // Декомпозиция
   sumTo:=a;
end;
begin
writeln('Введите число: ');
readln(x);
writeln(sumTo(x));
end.