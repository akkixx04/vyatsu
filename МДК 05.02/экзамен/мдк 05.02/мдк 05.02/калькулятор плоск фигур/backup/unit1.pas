unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, Menus, StdCtrls, Math,
  ExtCtrls, Buttons;

type

  { TShapes }

  TShapes = class(TForm)
    EntryAnswer: TLabel;
    Entry1: TEdit;
    Entry3Label: TLabel;
    Entry3: TEdit;
    Entry2: TEdit;
    Entry1Label: TLabel;
    Entry2Label: TLabel;
    CalculationResultLabel: TLabel;
    CalculationResult: TMemo;
    SelectionOfShapesLabel: TLabel;
    SelectionOfShapes: TComboBox;
    procedure Entry1KeyPress(Sender: TObject; var Key: char);
    procedure Entry2KeyPress(Sender: TObject; var Key: char);
    procedure Entry3KeyPress(Sender: TObject; var Key: char);
    procedure EntryAnswerClick(Sender: TObject);
    procedure SelectionOfShapesChange(Sender: TObject);
  private
    First, Second, Third: string;
  public

  end;

var
  Shapes: TShapes;

implementation

{$R *.lfm}

{ TShapes }

procedure TShapes.SelectionOfShapesChange(Sender: TObject);
begin
   CalculationResult.Lines.Clear;
   case SelectionOfShapes.Text of
   'Параллелограмм (общий случай)':
     begin
        Entry1Label.Visible := True;
        Entry1.Visible := True;
        Entry2Label.Visible := True;
        Entry2.Visible := True;
        Entry3Label.Visible := False;
        Entry3.Visible := False;
        Entry1Label.Caption := 'Введите длину высоты параллелограмма (в см):';
        Entry2Label.Caption := 'Введите длину основания параллелограмма (в см):';
        Entry1.Text := chr(0);
        Entry2.Text := chr(0)
     end;
   'Квадрат':
     begin
        Entry1Label.Visible := True;
        Entry1.Visible := True;
        Entry2Label.Visible := False;
        Entry2.Visible := False;
        Entry3Label.Visible := False;
        Entry3.Visible := False;
        Entry1Label.Caption := 'Введите длину стороны квадрата (в см):';
        Entry1.Text := chr(0)
     end;
   'Прямоугольник':
     begin
        Entry1Label.Visible := True;
        Entry1.Visible := True;
        Entry2Label.Visible := True;
        Entry2.Visible := True;
        Entry3Label.Visible := False;
        Entry3.Visible := False;
        Entry1Label.Caption := 'Введите длину прямоугольника (в см):';
        Entry2Label.Caption := 'Введите ширину прямоугольника (в см):';
        Entry1.Text := chr(0);
        Entry2.Text := chr(0)
     end;
   'Ромб':
     begin
        Entry1Label.Visible := True;
        Entry1.Visible := True;
        Entry2Label.Visible := True;
        Entry2.Visible := True;
        Entry3Label.Visible := False;
        Entry3.Visible := False;
        Entry1Label.Caption := 'Введите длину первой диагонали (в см):';
        Entry2Label.Caption := 'Введите длину второй диагонали (в см):';
        Entry1.Text := chr(0);
        Entry2.Text := chr(0)
     end;
   'Круг':
     begin
        Entry1Label.Visible := True;
        Entry1.Visible := True;
        Entry2Label.Visible := False;
        Entry2.Visible := False;
        Entry3Label.Visible := False;
        Entry3.Visible := False;
        Entry1Label.Caption := 'Введите радиус круга (в см):';
        Entry1.Text := chr(0)
     end;
   'Трапеция':
     begin
        Entry1Label.Visible := True;
        Entry1.Visible := True;
        Entry2Label.Visible := True;
        Entry2.Visible := True;
        Entry3Label.Visible := True;
        Entry3.Visible := True;
        Entry1Label.Caption := 'Введите длину первого основания (в см):';
        Entry2Label.Caption := 'Введите длину второго основания (в см):';
        Entry3Label.Caption := 'Введите длину высоты трапеции (в см):';
        Entry1.Text := chr(0);
        Entry2.Text := chr(0);
        Entry3.Text := chr(0)
     end;
   'Правильный многоугольник':
     begin
        Entry1Label.Visible := True;
        Entry1.Visible := True;
        Entry2Label.Visible := True;
        Entry2.Visible := True;
        Entry3Label.Visible := False;
        Entry3.Visible := False;
        Entry1Label.Caption := 'Введите количество сторон:';
        Entry2Label.Caption := 'Введите длину стороны многоугольника (в см):';
        Entry1.Text := chr(0);
        Entry2.Text := chr(0)
     end;
   end;
end;

