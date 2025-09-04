var
  y, x, a, b, h: integer;

begin
  a := 0;
  b := 7;
  h := 1;
  if (a < b) and (h > 0) then
  begin
    x := a;
    while x <= b do
    begin
      y := 2 * x + 1;
      writeln(y);
      x += h;
    end;
  end
end.