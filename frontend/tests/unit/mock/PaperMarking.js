import nock from "nock";

nock(/.*/)
  .get(/\/api\/paper_records\/.*/, () => true)
  .once()
  .reply(200, {
    questions: {
      "1": {}
    }
  });
nock(/.*/)
  .get(/\/api\/paper_records\/.*/, () => true)
  .once()
  .reply(400, {
    questions: {
      "1": {}
    }
  });

