var
  a, b, h, x, y: real;

begin
  readln(x);
  
  a := -10;
  b := 8;
  h := 0.1;
  
  begin
    
    while a <= b do
      if x < -8 then
      begin
        y := sin(a);
        writeln(y);
        a += h;
      end
      
      else if x < 1 then
      begin
        y := tan(a) / power(a, 0.1 * a);
        writeln(y);
        a += h;
      end
      
      else if x < 6 then
      begin
        y := (power(a, 3) * log10(a) + log10(a)) / power(a, 2);
        writeln(y);
        a += h;
      end
      
      else
      begin
        y := (85 * 64 + power(a, 3)) / cos(2 * a);
        writeln(y);
        a += h;
      end
      
  end
end.