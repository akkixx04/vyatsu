unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls;

type

  { TCalculator }

  TCalculator = class(TForm)
    DelOne: TButton;
    Four: TButton;
    Five: TButton;
    Six: TButton;
    Multiplication: TButton;
    DivOne: TButton;
    One: TButton;
    Two: TButton;
    Three: TButton;
    Minus: TButton;
    Zero: TButton;
    CE: TButton;
    Point: TButton;
    Plus: TButton;
    Equal: TButton;
    COut: TButton;
    SqrtBT: TButton;
    Seven: TButton;
    Eight: TButton;
    Nine: TButton;
    DivNumber: TButton;
    SqrBT: TButton;
    OutNum: TEdit;
    procedure ClickZpt(Sender: TObject);
    procedure ClickOneDel(Sender: TObject);
    procedure ClickNumber(Sender: TObject);
    procedure DeleteOne(Sender: TObject);
    procedure ClickOperand(Sender: TObject);
    procedure ClickCe(Sender: TObject);
    procedure ClickC(Sender: TObject);
    procedure ClickSqrt(Sender: TObject);
    procedure ClickSqr(Sender: TObject);
    procedure ClickZnak(Sender: TObject);
  private

  public

  end;

var
  Calculator: TCalculator;
  a, b, c: Real;
  znak: string;
implementation

{$R *.lfm}

{ TCalculator }

procedure TCalculator.ClickZnak(Sender: TObject);
begin
  if (OutNum.Text = 'Невозможно') or
     (OutNum.Text = 'Некорректное число') or
     (OutNum.Text = 'Введите число') then
  begin
    OutNum.Clear;
  end;
   try
    if Trim(OutNum.Text) = '' then
      raise Exception.Create('Введите число');

    a := StrToFloat(OutNum.Text);
    OutNum.Clear;
    znak := (Sender as TButton).Caption;
  except
    on E: EConvertError do
      OutNum.Text := 'Некорректное число';
    on E: Exception do
      OutNum.Text := E.Message;
  end;
end;

procedure TCalculator.ClickNumber(Sender: TObject);
begin
  if (OutNum.Text = 'Невозможно') or
     (OutNum.Text = 'Некорректное число') or
     (OutNum.Text = 'Введите число') then
  begin
    OutNum.Clear;
  end;
  if (OutNum.Text = '') or (OutNum.Text = '0') then
    OutNum.Text := (Sender as TButton).Caption
  else
    OutNum.Text := OutNum.Text + (Sender as TButton).Caption;
end;

procedure TCalculator.ClickOneDel(Sender: TObject);
begin
  if (OutNum.Text = 'Невозможно') or
     (OutNum.Text = 'Некорректное число') or
     (OutNum.Text = 'Введите число') then
  begin
    OutNum.Clear;
  end;
  if Trim(OutNum.Text) = '' then
  begin
    OutNum.Text := 'Введите число';
    Exit;
  end;
  try
    a := StrToFloat(OutNum.Text);
    if a = 0 then
      raise Exception.Create('Невозможно')
    else
    a := 1 / a;
    OutNum.Text := FloatToStr(a);
    a := 0;
  except
    on E: Exception do
    begin
      OutNum.Text := 'Введите число';
    end;
  end;
end;

procedure TCalculator.ClickZpt(Sender: TObject);
begin
  if (OutNum.Text = 'Невозможно') or
     (OutNum.Text = 'Введите число') or
     (OutNum.Text = 'Некорректное число') then
  begin
    Exit;
  end;
   if Trim(OutNum.Text) = '' then
  begin
    OutNum.Text := 'Введите число';
    Exit;
  end;
  if Pos(',', OutNum.Text) = 0 then
  begin
    if OutNum.Text = '' then
      OutNum.Text := ','
    else
      OutNum.Text := OutNum.Text + ',';
  end;
end;

procedure TCalculator.DeleteOne(Sender: TObject);
var str: string;
begin
  if (OutNum.Text = 'Невозможно') or
     (OutNum.Text = 'Введите число') or
     (OutNum.Text = 'Некорректное число') then
  begin
    Exit;
  end;
   if Trim(OutNum.Text) = '' then
  begin
    OutNum.Text := 'Введите число';
    Exit;
  end;
  try
  str:= OutNum.Text;
  if str <> '' then
  Delete(str, length(str),1);
  OutNum.Text:= str;
  except
    on E: EConvertError do
    begin
      OutNum.Text := 'Невозможно';
      Exit;
    end;
  end;
end;

procedure TCalculator.ClickOperand(Sender: TObject);
begin
  if (OutNum.Text = 'Невозможно') or
     (OutNum.Text = 'Введите число') or
     (OutNum.Text = 'Некорректное число') then
  begin
    Exit;
  end;
   if Trim(OutNum.Text) = '' then
  begin
    OutNum.Text := 'Введите число';
    Exit;
  end;
   try
    b := StrToFloat(OutNum.Text);
  except
    on E: EConvertError do
    begin
      OutNum.Text := 'Некорректное число';
      Exit;
    end;
  end;

  OutNum.Clear;

  case znak of
    '+': c := a + b;
    '-': c := a - b;
    '*': c := a * b;
    '/': begin
           if b = 0 then
           begin
             OutNum.Text := 'Невозможно';
             Exit;
           end
           else
             c := a / b;
         end;
  end;
  a:=c;
  OutNum.Text := FloatToStr(c);
end;

procedure TCalculator.ClickCe(Sender: TObject);
begin
  OutNum.Clear;
end;

procedure TCalculator.ClickC(Sender: TObject);
begin
  OutNum.Clear;
  a:=0;
  b:=0;
  c:=0;
end;

procedure TCalculator.ClickSqrt(Sender: TObject);
begin
  if (OutNum.Text = 'Невозможно') or
     (OutNum.Text = 'Введите число') or
     (OutNum.Text = 'Некорректное число') then
  begin
    Exit;
  end;
  if Trim(OutNum.Text) = '' then
  begin
    OutNum.Text := 'Введите число';
    Exit;
  end;
  if a < 0 then
  begin
    OutNum.Text := 'Некорректное число';
    Exit;
  end
  else
  a:=strtofloat(OutNum.Text);
  a:=sqrt(a);
  OutNum.Text:=floattostr(a);
  a:=0;
end;

procedure TCalculator.ClickSqr(Sender: TObject);
begin
  if (OutNum.Text = 'Невозможно') or
     (OutNum.Text = 'Введите число') or
     (OutNum.Text = 'Некорректное число') then
  begin
    Exit;
  end;
  if Trim(OutNum.Text) = '' then
  begin
    OutNum.Text := 'Введите число';
    Exit;
  end;
  a:=strtofloat(OutNum.Text);
  a:=sqr(a);
  OutNum.Text:=floattostr(a);
  a:=0;
end;

end.

