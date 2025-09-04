var
  N, P, a : integer;
begin 
  readln(N);
  P := 1;
  a := 1;
  while N <> 0 do
  begin
    a := N mod 10;
    P *= a;
    N := N div 10;
  end;
  begin
    writeln(P)
  end;
end.