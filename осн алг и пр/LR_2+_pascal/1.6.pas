var
  a, b, c: integer;
  
begin
  a := 10;
  b := 10;
  c := 50;
  if (a * b) mod c = 0 then
    writeln('True')
  else
    writeln('False');
end.