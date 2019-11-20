import nock from "nock";

nock(/.*/)
  .get(/\/api\/papers\/.*/, () => true)
  .reply(200, {
    sections: [
      {
        id: 1,
        questions: [
          {
            id: 1
          }
        ]
      }
    ]
  });
nock(/.*/)
  .get(/\/api\/paper_sections\/.*/, () => true)
  .reply(200, {
    questions: [
      {
        id: 1
      }
    ]
  });
nock(/.*/)
  .get(/\/api\/questions\/.*/, () => true)
  .reply(200, {
  });
nock(/.*/)
  .post("/api/paper_records/", () => true)
  .reply(200, {
    questions: [
      {
        id: 1
      }
    ]
  });
nock(/.*/)
  .post(/.*/, () => true)
  .once()
  .reply(200, {
    questions: [
      {
        id: 1
      }
    ]
  });
nock(/.*/)
  .post(/.*/, () => true)
  .reply(400, {
    questions: [
      {
        id: 1
      }
    ]
  });

