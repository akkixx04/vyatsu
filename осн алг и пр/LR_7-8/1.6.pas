//Дана строка. Показать третий, шестой, девятый и так далее символы
var
  s: string;
  i, l: integer;

begin
  readln(s);
  l := length(s);
  for i := 3 to l do
  begin
    if (i mod 3 = 0) then
      write(s[i],' ');
  end;
end.