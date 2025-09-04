unit Edit;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons;

type

  { TfEdit }

  TfEdit = class(TForm)
    bSave: TBitBtn;
    bCancel: TBitBtn;
    CBNote: TComboBox;
    eTelephone: TEdit;
    eName: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    procedure eNameKeyPress(Sender: TObject; var Key: char);
    procedure eTelephoneKeyPress(Sender: TObject; var Key: char);
    procedure FormShow(Sender: TObject);
  private

  public

  end;

var
  fEdit: TfEdit;

implementation

{$R *.lfm}

{ TfEdit }

procedure TfEdit.eTelephoneKeyPress(Sender: TObject; var Key: char);
begin
  if not (Key in ['0'..'9', '+', '-', #8]) then Key := #0;
end;

procedure TfEdit.FormShow(Sender: TObject);
begin
  eName.SetFocus;
end;



end.

