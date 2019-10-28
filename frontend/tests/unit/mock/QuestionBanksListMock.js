import nock from "nock";

nock(/.*/)
  .delete("/api/question_banks/1/")
  .reply(200, {
    token: "ok"
  });
