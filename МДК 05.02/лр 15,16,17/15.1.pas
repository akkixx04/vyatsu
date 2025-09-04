//  Создать анкетные данные о студенте(type anketa)
type anketa = record
    fio: string;
    birth: string;
    kurs: 1..5
end;
var student:  anketa;
begin
  student.fio:= 'Широнина Анна Андреевна';
  student.birth := '24.07.2007';
  readln(student.kurs);
  writeln('ФИО: ', student.fio);
  writeln('Дата рождения: ',student.birth);
  writeln('Курс: ',student.kurs);
end.