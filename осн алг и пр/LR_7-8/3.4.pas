//Замените в строке все вхождения 'word' на 'letter'
var
  s, s_old, s_new:string;
  i,l_s_old: integer;
begin
  readln(s);
  s_old := 'word';
  s_new := 'letter';
  l_s_old := length(s_old);
  i := 1;
  while i <> 0 do 
    begin
    i := pos(s_old, s);
        if i <> 0 then 
        begin
            delete(s, i, l_s_old);
            insert(s_new, s, i);
        end;
    end;
  writeln(s);
end.