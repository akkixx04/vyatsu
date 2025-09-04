var n_m: integer;
begin
    write ('Введите номер месяца: ');
    readln (n_m);
    case n_m of
        1,3,5,7,8,10,12: writeln ('31');
        2: writeln ('28 or 29');
        4,6,9,11: writeln ('30');
        else writeln ('Такого месяца не существует')
    end;

end.