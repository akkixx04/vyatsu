function f(x:real):real;
begin
f:=x/sqr(sin(3*x));
end;
var 
  a, b, h, s:real;
  n, i:integer;
begin
a := 0.2;
b := 1;
write('Введите число разбиений n=');
readln(n);
h := (b - a) / n;
s:=(f(a) + f(b)) / 2;
for i := 1 to n - 1 do
s :=s + f(a+i*h);
s := s * h;
write('S = ',s:0:5);
end.