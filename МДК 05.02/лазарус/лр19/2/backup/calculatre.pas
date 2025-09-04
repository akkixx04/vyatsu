unit calculatre;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Math;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Edit1: TEdit;
    Edit4: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Label1: TLabel;
    Label5: TLabel;
    Label2: TLabel;
    Label4: TLabel;
    Label3: TLabel;
    Label6: TLabel;
    Label7: TLabel;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Label2Click(Sender: TObject);
    procedure Label3Click(Sender: TObject);
    procedure Label6Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Label2Click(Sender: TObject);
begin

end;

procedure TForm1.Button1Click(Sender: TObject);
  var S:integer;
    a,d,S1:real;
  begin
      S:=strtoint(edit1.text);
      a:=sqrt(S);
      edit2.Text := floattostr(a);
      d := a*sqrt(2);
      edit3.Text := floattostr(d);


  end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  edit1.clear;
  Edit2.clear;
  edit3.clear;
  Edit4.clear;
  edit1.setfocus;
end;

procedure TForm1.Label3Click(Sender: TObject);
begin

end;

procedure TForm1.Label6Click(Sender: TObject);
begin

end;

end.

