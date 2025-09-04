unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  Buttons;

type

  { TStopwatch }

  TStopwatch = class(TForm)
    ExitBt: TBitBtn;
    out: TLabel;
    StartBt: TButton;
    ResetBt: TButton;
    PauseBt: TButton;
    Timer: TTimer;
    procedure ResetBtClick(Sender: TObject);
    procedure StartBtClick(Sender: TObject);
    procedure PauseBtClick(Sender: TObject);
    procedure MyTimer(Sender: TObject);
  private
    FStartTime: TDateTime;
    FElapsedBeforePause: TDateTime;
    FIsRunning: Boolean;
    FIsPaused: Boolean;
  public

  end;

var
  Stopwatch: TStopwatch;

  start : Double;
  b : Boolean;

implementation

{$R *.lfm}

{ TStopwatch }

function GetTime : TDateTime;
var
  s : TSystemTime;
begin
  GetLocalTime(s);
  Result := SystemTimeToDateTime(s);

end;

procedure TStopwatch.StartBtClick(Sender: TObject);
begin
  if not FIsRunning then
  begin
    FStartTime := Now;
    FElapsedBeforePause := 0;
    FIsRunning := True;
    FIsPaused := False;
    Timer.Enabled := True;
  end
  else if FIsPaused then
  begin
    FStartTime := Now - FElapsedBeforePause;
    FIsPaused := False;
    Timer.Enabled := True;
  end;
end;

procedure TStopwatch.ResetBtClick(Sender: TObject);
begin
  Timer.Enabled := False;
  FIsRunning := False;
  FIsPaused := False;
  FElapsedBeforePause := 0;
  Out.Caption := '00:00:00 000';
end;


procedure TStopwatch.PauseBtClick(Sender: TObject);
begin
  if FIsRunning and not FIsPaused then
  begin
    FElapsedBeforePause := Now - FStartTime;
    FIsPaused := True;
    Timer.Enabled := False;
  end;
end;


procedure TStopwatch.MyTimer(Sender: TObject);
begin
  if FIsRunning and not FIsPaused then
    Out.Caption := FormatDateTime('hh:mm:ss zzz', Now - FStartTime);
end;

end.

