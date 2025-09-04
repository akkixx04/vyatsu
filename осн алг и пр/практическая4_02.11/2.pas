var
  N, x, k : integer;
begin 
  readln(N);
  x := 1;
  k := 0;
  while x <= N do
  begin
    if N mod x = 0 then
    begin
    k += 1;
    x += 1;
    end
    else 
      begin
      x += 1;
      end;
  end;
  begin
    writeln(k)
  end;
end.