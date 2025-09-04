var
  a, b, T: boolean;

begin
  a := True;
  b := False;
  if (a = True) and (b = False) or (a = False) and (b = True) then
    T := True
  else
    T := False;
  writeln(T);
end.
