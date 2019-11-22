import nock from "nock";

nock(/.*/)
  .delete("/api/question_banks/1/")
  .reply(200, {
    token: "ok"
  });

nock(/.*?/)
  .get("/api/question_banks/")
  .once()
  .reply(200, [1, 2]);

nock(/.*?/)
  .get("/api/question_banks/")
  .twice()
  .reply(500, {
    result: "failed"
  });

nock(/.*?/)
  .get("/api/question_banks/1/")
  .reply(200, {
    id: 1,
    name: "test1",
    brief: "brief",
    picture: "mdi-eye",
    authority: "private",
    createTime: "now",
    lastUpdate: "now",
    question_count: 100,
    invitation_code_count: 0,
    activated_code_count: 0
  });

nock(/.*?/)
  .get("/api/question_banks/2/")
  .reply(200, {
    id: 2,
    name: "test2",
    brief: "brief",
    picture: "mdi-eye",
    authority: "private",
    createTime: "now",
    lastUpdate: "now",
    question_count: 100,
    invitation_code_count: 0,
    activated_code_count: 0
  });

  nock(/.*?/)
    .put("/api/accounts/users/200/")
    .reply(200, {
      id: 200,
      question_banks: [1]
    })

  nock(/.*?/)
    .put("/api/accounts/users/500/")
    .reply(500, {
      results: "Failed"
    })