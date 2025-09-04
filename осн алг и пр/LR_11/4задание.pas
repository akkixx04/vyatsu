uses GraphABC;
var
  r: integer;
begin
  setwindowsize(500,500);
  r := 200;
  repeat
    setpencolor(rgb(random(256), random(256), random(256)));
    circle(250,250,r);
    r -= 10
  until r = 0;
 
end.