var
  n_kv, n_pod, n_floor: integer;

begin
  writeln('Введите номер квартиры: ');
  readln(n_kv);

  n_pod := (n_kv - 1) div 36 + 1;
  n_floor := (n_kv - 1) mod 36 div 4 + 1;

  writeln('Номер подъезда: ', n_pod);
  writeln('Этаж: ', n_floor);
end.
