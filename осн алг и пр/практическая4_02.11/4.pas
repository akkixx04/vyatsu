var
  N, i, k, c, x, y : integer;
begin 
  readln(N);
  i := 1;
  k := 0;
  while i <= N do
  begin
    x := 1;
    c := 0;
    readln(y);
    while x <= y do
      begin
      if y mod x = 0 then
      begin
        c += 1;
      end;
        x += 1;
      end;
    if c = 2 then
    begin
      k += 1;
    end;
      i += 1;
    end;
    writeln(k) 
end.