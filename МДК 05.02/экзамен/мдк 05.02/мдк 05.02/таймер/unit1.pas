unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, Spin, StdCtrls,
  ComCtrls, ExtCtrls, Buttons, MMSystem;

type

  { TForm1 }

  TForm1 = class(TForm)
    BitBtn1: TBitBtn;
    Start: TButton;
    Status: TLabel;
    Sound: TCheckBox;
    Progress: TProgressBar;
    lbMinutes: TLabel;
    lbSeconds: TLabel;
    Minutes: TSpinEdit;
    Seconds: TSpinEdit;
    Stop: TButton;
    Reset: TButton;
    Timer1: TTimer;
    procedure FormCreate(Sender: TObject);
    procedure ResetClick(Sender: TObject);
    procedure StartClick(Sender: TObject);
    procedure StopClick(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
  private
  FTotalSeconds: Integer;
  FRemainingSeconds: Integer;
  procedure UpdateDisplay;
  procedure PlaySound;
  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.FormCreate(Sender: TObject);
begin
  Minutes.Value := 1;
  Seconds.Value := 0;
  FTotalSeconds := 0;
  FRemainingSeconds := 0;
  Status.Caption := 'Готов к работе';
  Progress.Position := 100;
end;

procedure TForm1.ResetClick(Sender: TObject);
begin
  Timer1.Enabled := False;
  FRemainingSeconds := FTotalSeconds;
  UpdateDisplay;
  Status.Caption := 'Таймер сброшен';
end;

procedure TForm1.StartClick(Sender: TObject);
begin
  if Timer1.Enabled then Exit;

  FTotalSeconds := Minutes.Value * 60 + Seconds.Value;
  if FTotalSeconds <= 0 then
  begin
    ShowMessage('Установите время больше 0 секунд');
    Exit;
  end;

  FRemainingSeconds := FTotalSeconds;
  UpdateDisplay;

  Timer1.Enabled := True;
  Status.Caption := 'Таймер запущен';
end;

procedure TForm1.StopClick(Sender: TObject);
begin
   Timer1.Enabled := False;
  Status.Caption := 'Таймер остановлен';
end;

procedure TForm1.Timer1Timer(Sender: TObject);
begin
  Dec(FRemainingSeconds);
  UpdateDisplay;

  if FRemainingSeconds <= 0 then
  begin
    Timer1.Enabled := False;
    Status.Caption := 'Время вышло!';
    if Sound.Checked then
      PlaySound;
  end;
end;

procedure TForm1.UpdateDisplay;
var
  M, S: Integer;
begin
  M := FRemainingSeconds div 60;
  S := FRemainingSeconds mod 60;

  Minutes.Value := M;
  Seconds.Value := S;

  if FTotalSeconds > 0 then
    Progress.Position := Round((FRemainingSeconds / FTotalSeconds) * 100);
end;

procedure TForm1.PlaySound;
begin
  sndPlaySound('SystemAsterisk', SND_ASYNC);
end;

end.

