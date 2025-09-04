// Требуется написать программу, которая в зависимости от числа добавляет правильное окончание.
var
  number: integer;
  years_w: string;
  a: set of byte;

begin
  writeln('Введите количество лет:');
  readln(number);
  
  a := [11, 12, 13, 14];
  
  if (number mod 100 in a) then
    years_w := 'лет'
  else
    case number mod 10 of
      1: years_w := 'год';
      2, 3, 4: years_w := 'года';
    else years_w := 'лет';
    end;
  
  writeln(number, ' ', years_w);
end.
