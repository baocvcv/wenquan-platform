import nock from "nock";

nock(/.*/)
  .get(/\/api\/papers\/.*/)
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
  .get("/api/paper_sections/1/", () => true)
  .reply(200, {
    questions: [
      {
        id: 1
      }
    ]
  });
nock(/.*/)
  .get("/api/questions/1/", () => true)
  .reply(200, {
    content: {}
  });
