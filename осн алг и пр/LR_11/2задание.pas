uses GraphABC;
begin
  setwindowsize(1000,500);
  
  line(300,400,600,400);
  
//  setbrushcolor(clRed);
  
  line(375,400,450,150);
  line(450,150,525,400);
  floodfill(450,197,clred);
 
  circle(450,150,30);
  floodfill(450,150,clred);
  
//  setbrushcolor(clblue);
  
  line(392,342,250,200);
  line(250,200,300,400);
  floodfill(333,333,clblue);
  
  circle(250,200,30);
  floodfill(250,200,clblue);
  
//  setbrushcolor(cllime);
  
  line(510,350,650,200);
  line(650,200,600,400);
  floodfill(567,333,clLime);
  
  circle(650,200,30);
  floodfill(650,200,cllime);
  
  setbrushcolor(clRed);
  
//  line(375,400,450,150);
//  line(450,150,525,400);
//  floodfill(450,197,clred);
//  
//  circle(450,150,30);
//  floodfill(450,150,clred);
end.