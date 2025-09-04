uses GraphABC;
var
  x: integer;
begin
  setwindowsize(350,200);
  x := 50;
  repeat 
    setpencolor(rgb(random(256), random(256), random(256)));
    circle(x,100,10);
    x += 30;
  until x=350;
end.