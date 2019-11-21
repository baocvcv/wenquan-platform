import nock from "nock";

nock(/.*/)
  .get(/\/api\/question_records\/.*/)
  .once()
  .reply(200, {
    correct_or_not: [true]
  });
nock(/.*/)
  .get(/\/api\/question_records\/.*/)
  .once()
  .reply(400, {
    correct_or_not: true
  });
nock(/.*/)
  .put(/\/api\/paper_records\/.*/)
  .once()
  .reply(200, {
    correct_or_not: true
  });
nock(/.*/)
  .put(/\/api\/paper_records\/.*/)
  .once()
  .reply(400, {
    correct_or_not: true
  });