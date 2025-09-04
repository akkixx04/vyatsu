unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls, StdCtrls,
  Buttons, Math;

type

  { TForm1 }

  TForm1 = class(TForm)
    BitBtn1: TBitBtn;
    Button1: TButton;
    InterestType: TComboBox;
    Time: TComboBox;
    Label5: TLabel;
    Sum: TEdit;
    Percent: TEdit;
    Period: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Output: TMemo;
    procedure BitBtn1Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure InterestTypeChange(Sender: TObject);
    procedure Label2Click(Sender: TObject);
    procedure Label4Click(Sender: TObject);
    procedure SumChange(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.InterestTypeChange(Sender: TObject);
begin
end;

procedure TForm1.Button1Click(Sender: TObject);
var
  x, a, b, f: Float;
  i: set of char;
  j: Integer;
  k: Integer;
  Valid: Boolean;
begin
  i := ['0'..'9', ','];
  j := 1;
  if (Period.Text = '') or (InterestType.Text = '') or (Sum.Text = '') or (Percent.Text = '') then
  begin
    ShowMessage('Не все данные введены!');
    Exit;
  end;
  Valid := True;
  for k := 1 to Length(Period.Text) do
    if not (Period.Text[k] in i) then
      Valid := False;
  if Valid then
    for k := 1 to Length(Sum.Text) do
      if not (Sum.Text[k] in i) then
        Valid := False;
  if Valid then
    for k := 1 to Length(Percent.Text) do
      if not (Percent.Text[k] in i) then
        Valid := False;

  if not Valid then
  begin
    ShowMessage('Некорректно введены данные! Используйте только цифры и запятую.');
    Exit;
  end;

  if InterestType.Text = 'Простые проценты' then
  begin
    if Time.Text = 'Дни' then
    begin
      a := StrToFloat(Sum.Text);
      b := StrToFloat(Percent.Text) / 100;
      x := StrToFloat(Period.Text);

      f := a * b * (x/365);
      Output.Lines.Add('Будет начислено с суммы в ' + FloatToStr(a) + ' рублей с процентной ставкой в ' + FloatToStr(b) + ' начисляемых ежедневно: ' + FloatToStr(f)+ 'рублей');
    end;
    if Time.Text = 'Недели' then
    begin
      a := StrToFloat(Sum.Text);
      b := StrToFloat(Percent.Text) / 100;
      x := StrToFloat(Period.Text);

      f := a * b * (x/52);
      Output.Lines.Add('Будет начислено с суммы в ' + FloatToStr(a) + ' рублей с процентной ставкой в ' + FloatToStr(b) + ' начисляемых ежедневно: ' + FloatToStr(f)+ 'рублей');
    end;
     if Time.Text = 'Месяц' then
     begin
      a := StrToFloat(Sum.Text);
      b := StrToFloat(Percent.Text) / 100;
      x := StrToFloat(Period.Text);

      f := a * b * (x/12);
      Output.Lines.Add('Будет начислено с суммы в ' + FloatToStr(a) + ' рублей с процентной ставкой в ' + FloatToStr(b) + ' начисляемых ежедневно: ' + FloatToStr(f)+ 'рублей');
    end;
     if Time.Text = 'Квартал' then
      begin
      a := StrToFloat(Sum.Text);
      b := StrToFloat(Percent.Text) / 100;
      x := StrToFloat(Period.Text);

      f := a * b * (x/4);
      Output.Lines.Add('Будет начислено с суммы в ' + FloatToStr(a) + ' рублей с процентной ставкой в ' + FloatToStr(b) + ' начисляемых ежедневно: ' + FloatToStr(f)+ 'рублей');
    end;
    if Time.Text = 'Год' then
     begin
      a := StrToFloat(Sum.Text);
      b := StrToFloat(Percent.Text) / 100;
      x := StrToFloat(Period.Text);

      f := a * b * x;
      Output.Lines.Add('Будет начислено с суммы в ' + FloatToStr(a) + ' рублей с процентной ставкой в ' + FloatToStr(b) + ' начисляемых ежедневно: ' + FloatToStr(f)+ 'рублей');
    end;
  end;
  if InterestType.Text = 'Сложные проценты' then
  begin
    if Time.Text = 'Дни' then
    begin
      a := StrToFloat(Sum.Text);
      b := StrToFloat(Percent.Text) / 100;
      x := StrToFloat(Period.Text);

      f := a * b * (x/365);
      Output.Lines.Add('Будет начислено с суммы в ' + FloatToStr(a) + ' рублей с процентной ставкой в ' + FloatToStr(b) + ' начисляемых ежедневно: ' + FloatToStr(f)+ 'рублей');
    end;
    if Time.Text = 'Недели' then
    begin
      a := StrToFloat(Sum.Text);
      b := StrToFloat(Percent.Text) / 100;
      x := StrToFloat(Period.Text);

      f := a * b * (x/52);
      Output.Lines.Add('Будет начислено с суммы в ' + FloatToStr(a) + ' рублей с процентной ставкой в ' + FloatToStr(b) + ' начисляемых ежедневно: ' + FloatToStr(f)+ 'рублей');
    end;
     if Time.Text = 'Месяц' then
     begin
      a := StrToFloat(Sum.Text);
      b := StrToFloat(Percent.Text) / 100;
      x := StrToFloat(Period.Text);

      f := a * b * (x/12);
      Output.Lines.Add('Будет начислено с суммы в ' + FloatToStr(a) + ' рублей с процентной ставкой в ' + FloatToStr(b) + ' начисляемых ежедневно: ' + FloatToStr(f)+ 'рублей');
    end;
     if Time.Text = 'Квартал' then
      begin
      a := StrToFloat(Sum.Text);
      b := StrToFloat(Percent.Text) / 100;
      x := StrToFloat(Period.Text);

      f := a * b * (x/4);
      Output.Lines.Add('Будет начислено с суммы в ' + FloatToStr(a) + ' рублей с процентной ставкой в ' + FloatToStr(b) + ' начисляемых ежедневно: ' + FloatToStr(f)+ 'рублей');
    end;
    if Time.Text = 'Год' then
     begin
      a := StrToFloat(Sum.Text);
      b := StrToFloat(Percent.Text) / 100;
      x := StrToFloat(Period.Text);

      f := a * b * x;
      Output.Lines.Add('Будет начислено с суммы в ' + FloatToStr(a) + ' рублей с процентной ставкой в ' + FloatToStr(b) + ' начисляемых ежедневно: ' + FloatToStr(f)+ 'рублей');
    end;
  end;
  if InterestType.Text = 'Сложные проценты' then
begin
  a := StrToFloat(Sum.Text);
  b := StrToFloat(Percent.Text) / 100;
  x := StrToFloat(Period.Text);

  if Time.Text = 'Дни' then
  begin
    f := a * Power(1 + b/365, x);
    Output.Lines.Add('Итоговая сумма за ' + FloatToStr(x) + ' дней: ' + FloatToStrF(f, ffCurrency, 12, 2));
  end
  else if Time.Text = 'Недели' then
  begin
    f := a * Power(1 + b/52, x);
    Output.Lines.Add('Итоговая сумма за ' + FloatToStr(x) + ' недель: ' + FloatToStrF(f, ffCurrency, 12, 2));
  end
  else if Time.Text = 'Месяц' then
  begin
    f := a * Power(1 + b/12, x);
    Output.Lines.Add('Итоговая сумма за ' + FloatToStr(x) + ' месяцев: ' + FloatToStrF(f, ffCurrency, 12, 2));
  end
  else if Time.Text = 'Квартал' then
  begin
    f := a * Power(1 + b/4, x);
    Output.Lines.Add('Итоговая сумма за ' + FloatToStr(x) + ' кварталов: ' + FloatToStrF(f, ffCurrency, 12, 2));
  end
  else if Time.Text = 'Год' then
  begin
    f := a * Power(1 + b, x);
    Output.Lines.Add('Итоговая сумма за ' + FloatToStr(x) + ' лет: ' + FloatToStrF(f, ffCurrency, 12, 2));
  end;
end;
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
begin
  Close;
end;

procedure TForm1.FormCreate(Sender: TObject);
begin

end;

procedure TForm1.Label2Click(Sender: TObject);
begin

end;

procedure TForm1.Label4Click(Sender: TObject);
begin

end;

procedure TForm1.SumChange(Sender: TObject);
begin

end;

end.

