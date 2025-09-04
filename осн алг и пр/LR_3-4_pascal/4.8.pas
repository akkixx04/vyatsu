var

  service_time, min_time, num_min_buyer, num_buyer: integer;

begin
  min_time := maxint;
  num_buyer := 0;
  
  writeln('Введите время обслуживания каждого покупателя (0 - для окончания ввода):');
  
  repeat
    num_buyer += 1;
    readln(service_time);
    if (service_time > 0) and (service_time < min_time) then
    begin
      min_time := service_time;
      num_min_buyer := num_buyer;
    end;
  until service_time = 0;
  
  writeln('Покупателю с номером ', num_min_buyer, ' потребовалось самое малое время на обслуживание.');
  
end.