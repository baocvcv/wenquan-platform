import nock from "nock";

nock(/.*/)
  .delete("/api/question_banks/1/", data => data.id == 1)
  .reply(200, {
    token: "ok"
  });

nock(/.*/)
  .delete("/api/question_banks/1/", data => data.id != 1)
  .reply(403, {
    token: "failed"
  });
