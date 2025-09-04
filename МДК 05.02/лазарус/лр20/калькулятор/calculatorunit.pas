unit calculatorUnit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls;

type

  { TcalculatorForm }

  TcalculatorForm = class(TForm)
    backspace: TButton;
    btn4: TButton;
    btn5: TButton;
    Background: TImage;
    btn6: TButton;
    btnMultiplication: TButton;
    btnDivOne: TButton;
    btn1: TButton;
    btn2: TButton;
    btn3: TButton;
    btnMinus: TButton;
    btn0: TButton;
    btnCE: TButton;
    btnPoint: TButton;
    btnPlus: TButton;
    btnEqual: TButton;
    btnC: TButton;
    SqrtBT: TButton;
    btn7: TButton;
    btn8: TButton;
    btn9: TButton;
    btnDiv: TButton;
    btnSqr: TButton;
    display: TEdit;
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
  calculatorForm: TcalculatorForm;
  num1, num2, res: Real;
  znak: string;
implementation

{$R *.lfm}

{ TcalculatorForm }

procedure TcalculatorForm.ClickZnak(Sender: TObject);
begin
  if (display.Text = 'невозможно') or
     (display.Text = 'некорректное число') or
     (display.Text = 'введите число') then
  begin
    display.Clear;
  end;
   try
    if Trim(display.Text) = '' then
      raise Exception.Create('введите число');
    if Trim(display.Text) = '-' then
      raise Exception.Create('введите число');

    num1 := StrToFloat(display.Text);
    display.Clear;
    znak := (Sender as TButton).Caption;
  except
    on E: EConvertError do
      display.Text := 'некорректное число';
    on E: Exception do
      display.Text := E.Message;
  end;
end;

procedure TcalculatorForm.ClickNumber(Sender: TObject);
begin
  if (display.Text = 'невозможно') or
     (display.Text = 'некорректное число') or
     (display.Text = 'введите число') then
  begin
    display.Clear;
  end;
  if (display.Text = '') or (display.Text = '0') then
    display.Text := (Sender as TButton).Caption
  else
    display.Text := display.Text + (Sender as TButton).Caption;
end;

procedure TcalculatorForm.ClickOneDel(Sender: TObject);
begin
  if (display.Text = 'невозможно') or
     (display.Text = 'некорректное число') or
     (display.Text = 'введите число') then
  begin
    display.Clear;
  end;
  if Trim(display.Text) = '' then
  begin
    display.Text := 'введите число';
    Exit;
  end;
  try
    num1 := StrToFloat(display.Text);
    if num1 = 0 then
      raise Exception.Create('невозможно')
    else
    num1 := 1 / num1;
    display.Text := FloatToStr(num1);
    num1 := 0;
  except
    on E: Exception do
    begin
      display.Text := 'невозможно';
    end;
  end;
end;

procedure TcalculatorForm.ClickZpt(Sender: TObject);
begin
  if (display.Text = 'невозможно') or
     (display.Text = 'некорректное число') or
     (display.Text = 'введите число') then
  begin
    Exit;
  end;
   if Trim(display.Text) = '' then
  begin
    display.Text := 'введите число';
    Exit;
    end;
   if Trim(display.Text) = '-' then
   begin
      display.Text := 'введите число';
      Exit;
  end;
  if Pos(',', display.Text) = 0 then
  begin
    if display.Text = '' then
      display.Text := ','
    else
      display.Text := display.Text + ',';
  end;
end;

procedure TcalculatorForm.DeleteOne(Sender: TObject);
var str: string;
begin
  if (display.Text = 'невозможно') or
     (display.Text = 'некорректное число') or
     (display.Text = 'введите число') then
  begin
    Exit;
  end;
   if Trim(display.Text) = '' then
  begin
    display.Text := 'введите число';
    Exit;
  end;
  try
  str:= display.Text;
  if str <> '' then
  Delete(str, length(str),1);
  display.Text:= str;
  except
    on E: EConvertError do
    begin
      display.Text := 'невозможно';
      Exit;
    end;
  end;
end;

procedure TcalculatorForm.ClickOperand(Sender: TObject);
begin
  if (display.Text = 'невозможно') or
     (display.Text = 'некорректное число') or
     (display.Text = 'введите число') then
  begin
    Exit;
  end;
   if Trim(display.Text) = '' then
  begin
    display.Text := 'введите число';
    Exit;
  end;
   if Trim(display.Text) = '-' then
  begin
    display.Text := 'введите число';
    Exit;
  end;
   try
    num2 := StrToFloat(display.Text);
  except
    on E: EConvertError do
    begin
      display.Text := 'некорректное число';
      Exit;
    end;
  end;

  display.Clear;

  case znak of
    '+': res := num1 + num2;
    '-': res := num1 - num2;
    '*': res := num1 * num2;
    '/': begin
           if num2 = 0 then
           begin
             display.Text := 'невозможно';
             Exit;
           end
           else
             res := num1 / num2;
         end;
  end;
  num1:=res;
  display.Text := FloatToStr(res);
end;

procedure TcalculatorForm.ClickCe(Sender: TObject);
begin
  display.Clear;
end;

procedure TcalculatorForm.ClickC(Sender: TObject);
begin
  display.Clear;
  num1:=0;
  num2:=0;
  res:=0;
end;

procedure TcalculatorForm.ClickSqrt(Sender: TObject);
begin
  if (display.Text = 'невозможно') or
     (display.Text = 'некорректное число') or
     (display.Text = 'введите число') then
  begin
    Exit;
  end;
  if Trim(display.Text) = '' then
  begin
    display.Text := 'введите число';
    Exit;
  end;
  if Trim(display.Text) = '-' then
  begin
    display.Text := 'введите число';
    Exit;
  end;
  if num1 < 0 then
  begin
    display.Text := 'некорректное число';
    Exit;
  end
  else
  num1:=strtofloat(display.Text);
  num1:=sqrt(num1);
  display.Text:=floattostr(num1);
  num1:=0;
end;

procedure TcalculatorForm.ClickSqr(Sender: TObject);
begin
  if (display.Text = 'невозможно') or
     (display.Text = 'некорректное число') or
     (display.Text = 'введите число') then
  begin
    Exit;
  end;
  if Trim(display.Text) = '' then
  begin
    display.Text := 'введите число';
    Exit;
  end;
  if Trim(display.Text) = '-' then
  begin
    display.Text := 'введите число';
    Exit;
  end;
  num1:=strtofloat(display.Text);
  num1:=sqr(num1);
  display.Text:=floattostr(num1);
  num1:=0;
end;

end.

