unit obmen;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons;

type

  { TForm1 }

  TForm1 = class(TForm)
    BitBtnExit: TBitBtn;
    ButtonObmen: TButton;
    EditNum1: TEdit;
    EditNum2: TEdit;
    LabelNum1: TLabel;
    LabelNum2: TLabel;
    procedure BitBtnExitClick(Sender: TObject);
    procedure ButtonObmenClick(Sender: TObject);
    procedure LabelNum1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  C: string;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.LabelNum1Click(Sender: TObject);
begin

end;

procedure TForm1.BitBtnExitClick(Sender: TObject);
begin
  Close
end;

procedure TForm1.ButtonObmenClick(Sender: TObject);
begin
  C:=EditNum1.text;
  EditNum1.text:=EditNum2.text;
  EditNum2.text:=C;
end;

end.

