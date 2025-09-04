//Дана строка. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'
var
  s,s1:string;
  l:integer;
begin
  readln(s);
  s1 := s[1]+s[2]+s[3];
  l := length(s);
  if s1 = 'abc' then
    begin
    s[1] := 'w';
    s[2] := 'w';
    s[3] := 'w';
    end
  else
    begin
    insert('zzz',s,l+1);
    end;
  writeln(s)
end.