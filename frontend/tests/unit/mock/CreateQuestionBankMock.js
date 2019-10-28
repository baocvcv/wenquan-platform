import nock from "nock";

nock(/.*?/)
  .post("/api/question_banks/", content => content.name != "Error")
  .reply(200, {
    data: { id: 1 }
  });
