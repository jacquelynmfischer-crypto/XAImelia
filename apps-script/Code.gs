// Google Apps Script attached to the "AImelia Survey Responses" sheet.
// Deploy as a web app (Execute as: Me, Who has access: Anyone).
// doPost receives each player's survey answers from the game; doGet returns
// completed responses to the password-protected Results page.
const KEY = 'XAI';
function sheet_() { return SpreadsheetApp.getActiveSpreadsheet().getSheets()[0]; }
function doPost(e) {
  const d = JSON.parse(e.postData.contents), sh = sheet_();
  if (!sh.getRange(1, 9).getValue()) sh.getRange(1, 9).setValue('message');
  sh.appendRow([new Date(), d.id, d.name, d.age, d.ai,
    JSON.stringify(d.pre), JSON.stringify(d.post), d.minutes, d.message || '']);
  return ContentService.createTextOutput('ok');
}
function doGet(e) {
  const out = (x) => ContentService.createTextOutput(JSON.stringify(x))
    .setMimeType(ContentService.MimeType.JSON);
  if ((e.parameter.key || '').toUpperCase() !== KEY) return out([]);
  const latest = {};
  sheet_().getDataRange().getValues().slice(1).forEach(r => {
    latest[r[1]] = { id: r[1], name: r[2], age: r[3], ai: r[4],
      pre: JSON.parse(r[5] || 'null'), post: JSON.parse(r[6] || 'null'),
      minutes: r[7], message: r[8] || '' };
  });
  return out(Object.values(latest).filter(o => o.pre && o.post));
}
