var
  x, y: real;

begin
  readln(x);
  
  if x < -8 then
  begin
    y := sin(x);
    writeln(y);
  end
  
  else if x < 1 then
  begin
    y := tan(x) / power(x, 0.1 * x);
    writeln(y)
  end
  
  else if x < 6 then
  begin
    y := (power(x, 3) * log10(x) + log10(x)) / power(x, 2);
    writeln(y)
  end
  
  else
  begin
    y := (85 * 64 + power(x, 3)) / cos(2 * x);
    writeln(y)
  end
  
end.