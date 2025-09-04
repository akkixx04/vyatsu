var
  N, x, s : integer;
begin 
  readln(N);
  x := 1;
  s := 0;
  while x < N do
  begin
    if N mod x = 0 then
    begin
    s += x;
    x += 1;
    end
    else 
      begin
      x += 1;
      end;
  end;
  if s = N then
  begin
    writeln('ДА')
  end
  else
  begin
    writeln('НЕТ')
  end;
end.