procedure TShapes.Entry1KeyPress(Sender: TObject; var Key: char);
begin
  Entry1.ReadOnly:= not ((Key in ['0'..'9', #8]) or ((Key in [',','.']) and ((pos(',', Entry1.Text) = 0) and (pos('.', Entry1.Text) = 0)) and (Entry1.Text <> '')))
end;

procedure TShapes.Entry2KeyPress(Sender: TObject; var Key: char);
begin
  Entry2.ReadOnly:= not ((Key in ['0'..'9',#8]) or ((Key in [',','.']) and ((pos(',', Entry2.Text) = 0) and (pos('.', Entry2.Text) = 0)) and (Entry2.Text <> '')))
end;

procedure TShapes.Entry3KeyPress(Sender: TObject; var Key: char);
begin
  Entry3.ReadOnly:= not ((Key in ['0'..'9',#8]) or ((Key in [',','.']) and ((pos(',', Entry3.Text) = 0) and (pos('.', Entry3.Text) = 0)) and (Entry3.Text <> '')))
end;

procedure TShapes.EntryAnswerClick(Sender: TObject);
var AnswerNum, p, FirstNum, SecondNum, ThirdNum: real;
    t: boolean;
begin
   CalculationResult.Lines.Clear;
   t:=False;
   case SelectionOfShapes.Text of
   'Параллелограмм (общий случай)':
     begin
         First:=Entry1.Text;
         Second:=Entry2.Text;
         if (First = '') or (Second = '') or (StrToFloat(First) = 0) or (StrToFloat(Second) = 0) then CalculationResult.Lines.Add('Ошибка! Неверный формат ввода! Строка ввода не должна быть пустой и параметр не должен быть равен 0.')
         else
           begin
             t:=True;
             FirstNum:=(Round(StrToFloat(First)*100)/100);
             SecondNum:=(Round(StrToFloat(Second)*100)/100);
             AnswerNum:=FirstNum * SecondNum;
           end;
     end;
   'Квадрат':
     begin
         First:=Entry1.Text;
         if (First = '') or (StrToFloat(First) = 0) then CalculationResult.Lines.Add('Ошибка! Неверный формат ввода! Строка ввода не должна быть пустой и параметр не должен быть равен 0.')
         else
           begin
             t:=True;
             FirstNum:=(Round(StrToFloat(First)*100)/100);
             AnswerNum:=sqr(FirstNum);
           end;
     end;
   'Прямоугольник':
     begin
         First:=Entry1.Text;
         Second:=Entry2.Text;
         if (First = '') or (Second = '') or (StrToFloat(First) = 0) or (StrToFloat(Second) = 0) then CalculationResult.Lines.Add('Ошибка! Неверный формат ввода! Строка ввода не должна быть пустой и параметр не должен быть равен 0.')
         else
           begin
             t:=True;
             FirstNum:=(Round(StrToFloat(First)*100)/100);
             SecondNum:=(Round(StrToFloat(Second)*100)/100);
             AnswerNum:=FirstNum * SecondNum;
           end;
     end;
   'Ромб':
     begin
         First:=Entry1.Text;
         Second:=Entry2.Text;
         if (First = '') or (Second = '') or (StrToFloat(First) = 0) or (StrToFloat(Second) = 0) then CalculationResult.Lines.Add('Ошибка! Неверный формат ввода! Строка ввода не должна быть пустой и параметр не должен быть равен 0.')
         else
           begin
             t:=True;
             FirstNum:=(Round(StrToFloat(First)*100)/100);
             SecondNum:=(Round(StrToFloat(Second)*100)/100);
             AnswerNum:=0.5 * FirstNum * SecondNum;
           end;
     end;
   'Круг':
     begin
         First:=Entry1.Text;
         if (First = '') or (StrToFloat(First) = 0) then CalculationResult.Lines.Add('Ошибка! Неверный формат ввода! Строка ввода не должна быть пустой и параметр не должен быть равен 0.')
         else
           begin
             t:=True;
             FirstNum:=(Round(StrToFloat(First)*100)/100);
             AnswerNum:=Pi*sqr(FirstNum);
           end;
     end;
   'Трапеция':
     begin
         First:=Entry1.Text;
         Second:=Entry2.Text;
         Third:=Entry3.Text;
         if (First = '') or (Second = '') or (Third = '') or (StrToFloat(First) = 0) or (StrToFloat(Second) = 0) or (StrToFloat(Third) = 0) then CalculationResult.Lines.Add('Ошибка! Неверный формат ввода! Строка ввода не должна быть пустой и параметр не должен быть равен 0.')
         else
           begin
             t:=True;
             FirstNum:=(Round(StrToFloat(First)*100)/100);
             SecondNum:=(Round(StrToFloat(Second)*100)/100);
             ThirdNum:=(Round(StrToFloat(Third)*100)/100);
             AnswerNum:=0.5 * (FirstNum + SecondNum) * ThirdNum;
           end;
     end;
   'Правильный многоугольник':
     begin
         First:=Entry1.Text;
         Second:=Entry2.Text;
         if (First = '') or (Second = '') or (StrToFloat(First) = 0) or (StrToFloat(Second) = 0) or (StrToFloat(First)<>Round(StrToFloat(First))) then CalculationResult.Lines.Add('Ошибка! Неверный формат ввода! Строка ввода не должна быть пустой, параметр не должен быть равен 0 и количество сторон должно быть выражено целым числом.')
         else
           begin
             t:=True;
             FirstNum:=(Round(StrToFloat(First)*100)/100);
             SecondNum:=(Round(StrToFloat(Second)*100)/100);
             AnswerNum:=(FirstNum/4)*sqr(SecondNum)* Cot(Pi/FirstNum);
           end;
     end;
   end;
   if t then
   begin
      CalculationResult.Font.Size:=20;
      CalculationResult.Lines.Add(FloatToStr(Round(AnswerNum*100)/100) + ' кв.см')
   end;
end;



end.

